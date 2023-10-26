import copy
import os
import json
import sys

from pprint import pprint
import pandas as pd

from regression_dashboard_upload import UpdateDashboardLog

true = True
false = False
null = None


class PrettyTableMaker:
    tables_list = []
    summary_tables = []
    sim_name = None
    category_literal = {
        "trending_widget": {
            "Sales": {
                "Sales": {},
                "ROAS %": {},
                "ROAS": {},
                "Orders": {},
                "Gross Sales": {},
                "Conversion Rate": {},
                "Average Order Amount": {}
            },
            "Combined Commission": {
                "Total Cost": {},
                "Sale Commission": {},
                "Paid Placement": {},
                "Incentive Commission": {},
                "CPC": {},
                "Bonus": {}
            },
            "Network Commission": {
                "Network Bonus": {},
                "Network CPC": {},
                "Network Paid Placement": {},
                "Network Sale Commission": {},
                "Network Total Commission Average Rate": {},
                "Network Total Earnings": {},
                "Network Total Earnings Average Rate": {}
            },
            "Clicks % Impressions": {
                "Click Through Rate": {},
                "Clicks": {},
                "Impressions": {}
            },
            "Adjustments": {
                "Adjusted Affiliate Earnings": {},
                "Adjusted Sales": {},
                "Adjustments": {},
                "Reversal Rate": {}
            },
            "Affiliate Commission": {
                "Affiliate Bonus": {},
                "Affiliate CPC": {},
                "Affiliate Incentive Commission": {},
                "Affiliate Paid Placement": {},
                "Affiliate Sale Commission": {},
                "Affiliate Total Commission Average Rate": {},
                "Affiliate Total Earnings": {},
                "Affiliate Total Earnings Average Rate": {},
                "EPC": {}
            }
        },
        "top_affiliates_widget": {
            "Sales": {
                "Average Order Amount": {},
                "Sales": {},
                "ROAS %": {},
                "ROAS": {},
                "Orders": {},
                "Gross Sales": {},
                "Conversion Rate": {}
            },
            "Combined Commission": {
                "Total Cost": {},
                "Sale Commission": {},
                "Paid Placement": {},
                "Incentive Commission": {},
                "CPC": {},
                "Bonus": {}
            },
            "Affiliate Commission": {
                "Affiliate Bonus": {},
                "Affiliate CPC": {},
                "Affiliate Incentive Commission": {},
                "Affiliate Paid Placement": {},
                "Affiliate Sale Commission": {},
                "Affiliate Total Commission Average Rate": {},
                "Affiliate Total Earnings": {},
                "Affiliate Total Earnings Average Rate": {},
                "EPC": {}
            },
            "Network Commission": {
                "Network CPC": {},
                "Network Paid Placement": {},
                "Network Bonus": {},
                "Network Sale Commission": {},
                "Network Total Commission Average Rate": {},
                "Network Total Earnings": {},
                "Network Total Earnings Average Rate": {}
            },
            "Clicks % Impressions": {
                "Click Through Rate": {},
                "Clicks": {},
                "Impressions": {}
            },
            "Adjustments": {
                "Adjusted Affiliate Earnings": {},
                "Adjusted Cost": {},
                "Adjusted Network Earnings": {},
                "Adjusted Sales": {},
                "Adjustments": {},
                "Reversal Rate": {}
            }
        }
    }
    report_index_map = {
        "trending_widget": {
            "Sales": {
                "Sales": 3,
                "ROAS %": 4,
                "ROAS": 5,
                "Orders": 6,
                "Gross Sales": 7,
                "Conversion Rate": 8,
                "Average Order Amount": 9
            },
            "Combined Commission": {
                "Total Cost": 11,
                "Sale Commission": 12,
                "Paid Placement": 13,
                "Incentive Commission": 14,
                "CPC": 15,
                "Bonus": 16
            },
            "Network Commission": {
                "Network Bonus": 18,
                "Network CPC": 19,
                "Network Paid Placement": 20,
                "Network Sale Commission": 21,
                "Network Total Commission Average Rate": 22,
                "Network Total Earnings": 23,
                "Network Total Earnings Average Rate": 24
            },
            "Clicks % Impressions": {
                "Click Through Rate": 26,
                "Clicks": 27,
                "Impressions": 28
            },
            "Adjustments": {
                "Adjusted Affiliate Earnings": 30,
                "Adjusted Sales": 31,
                "Adjustments": 32,
                "Reversal Rate": 33,
                "Adjusted Cost": 34,
                "Adjusted Network Earnings": 35
            },
            "Affiliate Commission": {
                "Affiliate Bonus": 37,
                "Affiliate CPC": 38,
                "Affiliate Incentive Commission": 39,
                "Affiliate Paid Placement": 40,
                "Affiliate Sale Commission": 41,
                "Affiliate Total Commission Average Rate": 42,
                "Affiliate Total Earnings Average Rate": 43,
                "Affiliate Total Earnings": 44,
                "EPC": 45
            }
        },
        "top_affiliates_widget": {
            "Sales": {
                "Sales": 3,
                "ROAS %": 4,
                "ROAS": 5,
                "Orders": 6,
                "Gross Sales": 7,
                "Conversion Rate": 8,
                "Average Order Amount": 9
            },
            "Combined Commission": {
                "Total Cost": 11,
                "Sale Commission": 12,
                "Paid Placement": 13,
                "Incentive Commission": 14,
                "CPC": 15,
                "Bonus": 16
            },
            "Network Commission": {
                "Network Bonus": 18,
                "Network CPC": 19,
                "Network Paid Placement": 20,
                "Network Sale Commission": 21,
                "Network Total Commission Average Rate": 22,
                "Network Total Earnings": 23,
                "Network Total Earnings Average Rate": 24
            },
            "Clicks % Impressions": {
                "Click Through Rate": 26,
                "Clicks": 27,
                "Impressions": 28
            },
            "Adjustments": {
                "Adjusted Affiliate Earnings": 30,
                "Adjusted Sales": 31,
                "Adjustments": 32,
                "Reversal Rate": 33,
                "Adjusted Cost": 34,
                "Adjusted Network Earnings": 35
            },
            "Affiliate Commission": {
                "Affiliate Bonus": 37,
                "Affiliate CPC": 38,
                "Affiliate Incentive Commission": 39,
                "Affiliate Paid Placement": 40,
                "Affiliate Sale Commission": 41,
                "Affiliate Total Commission Average Rate": 42,
                "Affiliate Total Earnings Average Rate": 43,
                "Affiliate Total Earnings": 44,
                "EPC": 45
            }
        }
    }
    reversed_report_index_map = {
        'top_affiliates_widget': {},
        'trending_widget': {}
    }
    start_date = None
    end_date = None
    date_range = []
    categorical_report = {
        'top_affiliates_widget': {
            'Adjustments': {'Adjusted Affiliate Earnings': '',
                            'Adjusted Cost': '',
                            'Adjusted Network Earnings': '',
                            'Reversal Rate': ''},
            'Affiliate Commission': {'Affiliate Bonus': '',
                                     'Affiliate CPC': '',
                                     'Affiliate Incentive Commission': '',
                                     'Affiliate Paid Placement': '',
                                     'Affiliate Sale Commission': '',
                                     'Affiliate Total Commission Average Rate': '',
                                     'Affiliate Total Earnings': '',
                                     'Affiliate Total Earnings Average Rate': '',
                                     'EPC': ''},
            'Clicks % Impressions': {'Click Through Rate': '',
                                     'Clicks': '',
                                     'Impressions': ''},
            'Combined Commission': {'Bonus': '',
                                    'CPC': '',
                                    'Incentive Commission': '',
                                    'Paid Placement': '',
                                    'Sale Commission': '',
                                    'Total Cost': ''},
            'Network Commission': {'Network Bonus': '',
                                   'Network CPC': '',
                                   'Network Paid Placement': '',
                                   'Network Sale Commission': '',
                                   'Network Total Commission Average Rate': '',
                                   'Network Total Earnings': '',
                                   'Network Total Earnings Average Rate': ''},
            'Sales': {'Average Order Amount': '',
                      'Conversion Rate': '',
                      'Gross Sales': '',
                      'Orders': '',
                      'ROAS': '',
                      'ROAS %': '',
                      'Sales': ''}},
        'trending_widget': {'Adjustments': {'Adjusted Affiliate Earnings': '',
                                            'Adjusted Sales': '',
                                            'Adjustments': '',
                                            'Reversal Rate': ''},
                            'Affiliate Commission': {'Affiliate Bonus': '',
                                                     'Affiliate CPC': '',
                                                     'Affiliate Incentive Commission': '',
                                                     'Affiliate Sale Commission': '',
                                                     'Affiliate Total Commission Average Rate': '',
                                                     'Affiliate Total Earnings': '',
                                                     'Affiliate Total Earnings Average Rate': '',
                                                     'EPC': ''},
                            'Clicks % Impressions': {'Click Through Rate': '',
                                                     'Clicks': '',
                                                     'Impressions': ''},
                            'Combined Commission': {'Bonus': '',
                                                    'CPC': '',
                                                    'Incentive Commission': '',
                                                    'Paid Placement': '',
                                                    'Sale Commission': '',
                                                    'Total Cost': ''},
                            'Network Commission': {'Network Bonus': '',
                                                   'Network CPC': '',
                                                   'Network Paid Placement': '',
                                                   'Network Sale Commission': '',
                                                   'Network Total Commission Average Rate': '',
                                                   'Network Total Earnings': '',
                                                   'Network Total Earnings Average Rate': ''},
                            'Sales': {'Average Order Amount': '',
                                      'Conversion Rate': '',
                                      'Gross Sales': '',
                                      'ROAS': '',
                                      'ROAS %': '',
                                      'Sales': ''}}}
    merchant_summary = {
        "Last Test": None,
        "Merchant": None,
        "Currency": None,
        "Network": None,
        "Sales": None,
        "Combined Commission": None,
        "Network Commission": None,
        "Clicks & Impressions": None,
        "Adjustments": None,
        "Affiliate Commission": None
    }
    merchant_summary_from_deploy = {}
    linked_categorical_report = {}
    dir_path = None

    def __init__(self, merchant_summary_from_deploy, dir_path=None):
        self.merchant_summary_from_deploy = merchant_summary_from_deploy
        for merchant_name in merchant_summary_from_deploy:
            for val in merchant_summary_from_deploy[merchant_name]:
                self.dir_path = "/".join(val["file"].split("/")[-6:])
        if dir_path:
            self.dir_path = dir_path

    def build_reverse_index_map(self):
        result = {}
        for widget in self.report_index_map:
            result[widget] = {}
            for category in self.report_index_map[widget]:
                for report_name in self.report_index_map[widget][category]:
                    result[widget][self.report_index_map[widget][category][report_name]] = {category: report_name}
        self.reversed_report_index_map = result
        return result

    def run(self):
        self.build_internal_tables()
        self.generate_merchant_summary_update_literal()
        self.build_reverse_index_map()
        self.generate_categorical_reports()
        self.build_slack_link_map()
        return UpdateDashboardLog(self.merchant_summary, self.categorical_report, self.linked_categorical_report,
                                  self.reversed_report_index_map, self.sim_name, self.merchant_summary_from_deploy)

    def build_slack_link_map(self):
        subject = {}
        result = {}
        if self.merchant_summary_from_deploy:
            subject = copy.deepcopy(self.merchant_summary_from_deploy)

        for merchant_name in subject:
            for report_literal in subject[merchant_name]:
                if report_literal["widget"] not in result:
                    result[report_literal["widget"]] = {}
                if report_literal["category"] not in result[report_literal["widget"]]:
                    result[report_literal["widget"]][report_literal["category"]] = {}
                if report_literal['report_name'] not in result[report_literal["widget"]][report_literal["category"]]:
                    result[report_literal["widget"]][report_literal["category"]][report_literal['report_name']] = \
                        {"slack_link": report_literal['link']}

        for widget in copy.deepcopy(self.merchant_summary):
            if widget not in result:
                result[widget] = {}
            if "widget" in widget:
                for category in self.merchant_summary[widget]:
                    if category not in result[widget]:
                        result[widget][category] = {}
                    for report_name in self.merchant_summary[widget][category]:
                        if report_name in result[widget][category]:
                            result[widget][category][report_name] = {
                                "result": self.merchant_summary[widget][category][report_name],
                                "slack_link": result[widget][category][report_name]["slack_link"]
                            }
                        else:
                            result[widget][category][report_name] = {
                                "result": self.merchant_summary[widget][category][report_name],
                                "slack_link": None
                            }
        self.linked_categorical_report = result
        # pprint(result)

    def build_internal_tables(self):
        try:
            # Dev Mode
            timestamp = self.dir_path.split('/')[2]
            parent_directory = f'DataValidation/validation_outputs/xlsx/{timestamp}'
            sim_dir = os.listdir(parent_directory)
        except:
            # Prod mode
            try:
                timestamp = self.dir_path.split('/')[0]
                parent_directory = f'DataValidation/validation_outputs/xlsx/{timestamp}'
                sim_dir = os.listdir(parent_directory)
            except:
                # Something wrong with the file tree given
                timestamp = os.listdir('DataValidation/validation_outputs/xlsx')[0]
                parent_directory = f'DataValidation/validation_outputs/xlsx/{timestamp}'
                sim_dir = os.listdir(parent_directory)

        self.sim_name = sim_dir[0]
        sim_path = os.path.join(parent_directory, sim_dir[0])
        source_name = os.listdir(sim_path)[0]
        source_path = os.path.join(sim_path, source_name)

        source_path_files = os.listdir(source_path)
        for widget in source_path_files:
            if os.path.isdir(os.path.join(source_path, widget)):
                widget_path = os.path.join(source_path, widget)
                for category in os.listdir(widget_path):
                    category_path = os.path.join(widget_path, category)
                    for filename in os.listdir(category_path):
                        filepath = os.path.join(category_path, filename)
                        new_df = pd.read_excel(filepath)
                        self.tables_list.append(new_df)
                        if self.start_date is None:
                            self.start_date = new_df["Day"].values[0]
                        if self.end_date is None:
                            self.end_date = new_df["Day"].values[-1]
                        if self.start_date is not None and self.end_date is not None:
                            self.date_range = f"{self.start_date} - {self.end_date}"
            else:
                summary_name = os.path.join(source_path, widget)
                self.summary_tables.append(pd.read_excel(summary_name))


    def generate_merchant_summary_update_literal(self):
        """
         create the object used to update merchant summary. This overview shows a compressed view of
         each merchant being tested listing the following;
         -1 merchant per row,
         -each category of tests run, if fails are present - the names of the failed reports will be listed in the cell

        Returns:
            None  - Side effect = set self.merchant_result_overview (see class definition self.merchant_result_overview)
        """

        result = {}
        if len(self.summary_tables) > 1:
            for summary in self.summary_tables:
                for index, row in summary.iterrows():
                    widget_name = row["widget"]
                    category_name = row["Dashboard Category"]
                    # Check if the widget is in the result already, if not - create entry
                    if widget_name not in result:
                        result[widget_name] = {}
                    # Check if the category is in the widget result already, if not - create entry
                    if category_name not in result[widget_name]:
                        result[widget_name][category_name] = {}
            for summary in self.summary_tables:
                for index, row in summary.iterrows():
                    widget_name = row["widget"]
                    category_name = row["Dashboard Category"]
                    if row["Dashboard Report Name"] not in result[widget_name][category_name]:
                        result[widget_name][category_name][row["Dashboard Report Name"]] = row['pass/fail']
        result["Last Test"] = self.convert_run_time()
        result["Merchant"] = self.get_merchant()
        result["Currency"] = self.get_currency()
        result["SQL_source"] = self.get_sql_source()
        result["Date Range"] = self.date_range
        result["Network"] = None
        self.merchant_summary = result

    def generate_categorical_reports(self):
        overview = copy.deepcopy(self.merchant_summary)
        result = {
            "top_affiliates_widget": [],
            "trending_widget": []
        }
        for widget_key in overview:
            if "widget" in widget_key:
                for cell in range(list(self.reversed_report_index_map[widget_key].keys()).pop() + 1):
                    if cell not in self.reversed_report_index_map[widget_key]:
                        result[widget_key].append([])
                    else:
                        category_literal = self.reversed_report_index_map[widget_key][cell]
                        category = list(category_literal.keys()).pop()
                        report_name = category_literal[category]
                        try:
                            result[widget_key].append(
                                [
                                    f"{[self.merchant_summary[widget_key][category][report_name]].pop()}"]
                            )
                        except KeyError:
                            result[widget_key].append([f"N/A"])

        # Add in Run time, Data Source, And Merchant outputs to Categorical Report Values
        for widget_key in result:
            try:
                # Set the source- redefining if necessary to ensure the source is compatible with the widget
                # An example of this use case is when Top Affiliates Widget is specified and cube_postgres is the source
                # In that case, we need to redefine it to cube_olap
                _source = self.get_sql_source()
                if widget_key == 'trending_widget' and _source == 'cube_olap':
                    _source = 'cube_postgres'
                elif widget_key == 'top_affiliates_widget' and _source == 'cube_postgres':
                    _source = 'cube_olap'

                result[widget_key].pop(0)
                result[widget_key].insert(0, [self.convert_run_time()])
                result[widget_key].pop(1)
                result[widget_key].insert(1, [_source])
                result[widget_key].insert(3, [self.get_merchant()])
            except IndexError:
                continue # Empty directory go to next one
        self.categorical_report = result

    def simplify_merchant_summary(self):
        for widget_name in self.merchant_summary:
            for category_name in self.merchant_summary[widget_name]:
                if "Fail" in str(self.merchant_summary[widget_name][category_name]):
                    self.merchant_summary[widget_name][category_name] = "FAIL!"
                else:
                    self.merchant_summary[widget_name][category_name] = "PASS!"

    def get_sql_source(self):
        """
        Returns:
            string - data source used for the comparison
        """
        for key in self.merchant_summary_from_deploy.keys():
            return self.merchant_summary_from_deploy[key][0]['data_source']

    def get_currency(self):
        """
        Returns:
            string - Currency listed in the request Object for the comparison
        """
        for report in self.tables_list[0]["edw3_request_object"]:
            ro = json.loads(report)
            for ro_key in ro:
                for key in ro[ro_key]:
                    if key == "currency":
                        return ro[ro_key][key]

    def get_merchant(self):
        """
        Returns:
           string - Merchant listed for the comparison
        """
        return list(self.merchant_summary_from_deploy.keys())[0].replace('_', ' ')

    def convert_run_time(self):
        ugly_runtime = self.dir_path.split("/")[0]
        # Catch for dev mode
        if ':' not in ugly_runtime:
            ugly_runtime = self.dir_path.split("/")[-4] 
        clean_runtime = ugly_runtime.split("_").pop()
        clean_date = "/".join(ugly_runtime.split("_")[:-1])
        return f"{clean_date} @ {clean_runtime}\n{self.date_range}"

    @staticmethod
    def clean_input_category_names(deploy_output):
        for merchant_name in deploy_output:
            for literal in deploy_output[merchant_name]:
                clean_category = literal['category'].replace("_", " ")
                literal.update({'category': clean_category})
        return deploy_output
