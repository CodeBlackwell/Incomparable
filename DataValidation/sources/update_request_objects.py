from __future__ import print_function

import os.path
import json
import sys

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

#Retrieve values from Google Spreadsheets
def get_values(spreadsheet_id, range_name):
    """
    Creates the batch_update the user has access to.
    Load pre-authorized user credentials from the environment.
    TODO(developer) - See https://developers.google.com/identity
    for guides on implementing OAuth2 for the application.
        """
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('DataValidation/token.json'):
        creds = Credentials.from_authorized_user_file('DataValidation/token.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            print(os.getcwd())
            flow = InstalledAppFlow.from_client_secrets_file(
                '/home/ubuntu/ds-data_validation/DataValidation/credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('DataValidation/token.json', 'w') as token:
            token.write(creds.to_json())    # pylint: disable=maybe-no-member
    try:
        service = build('sheets', 'v4', credentials=creds)

        result = service.spreadsheets().values().get(
            spreadsheetId=spreadsheet_id, range=range_name).execute()
        rows = result.get('values', [])
        print(f"{len(rows)} rows retrieved")
        return result
    except HttpError as error:
        print(f"An error occurred: {error}")
        return error

# Needed to convert python literal strings into parsable JSON
def fix_json(broken_json):
    return broken_json.replace("'", '"').replace("True", "true").replace("False", "false").replace("None", "null")

#Process the Gspread return value into a list of unique request object (One for each Report Name)
def process_rows(rows):
    cache = []
    request_objects = {}
    for row in rows['values']:
        cache.append({
            'Report/Graph': row[0],
            'Version': row[1],
            'Date': row[2],
            'Query': row[3]
        })
    for item in cache:
        if item["Version"] == "EDW3":
            request_objects[item["Report/Graph"]] = item["Query"]
    return request_objects

if __name__ == '__main__':
    rows = get_values("1sA8anBPSorLyLiYwf0oTOZ7FSRkvE9nDK16Wm83Cc-Y", "A1:ZZZ")
    request_objects = process_rows(rows)
    print(request_objects.keys())
    for key, request_object in request_objects.items():
        fname = key.replace(' ', '_') #replace spaces with _
        with open(f"DataValidation/sources/json_sources/no_error_validation/{fname}.json", "w+") as f:
            f.write(fix_json(request_objects[key]))
