# Argument collector for the deploy script

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--job", type=str, help="Specifies the name of the job to use. Default is ds_validation", default="ds_validation")
parser.add_argument("--create-required", type=bool, help="Indicates if we need to use this script to create an image. Default is false.", default=False)
parser.add_argument("--containers", type=str, help="Comma separated string with a list of containers to deploy. Default is empty", default="")
parser.add_argument("--channel", type=str, help="Specifies the channel (ID) to output to slack. Default is ds_data_validation", default="ds_validation")
parser.add_argument("--fail_channel", type=str, help="Specifies the channel (ID) to output to slack in the event of failures. Default is None", default=None)
parser.add_argument("--start", type=str, help="Specifies a start date for validation. Default is blank, which will use 30 days relative to yesterday. Format: mm/dd/yyyy", default="")
parser.add_argument("--end", type=str, help="Specifies an end date for validation. Default is blank, which will force validation to end at yesterday. Format: mm/dd/yyyy", default="")
parser.add_argument("--merchants", type=str, help="Specifies which merchant to run. Default is a set of 5 top merchants.", default="default")
parser.add_argument("--skip-slack", action="store_true", help="Indicates if we should skip posting to Slack for this run. Default is False")
parser.add_argument("--skip-logging", action="store_true", help="Indicates if logging should be skipped to the master spreadsheet")
parser.add_argument("--tag", type=str, help="Gives the tag label for the deployment. Default is test", default="test")
parser.add_argument("--simulation", type=str, help="Switches the simulation (e.g. kiran_dev). Default is empty", default="")
parser.add_argument("--timeout", type=int, help="Sets the timeout for running the rgeression test before failing. Default is 5 minutes", default=3000)
parser.add_argument("--source", type=str, help="Tells the picker to use a particular data source. Default is empty, which will use typical fallback system.", default="")
parser.add_argument("--dev", action="store_true", help="Run in dev mode with functions for debugging")
parser.add_argument("-ne", "--no-error", action="store_true", help="Run the Picker Test suite iteartion of this library (see README)")
parser.add_argument("-native", "--native", action="store_true", help="Tells the Picker test suite to run with NATIVE currency") # FIXME: We COULD set this to toggle the main regression too
args = parser.parse_args()
