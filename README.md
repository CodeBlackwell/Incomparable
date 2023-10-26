# ds-data_validation repo readme

## Purpose

This is the repo we (the DS team) use for end to end validation and provide as overview of the health of the system. This repo uses versioning as we work through issues and find bugs. This readme provides an overview of what's in here, how to use it, and much more!

## How the regression works
TODO: Le, fill this in when you get the chance

## The deploy.py script

The deploy script is our executable "wrapper" script that launches the regression library with default settings (and some customizations!). This script can be run by simply running python deploy.py from the root directory of the repo, which will invoke the script with default settings. Those settings are as follows (January 2022):

- Job name: ds_validation
- Channel to output to: ds_validation
- Some container stuff (it's all skipped and commented out right now)
- A blank start... this equates to the following start times:
    - Today - 31 days (last 30 days)
    - 1st day of last month (last month)
    - 1st day of last year (last year)
- A blank end... this equates to the following end times:
    - Today - 1 days (last 30 days)
    - 1st day of this month- non-inclusive (last month)
    - 1st day of this year- non-inclusive (last year)
- Merchants: all (which runs the top 5 merchants as of this release
- Skip-slack = False. This prevents suppressing output to Slack.

The following arguments are available for the deploy script:
--job: Gives the name of the job. Mostly unused
--create-required: For containers. Keep false.
--containers: Unused, keep blank.
--channel: The output channel to Slack. Use this flag to output to a different channel
--start: The start time for validation. Can be specified here to manually choose an interval to run
--end: Ditto here except for the end time. If unspecified, will default to start + 30 days or now
--merchants: Allows for a list of merchants specified to run for (no spaces). Can be by name or uuid (see DataValidation/json_sources/merchant_map.json)
--skip-slack: If toggled to True, will suppress output to Slack. Mainly for debugging.
--tag: For Docker. Unused right now.
--fail-channel: If given, will redirect failures to a different place than the passes
--source: Will specify a specific source to test the data on (e.g. if you want to test Redshift data)

The idea is to have the deploy script run under default settings (or with args) on a cron job until it is integrated into the avant cli

## Automation

This is currently deployed and set to run on the dev etl server. Any updates done to the system should be deployed to there. It observes the following cron schedule:

- Everyday at 00:00 UTC the Picker Test Suite is run (see details on what the Picker Test Suite runs)
- Everyday at 01:00 UTC the regression is run with source specified as Redshift to test that data source (top 5 merchants)
- Everyday at 14:00 UTC the full regression libary is run without any arguments (top 5 merchants)

## Logging

We log the results in the ds_data_vlidation directory at /logs. There are separate logs for each cronjob which are cleared weekly (Sat at midnight)

## Picker Test Suite

The Picker Test Suite is a variation of the regression library intended to return no file outputs, but rather to just indicate if an error occured
or not for a collection of request object.

To run this, pass the argument -ne to the deploy.py wrapper script.

We test the picker test suite by attempting to run every Performance and AVM report in edw3 (Performance Reports are a good proxy for the sales metrics we view in top accounts/ trend widget. TYhis is a simple pass/fail, so we only check if any failure occurred while fetching it or not, NOT if the data matched edw2. By default, this is also run daily (see above) and defaults passes to data_validation and fails to edw3_data_errors (note than these can be toggled with command line args).

In the future, this will also include more debugging information and will be integrated into the deployment workflow. For now, the fails come with an embedded request object for you to manually test.

## Versioning and Issues

We'll release major and minor version releases to maintain this and keep it working as expected as updates come through our system. The code is, admittedly, set up for a quick release, but since we're using this for data control, some maintenance will be done.

For any bugs or errors found with this, please submit a github issue here and create a card through Jira. You can also flag bugs directly from the ds_validation channel in Avantlink Slack.
