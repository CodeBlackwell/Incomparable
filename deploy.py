# This is an executable deployment script with several functions for posting to Slack
# Largely based off of the existing set up in the Talend jobs
# This version is primarily for the regression library
'''
Note the following default run settings:
Merchants: REI.com,Black Diamond Equipment,Carousel Checks,Palmetto State Armory,RTIC Outdoors
(Reference available in merchant_map.json)
By default, we run for all metrics for these merchants for the following intervals:
    - Last 30 days
    - Last Year
'''

import sys
import os
import subprocess
import configparser
import argparse
import datetime
import logging
import json
import subprocess
import glob
import shutil
import time
import pandas as pd
import requests
import traceback

from datetime import datetime, timedelta
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
from pretty_tables import PrettyTableMaker
from runtime_args import args
from run_commands import NoErrorCommand, RunCommand, NoLoggingCommand
from data_sources import DataSource, RedshiftDataSource

# Get API key for file attachment
config = configparser.ConfigParser()
if args.dev is True:
    config_file = 'avantlinkpy2.conf' # Relative path- assumes config in current dir
else:
    config_file = '/home/ubuntu/ds-data_validation/avantlinkpy2.conf' # Cron needs whole path
config.read(config_file)
slack_key = config.get('slack', 'api_key')

def post_to_slack(channel, msg, fid, merchant, source, timeout=False, js=None, fail_channel=None):
    '''
    Posts a message to the chosen Slack channel

    Parameters:
        channel: str, the slack channel to post the alert to
        msg: str, contents to post to the Slack channel
        fid: str, gives the name of the file to post to Slack as an attachment
        merchant: str, the merchant name tied to this data result
        source: str, describes data source we're loading from (displays in title)
        timeout: boolean (optional), indicates if a timeout happened
        js: json object (optional), contains a set of metadata required for reporting on the test suite (only usage)
        fail_channel: str, if given will route the failures to a separate channel

    Returns:
        None
    '''
    # Check if a separate fail channel was given
    # If not, pipe all outputs to the same place
    if fail_channel is None:
        fail_channel = channel

    # If a timeout happend, go ahead and post that and carry on
    if timeout is True:
        # API Timeout failures
        if "API" in msg:
            title = msg
            channel = 'edw3_data_errors'
        # Generic timeout
        else:
            title = f'{merchant} timed out'

        # Append sim name to test if valid
        if args.simulation != '':
            title += f' ({args.simulation})'
        cmd = f'''curl -d "text={title}" -d "channel={channel}" -H "Authorization: Bearer {slack_key}" -X POST https://slack.com/api/chat.postMessage -k'''
        proc = subprocess.run(cmd, shell=True, timeout=30, stdout=subprocess.PIPE)
        result = json.loads(proc.stdout)
        return

    # Picker test suite doesn't post excel files
    # Instead post a pass/fail
    if fid is None:
        # Unpack json results for Slack
        try:
            title = js['test_name']
            edw3_ro = js['edw3_request_object']
            errors = js['errors']
        except:
            raise FileNotFoundError(f'The request json file {js} is missing required content for the test suite')

        # Append sim name to test if valid
        if args.simulation != '':
            title += f' ({args.simulation})'

        # Indicate NATIVE if used
        if args.native:
            title += '- NATIVE currency'

        # Try to build an error message
        # If it isn't there, use the default
        if js['error_status'] == 'N/A':
            pass
        else:
            try:
                error_dict = json.loads(js['error_status'][0])
                error_msg = error_dict['error']
            except(IndexError, KeyError, json.decoder.JSONDecodeError):
                error_msg = 'Error: Report could not be prepared at this time.'
            except TypeError:
                error_msg = 'Request returned no data' # This may be expected

        # Create temp file
        fid = 'edw3_request_objects.json'
        with open(fid, 'a+') as f:
            f.write(json.dumps(edw3_ro))

        # Post to Slack and exit
        if errors is False:
            title += ' passed'
            cmd = f'''curl -d "text={title}" -d "channel={channel}" -H "Authorization: Bearer {slack_key}" -X POST https://slack.com/api/chat.postMessage -k'''
        else:
            title += f' FAILED! {error_msg}'
            cmd = f"curl -F title='{fid}' -F initial_comment='{title}'  --form-string channels={fail_channel} -F file=@{fid} -F filename={fid} -F token={slack_key} https://slack.com/api/files.upload -k"
        proc = subprocess.run(cmd, shell=True, timeout=30, stdout=subprocess.PIPE)
        result = json.loads(proc.stdout)

        # Delete temp file
        os.remove(fid)
        return

    # Read file into dataframe
    df = pd.read_excel(fid)
    columns = df.columns.to_list()

    # Account for case where edw3 is 0 and edw2 is null
    # In this case, we want these values to be treated as the same, so replace nan with 0
    df = df.fillna(0)

    # Check if file matches between edw2 and edw3
    # Only send those that do not match to Slack
    source_error = False
    data_source = None
    pass_fail = df['pass/fail'][0]
    report_name = ''
    edw3_request_object = None
    for column in columns:
        if "edw2" in column and "request_object" not in column:
            edw2_column = column
        elif "edw3" in column and "request_object" not in column:
            if column == 'SQL_source' and df[column][0] != args.source:
                data_source = df[column][0]
                source_error = True
                edw3_request_object = df['edw3_request_object'][0]
            edw3_column = column
        # Grab report name  for metadata dict
        elif column == "Dashboard Report Name":
            report_name = df[column][0]

    if df[edw2_column].equals(df[edw3_column]) is True:
        pass
    else:
        # Checks for edge case where edw2 and edw3 are different data type but all 0s
        if (df[edw3_column] == 0).all() and(df[edw2_column] == 0).all():
            pass_fail = 'PASSED! ALL ZEROES!'

    # Build an upload curl command to post to slack
    # The components here govern how the data is displayed- note the display file name != system file name
    # NOTE: If we match, just post the test passed
    upload_name = merchant + '_' + fid.split('/')[-1]
    source = source.replace('fact_', '')
    temp_file = None
    if 'PASS' in pass_fail and source_error is False:
        if args.source != '':
             title = upload_name.replace('.xlsx', '') + f' ({source}) passed'
        else:
            title = upload_name.replace('.xlsx', '') + f' passed'
            passed = True
        cmd = f'''curl -d "text={title}" -d "channel={channel}" -H "Authorization: Bearer {slack_key}" -X POST https://slack.com/api/chat.postMessage -k'''
    # Cover the case where we requested a particular source, but got something else back instead
    # Here we want to post request object and mention the requested source but what we got instead
    elif source_error is True:
        title = upload_name.replace('.xlsx', '') + f' ({source})' + f'exepected to be sourced from {{args.source}} but returned from {{data_source}}'

        # Write request object to file
        temp_file = 'edw3_request_object.json'
        with open('edw3_request_object.json', 'w+') as f:
            f.write(json.dumps(edw3_request_object))

        # Log the fail to slack
        cmd = f"curl -F title='{title}' -F initial_comment='{title}'  --form-string channels={fail_channel} -F file=@{temp_file} -F filename={upload_name} -F token={slack_key} https://slack.com/api/files.upload -k"

    else:
        if args.source != '':
            title = upload_name.replace('.xlsx', '') + f' ({source})' + ' FAILED!'
        else:
            title = upload_name.replace('.xlsx', '') + ' FAILED!'
        # Simplify summary name
        if 'summary' in upload_name:
             upload_name = merchant + '_' + 'Combined_Summary.xlsx'
        cmd = f"curl -F title='{upload_name}' -F initial_comment='{title}'  --form-string channels={fail_channel} -F file=@{fid} -F filename={upload_name} -F token={slack_key} https://slack.com/api/files.upload -k"
    try:
        proc = subprocess.run(cmd, shell=True, timeout=30, stdout=subprocess.PIPE)
        result = json.loads(proc.stdout)
    except subprocess.TimeoutExpired:
        # Slack server must be busy- Well that sucks
        return

    # Log result
    # If it failed, log the stdout for debug
    if result["ok"] is True:
        print('Posted to Slack')
        errors = False
    else:
        print('Error posting to slack')
        print(result)
        errors = True

    # Remove temp file (if used)
    if temp_file is not None:
        os.remove(temp_file)
    return result, errors, pass_fail, report_name

def build_file_list():
    '''
    Builds a list of files by walking the file path
    Uses a relative path to where Le's code outputs the files
    At some point, might want to be able to choose which files to include or not
    '''
    output_dir = 'DataValidation/validation_outputs/xlsx/'
    file_list = []

    # If the output dir doesn't exist, make it for the user
    # However, the regression lib won't have files. Notify for a rerurn with an error
    if not os.path.exists(output_dir):
       os.mkdir('DataValidation/validation_outputs')
       os.mkdir(output_dir)
       raise Exception('The output directory for the data files was not present. This has been made for you, but a rerun is neccessary to generate files')

    # Walk the data directory and grab all output files (not dirs)
    for root, dirs, files in os.walk(output_dir):
        for name in files:
            fid = os.path.join(root, name)
            # Only applend excel files
            if name.endswith('.xlsx'):
                # Replace empty spaces with _
                if ' ' in fid:
                    try:
                        os.rename(fid, fid.replace(' ', '_'))
                        fid = fid.replace(' ', '_')
                    except FileNotFoundError:
                        print(fid)
                        raise
                file_list.append(fid)
    return file_list

def calculate_times(now):
    '''
    Builds lists of start and end times
    We'll exclude today and run for the following:
        - month_to_date (30 days back from yesterday)
        - last_month
        - last_year

    Parameters:
        now: datetime, gives the current time

    Returns:
        start_times: a list of start times
        end_times: a list of end times to use
    '''
    # Drop time
    now = now.replace(hour=0, minute=0, second=0)

    # Last 30 days
    mtd_end = now - timedelta(days=1)
    mtd_start = mtd_end - timedelta(days=30)

    # Last month
    day_of_month = int(now.strftime("%d"))
    lm_end = now - timedelta(days=day_of_month)
    lm_start = lm_end.replace(day=1)
    lm_end = lm_end + timedelta(days=1)

    # Last year
    doy = int(now.strftime("%j"))
    ly_end = now - timedelta(days=doy)
    ly_start = ly_end - timedelta(days=364)
    ly_end = ly_end + timedelta(days=1)

    # Collect into lists
    start_times = [mtd_start, lm_start, ly_start]
    end_times = [mtd_end, lm_end, ly_end]
    return start_times, end_times


def build_metadata(result, fid, merchant, source, passed, report_name, channel='C04HP5S5YNB'):
    '''
    This function compiles a json dictionary of metadata to send to the regression library dashboard
    Link:https://drive.google.com/drive/u/0/folders/1Pr0FWGKWu1Ji2tTkRlcsOCD2dMp2G3X6

    Parameters
        result: json object returned from Slack giving all of the parameters used to identify the post
        fid: str, full file path of the file posted, used to break apart into identifiers
        merchant: str, merchant used in this regression run
        source: str, location data came from (e.g. Redshift)
        passed: boolean, indicates pass/fail of regression test
        channel: str, channel used to find the message. Default is ds_data_validation in string form
        report_name: str, gives the proper name of the report to display on the dahsboard

    Returns:
       None
    '''
    # Grab the identifier for the message
    try:
        url = result['file']['permalink']
    except:
        message_ts = result['message']['ts']
        client = WebClient(token=slack_key)
        result = client.chat_getPermalink(
            channel=channel,
            message_ts=message_ts
        )
        url = result['permalink']

    # If the source is an empty string, replace that with olap for top_affiliates
    # For trend, default is cube_postgres
    metadata_string = fid.split('/')
    widget = metadata_string[-3]
    if widget == 'EDW3_Production':
        return None
    if source == '':
        if widget in ['top_affiliates_widget', 'combined_summary']:
            source = 'cube_olap'
        else:
            source = 'cube_postgres'

    # Build the json dictionary we need for the dashboard
    # {Widget, category, report name, merchant name, slack link}
    # Split fid into metadat pieces
    report = metadata_string[-1].replace('.xlsx', '')
    category = metadata_string[-2].replace('_', ' ')
    metadata = {
        "widget": widget,
        "category": category,
        "report": report,
        "data_source": source,
        "link": url,
        "passed": passed,
        "file": fid,
        "report_name": report_name
    }

    return metadata

if __name__ == "__main__":
    # Accept list of merchants
    # The "default" gives a list of 5 merchants we frequently run. This is the default setting
    if args.merchants == 'default':
        if args.no_error:
            merchants = ['REI.com']
        else:
            merchants = 'REI.com,black diamond equipment,Carousel Checks,Palmetto State Armory,RTIC Outdoors,A Life Plus'.split(',')
    # For all merchants, read from merchant map and run them all
    elif args.merchants == 'all':
        with open('merchant_map.json', 'r+') as f:
            data_set = json.load(f)
            merchants = list(data_set.values())
    # Custom list or single entry- supports multiple merchants
    else:
        merchants = args.merchants.split(',')

    # Check is source was specified. If it was, confirm we can use it
    if args.source == 'fact_redshift':
        source = RedshiftDataSource()
    else:
        source = DataSource(source=args.source)

    # Check for simulation
    if args.simulation != "":
        sim = args.simulation
    else:
        sim = None

    # Grab dates (30 days back ending yesterday is default)
    now = datetime.utcnow().replace(microsecond=0)
    if args.start == '' and args.end == '':
        start_times, end_times = calculate_times(now)
    else:
        # Cover case where end wasn't given
        if args.start != '' and args.end == '':
            logging.warning('Start given without end. Defaulting to now')
            end = now
        start_times = args.start.split(',')
        end_times = args.end.split(',')

    # Run for every input date
    for index, start_time in enumerate(start_times):
        start = start_times[index]
        end = end_times[index]

        # Try to parse dates
        # Since we allow input args for this, print a complaint if format fails
        try:
            end = end.strftime('%m/%d/%Y')
            start = start.strftime('%m/%d/%Y')
        except Exception as e:
            logging.error(f'Unable to process input args {start} and {end}')
            print('Hint: start/end should be in the format mm/dd/yyyy')
            print(e)

        # Make sure end isn't after now
        if datetime.strptime(end, '%m/%d/%Y') > now:
            logging.warning(f'End time given {end} is in the future! Resetting to now')
            end = now

        # Move to working directory (for cron only)
        if not args.dev:
            os.chdir('/home/ubuntu/ds-data_validation/')

        # Trigger script
        for merchant in merchants:
            metadata_dict = {} # By merchant
            metadata_dict[merchant] = []
            og_merchant = merchant
            print(f'Running regression for merchant {merchant}')
            try:
                os.chdir('DataValidation')
            except:
                print(os.getcwd())
            # Cannot use spaces in cli, replace with _
            merchant = merchant.replace(' ', '_')
            if args.no_error:
                if args.native:
                    native = True
                else:
                    native = False
                run_command = NoErrorCommand(merchants=merchant, source=source.source, sim=sim, native=native)
            else:
                #cmd = f'python -m sources.comparison -ra -sd {start} -ed {end} -mer {merchant}' # FIXME: Le's script hasn't been tested with custom times
                # Generally, logging will be done here: https://docs.google.com/spreadsheets/d/1JKJ_hQA4xzOxPHEd1xqgAPYk9vfmgpxeGXf21sBkWYw/edit#gid=0
                # It can be skipped however (see args)
                if args.skip_logging is False:
                    run_command = RunCommand(merchants=merchant, source=source.source)
                else:
                    run_command = NoLoggingCommand(merchants=merchant, source=source.source)
            cmd = run_command.command

            # Print the command and run it
            # If it should fail, make note of that here as well so we can print that out to slack
            try:
                result = subprocess.run(cmd, shell=True, timeout=args.timeout)
                return_code = result.returncode
                timeout = False
            except subprocess.TimeoutExpired:
                timeout = True # Log the timeout and then continue
                return_code = 1

            # If returned 1 (error), set timeout
            if return_code == 1:
                timeout = True

            # Slack configurations
            # Note the file tree here:
            '''
            xlsx
                date folder
                    regression test folder
                        EDW3_Production
                            xlsx file
            '''
            os.chdir('..')
            # Give the option to bypass Slack posting
            if args.skip_slack is False:
                channel = args.channel
                fail_channel = args.fail_channel
                msg = f'''Regression test results ({now} run)'''
                logging.info(msg)

                # For Picker test suite, don't post files
                # Instead, grab results from the log file on disk
                if args.no_error is True:
                    json_dicts = []
                    test_file = 'DataValidation/test_suite_outputs.json'
                    try:
                        with open(test_file) as f:
                            for line in f:
                                json_dicts.append(json.loads(line))
                    except Exception as e:
                        json_dicts = []

                    # Post results to Slack and cleanup if we get no results, post an API timesout
                    if not json_dicts:
                        post_to_slack(fail_channel, 'The API appears to have timed out', None, merchant, source.source, timeout=timeout, fail_channel=fail_channel)
                    else:
                        for json_dict in json_dicts:
                            post_to_slack(channel, msg, None, merchant, source.source, timeout=timeout, js=json_dict, fail_channel=fail_channel)
                    try:
                        os.remove(test_file)
                    except:
                        raise Exception('Test suite file is missing! Check file generator')

                # Routine data validation
                # Post each result to Slack with a pass/fail message
                else:
                    file_list = build_file_list()
                    # If no files, post a special message to Slack
                    if not file_list:
                        post_to_slack(fail_channel, 'The API appears to have timed out', None, merchant, source.source, timeout=timeout, fail_channel=fail_channel)
                    else:
                        for fid in file_list:
                            # If blacklisted, let us know that and skip
                            skipped = False
                            for item in source.blacklist:
                                if item in fid:
                                    print(f'Skipped blacklisted entry {fid}')
                                    skipped = True
                            if skipped is False:
                                result, errors, passed, report_name = post_to_slack(channel, msg, fid, merchant, source.source, timeout=timeout, fail_channel=fail_channel)
                                metadata_entry = build_metadata(result, fid, merchant, source.source, passed, report_name)
                                try:
                                    if metadata_entry is not None:
                                        metadata_dict[og_merchant].append(metadata_entry)
                                except KeyError:
                                    pass # Skip duplicates
                                time.sleep(1) # Because there's so many messages coming through at once otherwise
                                # Only post 1 timeout message
                                if timeout is True:
                                    break
                                # For dev mode, run just once for testing purposes
                                if args.dev is True and metadata_dict[og_merchant]:
                                    break

            # Send to dashboard- but not for Test suite
            if args.no_error is False:
                try:
                    dashboard = PrettyTableMaker(merchant_summary_from_deploy=metadata_dict)
                    dashboard.run()
                    print('Data sent to dashboard')
                except Exception:
                    print(traceback.format_exc())

            # Cleanup files stored on server
            files = glob.glob('DataValidation/validation_outputs/xlsx/*')
            for fid in files:
                shutil.rmtree(fid)
            print(f'Cleanup done for merchant {merchant}')

            # On the conclusion of each run, wait 30 seconds if running again
            # This is to prevent Slack from blocking outputs
            if merchant.replace('_', ' ') != merchants[-1]:
                print('Waiting 30 seconds before starting next merchant...')
                time.sleep(30)

        break # This is to skip the extra time ranges for now
