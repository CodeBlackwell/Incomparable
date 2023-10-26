from __future__ import print_function

import copy
import os.path
from pprint import pprint
import json

import sys
from pprint import pprint
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
VALUE_INPUT_OPTION = "USER_ENTERED"


class UpdateDashboardLog:
    service = None
    categorical_report = None
    merchant_summary = None
    sheet = None
    merchant_name = None
    merchant_summary_report_values = {
        "ta": [],
        "tw": []
    }
    avantlog_spreadsheet_ids = {
        "top_affiliates_widget": {
            "fact_postgres": "1jvLwUWylyoU4moSJSuVZ8Nq1IkIqGnRtGa0OHWAgmcQ",
            "fact_redshift": "16AGoYobiSKieJpTl9bwl1bo6l58QNqxM5Iwiq5AJ24U",
            "cube_olap": "15G0xYyQNdhDcqFvBqq3S1M3cFAaJHx8SwZyDtBLG_h8"
        },
        "trending_widget": {
            "fact_postgres": "1ZXk4QlTjDE3mkH6SOKqFMouAdHMEDf7xbRXALPQkLAs",
            "fact_redshift": "12K1sdP8ezk1e8OkvPFoSgiDhdqD0uYIHSJBRMB6LEmU",
            "cube_postgres": "1knT1Q0qKsucl1YEjzT8e7iNsVWouhXp5oJ4zS9RWfbE",
        },
        "all_sources": "1ANxSTK3-QdFyTnt8PAknVpFQZXwNdYombcyw87gx7rk",
        "historic_logs": "1JKJ_hQA4xzOxPHEd1xqgAPYk9vfmgpxeGXf21sBkWYw"
    }
    merchant_summary_RANGE = {
        "part_1": {
            "REI.com": "Merchant Summary!C2:C3",
            "black diamond equipment": "Merchant Summary!B2:B3",
            "Carousel Checks": "Merchant Summary!D2:D3",
            "Palmetto State Armory": "Merchant Summary!E2:E3",
            "RTIC Outdoors": "Merchant Summary!F2:F3",
            "A Life Plus": "Merchant Summary!G2:G3"
        },
        "part_2": {
            "REI.com": "Merchant Summary!C5:C12",
            "black diamond equipment": "Merchant Summary!B5:B12",
            "Carousel Checks": "Merchant Summary!D5:D12",
            "Palmetto State Armory": "Merchant Summary!E5:E12",
            "RTIC Outdoors": "Merchant Summary!F5:F12",
            "A Life Plus": "Merchant Summary!G5:G12"
        }
    }
    categorical_report_RANGE = {
        "all_sources": {
            "trending_widget": "Trending Widget Categorical Report Log!E1:E50",
            "top_affiliates_widget": "Top Affiliates Widget Categorical Report Log!E1:E50"
        },
        "REI.com": "REI.com!E1:E50",
        "black diamond equipment": "Black Diamond Equipment!E1:E50",
        "Carousel Checks": "Carousel Checks!E1:E50",
        "RTIC Outdoors": "RTIC Outdoors!E1:E50",
        "Palmetto State Armory": "Palmetto State Armory!E1:E50",
        "A Life Plus": "A Life Plus!E1:E50"
    }
    linked_categorical_report = {}
    categorical_report_spreadsheet_ids = {
        "trending_widget": {
            "cube_postgres": {
                "RTIC Outdoors": 483196132,
                "REI.com": 1654910639,
                "black diamond equipment": 50980162,
                "Carousel Checks": 2116400324,
                "Palmetto State Armory": 583081350,
                "A Life Plus": 893464757
            },
            "fact_postgres": {
                "REI.com": 1674335050,
                "black diamond equipment": 713675991,
                "Carousel Checks": 1977279573,
                "Palmetto State Armory": 593436964,
                "RTIC Outdoors": 1974675983,
                "A Life Plus": 564407217
            },
            "fact_redshift": {
                "REI.com": 1091042768,
                "black diamond equipment": 1028869454,
                "Carousel Checks": 1683149162,
                "Palmetto State Armory": 549061267,
                "RTIC Outdoors": 523928566,
                "A Life Plus": 895709852
            },
            "all_sources": 1567122299
        },
        "top_affiliates_widget": {
            "cube_olap": {
                "REI.com": 564315687,
                "black diamond equipment": 1931016559,
                "Carousel Checks": 969222130,
                "Palmetto State Armory": 653692908,
                "RTIC Outdoors": 130979600,
                "A Life Plus": 886186822
            },
            "fact_postgres": {
                "REI.com": 687597798,
                "black diamond equipment": 657468600,
                "Carousel Checks": 1960841405,
                "Palmetto State Armory": 998588654,
                "RTIC Outdoors": 52608501,
                "A Life Plus": 1693042867
            },
            "fact_redshift": {
                "REI.com": 1114619640,
                "black diamond equipment": 1032630095,
                "Carousel Checks": 1039748189,
                "Palmetto State Armory": 1858213088,
                "RTIC Outdoors": 1260101347,
                "A Life Plus": 437151484
            },
            "all_sources": 1278908903
        }
    }
    all_sources_merchant_summary_RANGE = {
        "part_1": {
            "trending_widget": {
                "cube_postgres": {
                    "black diamond equipment": "Merchant Summary!B2:B3",
                    "REI.com": "Merchant Summary!C2:C3",
                    "Carousel Checks": "Merchant Summary!D2:D3",
                    "Palmetto State Armory": "Merchant Summary!E2:E3",
                    "RTIC Outdoors": "Merchant Summary!F2:F3",
                    "A Life Plus": "Merchant Summary!G2:G3"
                },
                "fact_postgres": {
                    "black diamond equipment": "Merchant Summary!B15:B16",
                    "REI.com": "Merchant Summary!C15:C16",
                    "Carousel Checks": "Merchant Summary!D15:D16",
                    "Palmetto State Armory": "Merchant Summary!E15:E16",
                    "RTIC Outdoors": "Merchant Summary!F15:F16",
                    "A Life Plus": "Merchant Summary!G15:G16"
                },
                "fact_redshift": {
                    "black diamond equipment": "Merchant Summary!B28:B29",
                    "REI.com": "Merchant Summary!C28:C29",
                    "Carousel Checks": "Merchant Summary!D28:D29",
                    "Palmetto State Armory": "Merchant Summary!E28:E29",
                    "RTIC Outdoors": "Merchant Summary!F28:F29",
                    "A Life Plus": "Merchant Summary!G28:G29"
                }
            },
            "top_affiliates_widget": {
                "cube_olap": {
                    "black diamond equipment": "Merchant Summary!I2:I3",
                    "REI.com": "Merchant Summary!J2:J3",
                    "Carousel Checks": "Merchant Summary!K2:K3",
                    "Palmetto State Armory": "Merchant Summary!L2:L3",
                    "RTIC Outdoors": "Merchant Summary!M2:M3",
                    "A Life Plus": "Merchant Summary!N2:N3"
                },
                "fact_postgres": {
                    "black diamond equipment": "Merchant Summary!I15:I16",
                    "REI.com": "Merchant Summary!J15:J16",
                    "Carousel Checks": "Merchant Summary!K15:K16",
                    "Palmetto State Armory": "Merchant Summary!L15:L16",
                    "RTIC Outdoors": "Merchant Summary!M15:M16",
                    "A Life Plus": "Merchant Summary!N15:N16"
                },
                "fact_redshift": {
                    "black diamond equipment": "Merchant Summary!I28:I29",
                    "REI.com": "Merchant Summary!J28:J29",
                    "Carousel Checks": "Merchant Summary!K28:K29",
                    "Palmetto State Armory": "Merchant Summary!L28:L29",
                    "RTIC Outdoors": "Merchant Summary!M28:M29",
                    "A Life Plus": "Merchant Summary!N28:N29"
                }
            }
        },
        "part_2": {
            "trending_widget": {
                "cube_postgres": {
                    "black diamond equipment": "Merchant Summary!B5:B12",
                    "REI.com": "Merchant Summary!C5:C12",
                    "Carousel Checks": "Merchant Summary!D5:D12",
                    "Palmetto State Armory": "Merchant Summary!E5:E12",
                    "RTIC Outdoors": "Merchant Summary!F5:F12",
                    "A Life Plus": "Merchant Summary!G5:G12"
                },
                "fact_postgres": {
                    "black diamond equipment": "Merchant Summary!B18:B25",
                    "REI.com": "Merchant Summary!C18:C25",
                    "Carousel Checks": "Merchant Summary!D18:D25",
                    "Palmetto State Armory": "Merchant Summary!E18:E25",
                    "RTIC Outdoors": "Merchant Summary!F18:F25",
                    "A Life Plus": "Merchant Summary!G18:G25"
                },
                "fact_redshift": {
                    "black diamond equipment": "Merchant Summary!B31:B38",
                    "REI.com": "Merchant Summary!C31:C38",
                    "Carousel Checks": "Merchant Summary!D31:D38",
                    "Palmetto State Armory": "Merchant Summary!E31:E38",
                    "RTIC Outdoors": "Merchant Summary!F31:F38",
                    "A Life Plus": "Merchant Summary!G31:G38"
                }
            },
            "top_affiliates_widget": {
                "cube_olap": {
                    "black diamond equipment": "Merchant Summary!I5:I12",
                    "REI.com": "Merchant Summary!J5:J12",
                    "Carousel Checks": "Merchant Summary!K5:K12",
                    "Palmetto State Armory": "Merchant Summary!L5:L12",
                    "RTIC Outdoors": "Merchant Summary!M5:M12",
                    "A Life Plus": "Merchant Summary!N5:N12"
                },
                "fact_postgres": {
                    "black diamond equipment": "Merchant Summary!I18:I25",
                    "REI.com": "Merchant Summary!J18:J25",
                    "Carousel Checks": "Merchant Summary!K18:K25",
                    "Palmetto State Armory": "Merchant Summary!L18:L25",
                    "RTIC Outdoors": "Merchant Summary!M18:M25",
                    "A Life Plus": "Merchant Summary!N18:N25"
                },
                "fact_redshift": {
                    "black diamond equipment": "Merchant Summary!I31:I38",
                    "REI.com": "Merchant Summary!J31:J38",
                    "Carousel Checks": "Merchant Summary!K31:K38",
                    "Palmetto State Armory": "Merchant Summary!L31:L38",
                    "RTIC Outdoors": "Merchant Summary!M31:M38",
                    "A Life Plus": "Merchant Summary!N31:N38"
                }
            }
        },
    }
    slack_links = {
        "top_affiliates_widget": [],
        "trending_widget": [],
        "all_sources": {
            "top_affiliates_widget": [],
            "trending_widget": []
        }
    }
    categorical_report_slack_title_format_map = {
        "top_affiliates_widget": {},
        "trending_widget": {}
    }

    sim_name = ""

    def __init__(self, merchant_summary, categorical_report, linked_categorical_report,
                 reversed_report_index_map, sim_name, merchant_summary_from_deploy):
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
                flow = InstalledAppFlow.from_client_secrets_file(
                    'DataValidation/credentials.json', SCOPES)
                creds = flow.run_local_server(port=0)
            # Save the credentials for the next run
            with open('DataValidation/token.json', 'w') as token:
                token.write(creds.to_json())
        # Call the Sheets API
        service = build('sheets', 'v4', credentials=creds)
        self.sim_name = sim_name
        self.service = service
        self.sheet = service.spreadsheets().values()
        self.linked_categorical_report = linked_categorical_report
        self.categorical_report_values = categorical_report  # must be an Array of Arrays -[ [ each, col, value, per, cell ], [], [], [] ]
        self.reversed_report_index_map = reversed_report_index_map
        self.merchant_summary = merchant_summary
        self.sql_source = merchant_summary["SQL_source"]
        self.merchant_name = self.merchant_summary["Merchant"]
        self.merchant_summary_from_deploy = merchant_summary_from_deploy

        self.run()

    def run(self):
        self.process_merchant_summary_report_for_google()
        self.simplify_merchant_summary()
        self.update_merchant_summaries()
        self.update_categorical_reports()
        self.insert_slack_hyperlinks("top_affiliates_widget", all_sources=True)
        self.insert_slack_hyperlinks("top_affiliates_widget", all_sources=False)
        self.insert_slack_hyperlinks("trending_widget", all_sources=True)
        self.insert_slack_hyperlinks("trending_widget", all_sources=False)

    def insert_blank_categorical_report_column(self, widget, all_sources=False):
        # Kinda hacky here, but ensure trending_widget uses cube_postgres and not olap
        if widget == 'trending_widget' and self.sql_source == 'cube_olap':
            _source = 'cube_postgres'
        elif widget == 'top_affiliates_widget' and self.sql_source == 'cube_postgres':
            _source = 'cube_olap'
        else:
            _source = self.sql_source

        if not all_sources:
            avantlog_spreadsheet_id = self.avantlog_spreadsheet_ids[widget][_source]
            categorical_report_tab_id = self.categorical_report_spreadsheet_ids[widget][_source][
                self.merchant_name]
        if all_sources:
            avantlog_spreadsheet_id = self.avantlog_spreadsheet_ids["all_sources"]
            categorical_report_tab_id = self.categorical_report_spreadsheet_ids[widget]["all_sources"]

        body = {
            "requests": [
                {"insertDimension": {
                    "range": {"sheetId": categorical_report_tab_id, "dimension": "COLUMNS", "startIndex": 4,
                              "endIndex": 5}, "inheritFromBefore": False}}
            ]
        }
        result = self.service.spreadsheets().batchUpdate(spreadsheetId=avantlog_spreadsheet_id, body=body).execute()

    def update_all_sources_categorical_report(self):
        categorical_report_body = {'values': self.categorical_report_values["trending_widget"]}
        self.insert_blank_categorical_report_column("trending_widget", all_sources=True)

        # upload Categorical Report for each Widget - All Sources - Trending Widget
        try:
            categorical_report_request = self.sheet.update(
                spreadsheetId=self.avantlog_spreadsheet_ids["all_sources"],
                range=self.categorical_report_RANGE["all_sources"]["trending_widget"],
                valueInputOption=VALUE_INPUT_OPTION,
                body=categorical_report_body
            )
            result = categorical_report_request.execute()
            print(result, 'Trending Widget - All Sources - Categorical Report')
        except HttpError as err:
            print(err, 'Trending Widget - All Sources - Categorical Report')
        # self.insert_slack_hyperlinks("trending_widget", all_sources=True)

        # upload Categorical Report for each Widget - All Sources - Top Affiliates
        categorical_report_body = {'values': self.categorical_report_values["top_affiliates_widget"]}
        self.insert_blank_categorical_report_column("top_affiliates_widget", all_sources=True)

        try:
            categorical_report_request = self.sheet.update(
                spreadsheetId=self.avantlog_spreadsheet_ids["all_sources"],
                range=self.categorical_report_RANGE["all_sources"]["top_affiliates_widget"],
                valueInputOption=VALUE_INPUT_OPTION,
                body=categorical_report_body
            )
            result = categorical_report_request.execute()
            print(result, 'Top Affiliates Widget - All Sources - Categorical Report')
        except HttpError as err:
            print(err, 'Top Affiliates Widget - All Sources - Categorical Report')

        # self.insert_slack_hyperlinks("top_affiliates_widget", all_sources=True)

    def update_all_sources_merchant_summary(self):
        tw_merchant_summary_body_part_1 = {'values': self.merchant_summary_report_values["trending_widget"][:2]}
        tw_merchant_summary_body_part_2 = {'values': self.merchant_summary_report_values["trending_widget"][3:]}

        # Kinda hacky here, but ensure trending_widget uses cube_postgres and not olap
        if self.sql_source == 'cube_olap':
            _source = 'cube_postgres'
            _source_affiliate = self.sql_source
        elif self.sql_source == 'cube_postgres':
            _source = self.sql_source
            _source_affiliate = 'cube_olap'
        else:
            _source = self.sql_source
            _source_affiliate = self.sql_source

        try:
            # upload - Merchant Summary Report - Part 1
            merchant_account_overview_part_1 = self.sheet.update(
                spreadsheetId=self.avantlog_spreadsheet_ids["all_sources"],
                range=self.all_sources_merchant_summary_RANGE["part_1"]["trending_widget"][_source][
                    self.merchant_name],
                valueInputOption=VALUE_INPUT_OPTION,
                body=tw_merchant_summary_body_part_1
            ).execute()
            print(merchant_account_overview_part_1, 'Trending Widget - All Sources - Merchant Summary - Part 1')
        except HttpError as err:
            print(err)

        try:
            # upload - Merchant Summary Report - Part 2
            merchant_account_overview_part_2 = self.sheet.update(
                spreadsheetId=self.avantlog_spreadsheet_ids["all_sources"],
                range=self.all_sources_merchant_summary_RANGE["part_2"]["trending_widget"][_source][
                    self.merchant_name],
                valueInputOption=VALUE_INPUT_OPTION,
                body=tw_merchant_summary_body_part_2
            ).execute()
            print(merchant_account_overview_part_2, 'Trending Widget - All Sources - Merchant Summary - Part 2')
        except HttpError as err:
            print(err)
        # Update All Sources Merchant Summary - Top Affiliates widget
        ta_merchant_summary_body_part_1 = {'values': self.merchant_summary_report_values["top_affiliates_widget"][:2]}
        ta_merchant_summary_body_part_2 = {'values': self.merchant_summary_report_values["top_affiliates_widget"][3:]}

        try:
            # upload - Merchant Summary Report - Part 1
            merchant_account_overview_part_1 = self.sheet.update(
                spreadsheetId=self.avantlog_spreadsheet_ids["all_sources"],
                range=self.all_sources_merchant_summary_RANGE["part_1"]["top_affiliates_widget"][_source_affiliate][
                    self.merchant_name],
                valueInputOption=VALUE_INPUT_OPTION,
                body=ta_merchant_summary_body_part_1
            ).execute()
            print(merchant_account_overview_part_1, 'Top Affiliates Widget - All Sources - Merchant Summary - Part 1')
        except HttpError as err:
            print(err)
        try:
            # upload - Merchant Summary Report - Part 2
            merchant_account_overview_part_2 = self.sheet.update(
                spreadsheetId=self.avantlog_spreadsheet_ids["all_sources"],
                range=self.all_sources_merchant_summary_RANGE["part_2"]["top_affiliates_widget"][_source_affiliate][
                    self.merchant_name],
                valueInputOption=VALUE_INPUT_OPTION,
                body=ta_merchant_summary_body_part_2
            ).execute()
            print(merchant_account_overview_part_2, 'Top Affiliates Widget - All Sources - Merchant Summary - Part 2')
        except HttpError as err:
            print(err)

    def update_merchant_summaries(self):
        if self.sim_name == "EDW3_Production":
            self.update_merchant_summary("trending_widget")
            self.update_merchant_summary("top_affiliates_widget")
            self.update_all_sources_merchant_summary()

    def update_categorical_reports(self):
        self.update_merchant_categorical_report("trending_widget")
        self.update_merchant_categorical_report("top_affiliates_widget")
        self.update_all_sources_categorical_report()

    def update_merchant_summary(self, widget):
        merchant_summary_body_part_1 = {'values': self.merchant_summary_report_values[widget][:2]}
        merchant_summary_body_part_2 = {'values': self.merchant_summary_report_values[widget][3:]}

        # Kinda hacky here, but ensure trending_widget uses cube_postgres and not olap
        if widget == 'trending_widget' and self.sql_source == 'cube_olap':
            _source = 'cube_postgres'
        elif widget == 'top_affiliates_widget' and self.sql_source == 'cube_postgres':
            _source = 'cube_olap'
        else:
            _source = self.sql_source

        try:
            # upload - Merchant Summary Report - Part 1
            merchant_account_overview_part_1 = self.sheet.update(
                spreadsheetId=self.avantlog_spreadsheet_ids[widget][_source],
                range=self.merchant_summary_RANGE["part_1"][self.merchant_name],
                valueInputOption=VALUE_INPUT_OPTION,
                body=merchant_summary_body_part_1
            ).execute()
            print(merchant_account_overview_part_1, f'{widget} - Merchant Summary - Part 1')
        except HttpError as err:
            print(err, f'{widget} - Merchant Summary - Part 1')
        try:
            # upload - Merchant Summary Report - Part 2
            merchant_account_overview_part_2 = self.sheet.update(
                spreadsheetId=self.avantlog_spreadsheet_ids[widget][_source],
                range=self.merchant_summary_RANGE["part_2"][self.merchant_name],
                valueInputOption=VALUE_INPUT_OPTION,
                body=merchant_summary_body_part_2
            ).execute()
            print(merchant_account_overview_part_2, f'{widget} - Merchant Summary - Part 2')
        except HttpError as err:
            print(err, f'{widget} - Merchant Summary - Part 2')

    def update_merchant_categorical_report(self, widget=None):
        # Kinda hacky here, but ensure trending_widget uses cube_postgres and not olap
        if widget == 'trending_widget' and self.sql_source == 'cube_olap':
            _source = 'cube_postgres'
        elif widget == 'top_affiliates_widget' and self.sql_source == 'cube_postgres':
            _source = 'cube_olap'
        else:
            _source = self.sql_source

        categorical_report_body = {'values': self.categorical_report_values[widget]}
        self.insert_blank_categorical_report_column(widget)

        # upload Categorical Report for each Widget -- Top Affiliates / Trending widget
        try:
            categorical_report_request = self.sheet.update(
                spreadsheetId=self.avantlog_spreadsheet_ids[widget][_source],
                range=self.categorical_report_RANGE[self.merchant_name],
                valueInputOption=VALUE_INPUT_OPTION,
                body=categorical_report_body
            )
            result = categorical_report_request.execute()
            print(result, f'{widget} - Categorical Report')
        except HttpError as err:
            print(err, f'{widget} - {_source} - Categorical Report')
        # self.insert_slack_hyperlinks(widget)

    def process_merchant_summary_report_for_google(self):
        merchant_summary_values = []
        category_order = ["Sales", "Combined Commission", "Network Commission",
                          "Clicks % Impressions", "Adjustments", "Affiliate Commission"]
        subject = self.merchant_summary
        merchant_summary_values.append([subject["Last Test"]])
        merchant_summary_values.append([subject["Date Range"]])
        merchant_summary_values.append([subject["Merchant"]])
        merchant_summary_values.append([subject["Currency"]])
        merchant_summary_values.append([subject["Network"]])
        ta_result = copy.deepcopy(merchant_summary_values)
        tw_result = copy.deepcopy(merchant_summary_values)
        for category in category_order:
            try:
                ta_result.append([subject["top_affiliates_widget"][category]])
                tw_result.append([subject["trending_widget"][category]])
            except (KeyError, IndexError):
                ta_result.append([{'Default': 'PASS'}])  # If not present here, write as a pass
                tw_result.append([{'Default': 'PASS'}])
        for sublist in ta_result:
            for val in sublist:
                new_val = str(val).replace("{", "").replace("}", "").replace(",", "\n").replace("]", "")
                sublist.pop()
                sublist.append(new_val)
        for sublist in tw_result:
            for val in sublist:
                new_val = str(val).replace("{", "").replace("}", "").replace(",", "\n").replace("]", "")
                sublist.pop()
                sublist.append(new_val)
        self.merchant_summary_report_values["top_affiliates_widget"] = ta_result
        self.merchant_summary_report_values["trending_widget"] = tw_result
        return tw_result, ta_result

    def simplify_merchant_summary(self):
        new_summary_values = copy.deepcopy(self.merchant_summary_report_values)
        for widget_name in new_summary_values:
            for sublist in new_summary_values[widget_name]:
                if "fail" in str(sublist).lower():
                    sublist[0] = "FAIL"
                if "pass" in str(sublist).lower():
                    sublist[0] = "PASS!"
        self.merchant_summary_report_values = new_summary_values
        return new_summary_values

    def insert_slack_hyperlinks(self, widget, all_sources=False):
        self.generate_slack_hyperlinks()

        # Kinda hacky here, but ensure trending_widget uses cube_postgres and not olap
        if widget == 'trending_widget' and self.sql_source == 'cube_olap':
            _source = 'cube_postgres'
        elif widget == 'top_affiliates_widget' and self.sql_source == 'cube_postgres':
            _source = 'cube_olap'
        else:
            _source = self.sql_source

        body = {}
        avantlog_spreadsheet_id = ""
        if not all_sources:
            widget_body = self.slack_links[widget]
            avantlog_spreadsheet_id = self.avantlog_spreadsheet_ids[widget][_source]
            body = {
                "requests": widget_body
            }
        if all_sources:
            all_sources_body = self.slack_links["all_sources"][widget]
            avantlog_spreadsheet_id = self.avantlog_spreadsheet_ids["all_sources"]
            body = {
                "requests": all_sources_body
            }
        if len(body["requests"]):
            try:
                result = self.service.spreadsheets().batchUpdate(spreadsheetId=avantlog_spreadsheet_id,
                                                                 body=body).execute()
            except HttpError as e:
                print(e)
                pprint(body)
                raise

    def generate_slack_hyperlinks(self):
        # Kinda hacky here, but ensure trending_widget uses cube_postgres and not olap
        if self.sql_source == 'cube_olap':
            _source = 'cube_postgres'
        else:
            _source = self.sql_source

        for key in self.merchant_summary_from_deploy:
            overview = copy.deepcopy(self.merchant_summary_from_deploy[key])
        result = {
            "top_affiliates_widget": [],
            "trending_widget": [],
            "all_sources": {
                "top_affiliates_widget": [],
                "trending_widget": []
            }
        }
        for entry in overview:
            if entry["widget"] in ["trending_widget", "top_affiliates_widget", "all_sources"]:
                if entry["widget"] == 'top_affiliates_widget' and self.sql_source == 'cube_postgres':
                    _source = "cube_olap"
                for cell in range(list(self.reversed_report_index_map[entry["widget"]].keys()).pop() + 1):
                    # Skip blank rows
                    if cell not in self.reversed_report_index_map[entry["widget"]].keys():
                        continue
                    else:
                        category_literal = self.reversed_report_index_map[entry["widget"]][cell]
                        category = list(category_literal.keys()).pop().replace('_', ' ')
                        report_name = category_literal[category]

                        # Skip unused categories
                        if category not in list(self.linked_categorical_report[entry["widget"]].keys()):
                            #print(f'Skipping {category} as it is not in categorical report') (potentially useful debug info here)
                            continue                        
                        # Skip non base metrics
                        elif report_name not in list(self.linked_categorical_report[entry["widget"]][category].keys()):
                            #print(f'Skipping {report_name}')
                            continue
                        try:
                            if self.linked_categorical_report[entry["widget"]][category][report_name][
                                "slack_link"] is not None:
                                result[entry["widget"]].append(
                                    self.generate_single_slack_hyperlink_request(
                                        cell,
                                        self.linked_categorical_report[entry["widget"]][category][report_name][
                                            "slack_link"],
                                        self.categorical_report_spreadsheet_ids[entry["widget"]][_source][
                                            self.merchant_name],
                                        self.linked_categorical_report[entry["widget"]][category][report_name][
                                            "result"],
                                        report_name
                                    )
                                )
                                result["all_sources"][entry["widget"]].append(
                                    self.generate_single_slack_hyperlink_request(
                                        cell,
                                        self.linked_categorical_report[entry["widget"]][category][report_name][
                                            "slack_link"],
                                        self.categorical_report_spreadsheet_ids[entry["widget"]]["all_sources"],
                                        self.linked_categorical_report[entry["widget"]][category][report_name][
                                            "result"],
                                        report_name
                                    )
                                )
                        except KeyError as e:
                            continue  # Non base metric
        self.slack_links = result

    @staticmethod
    def generate_single_slack_hyperlink_request(index, slack_message_link,
                                                categorical_spreadsheet_id,
                                                pass_status, report_name):
        alternative_result = {
            "updateCells": {
                "rows": [
                    {
                        "values": [{
                            "userEnteredValue": {
                                "formulaValue": "=HYPERLINK({},{})".format(
                                    f'"{slack_message_link}"',
                                    f'"{pass_status}"')
                            }
                        }]
                    }
                ],
                "fields": "userEnteredValue",
                "start": {
                    "sheetId": categorical_spreadsheet_id,
                    "rowIndex": index + 1,
                    "columnIndex": 4
                }
            }
        }
        # print(alternative_result, report_name)
        return alternative_result
