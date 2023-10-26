import asyncio
import json
import os
import re
from typing import List
import sys
import json
import numpy as np
from args import args

import colorama
import pandas
import pandas as pd
import pprint

colorama.init(autoreset=True)
from sources.knowndiscrepancies import KnownDiscrepancies
from sources.base import SourceBase

curpath = os.getcwd()
if not os.path.exists("validation_csv_outputs"):
    os.makedirs(("validation_csv_outputs"))


# os.path.abspath(os.curdir)
# curpath="E:/"

class Comparison(KnownDiscrepancies):
    reports: List[SourceBase] = []
    diff = None  #
    diff_rows = None  # Rows that Exists in both/all but are different in data
    common_rows = None
    comparison_end_date = None
    comparison_start_date = None
    simple_difference_comparison = None
    output_xslx = False
    output_csv = False
    interval = None
    cascade = False
    cascade_start_date = None
    cascade_end_date = None
    dashboard_regression = False
    output_console = False
    merge = None
    validations = {
        "OLAP": None,
        "calculations": None
    }
    simple_report_name = None
    simple_difference = None
    has_missing_rows = False
    passing_records = None
    edw2_mismatches = None
    edw3_mismatches = None
    merchant = None
    edw3_orphans = None
    edw2_orphans = None
    prepared_col_map = None
    display_groups = []

    def __init__(self, *reports, sim=None):
        self.reports = reports
        self.has_missing_rows = False
        self.simulation = sim

    async def run(self):
        self.__add_simulation()
        await self.load()
        for report in self.reports:
            if report.data is None:
                # print(f"\n \n Skipping report that returned no data from - {vars(report)['picker_url']}...", json.dumps(vars(report)["request_object"]), "\n")
                return False
        if args.no_error is False:
            self.__validate()
            self.__make_names_distinct()
            self.__get_orphans()
            self.__get_diff()
            self.__get_known_discrepancies()
        return True

    async def run_and_barf(self):
        if not await self.run():
            # print("Skipping barf due to no data")
            return {"error": True,
                    "error_status": self.reports[0].error}
        else:
            return {"error": False, "error_status": "N/A"}

    async def load(self):
        # TODO: Futures pattern
        futures = []
        for report in self.reports:
            futures.append(report.load())
        await asyncio.gather(*futures)
        try:
            # print(futures[0])
            self.prepared_col_map = futures[0].prepared_col_map
            self.display_groups = futures[0].display_groups
        except Exception as e:
            # print(e)
            pass

    def set_outputs(self,
                    merchant=None,
                    output_xlsx=False, output_csv=False,
                    output_slack=False, interval=None,
                    comparison_start_date=None, comparison_end_date=None,
                    simple_difference=None,
                    dashboard_regression=False,
                    simple_report_name=None, cascade=False,
                    cascade_start_date=None, cascade_end_date=None
                    ):
        if simple_difference is None:
            simple_difference = {
                "join_on": None,
                "comparison_column": None
            }
        self.output_xslx = output_xlsx
        self.output_csv = output_csv
        self.output_slack = output_slack
        self.cascade = cascade
        self.merchant = merchant
        self.cascade_start_date = cascade_start_date
        self.cascade_end_date = cascade_end_date
        self.dashboard_regression = dashboard_regression
        self.interval = interval
        self.simple_difference = simple_difference
        self.simple_report_name = simple_report_name
        self.comparison_start_date = comparison_start_date
        self.comparison_end_date = comparison_end_date

    """
        Ensure that both of these reports can be validated. If not raise an exception so
    """

    def __validate(self):
        # Do we have at least two reports to compare?
        if len(self.reports) < 2:
            raise Exception("At least two reports must be provided for comparison")
        # Do we have the same column names?
        if len(set([str(list(report.data.columns.values)) for report in self.reports])) != 1:
            print(str(list(self.reports[0].data.columns.values)))
            print(str(list(self.reports[1].data.columns.values)))
            raise Exception("Column headers on all reports must be identical. "
                            "If the source columns don't match, try passing in the column names as a list.")
        # Are there any known Discrepancies, if So, There should only be 2 reports passes.
        if len(self.known_discrepancies) and len(self.reports) > 2:
            raise Exception("When Evaluating reports with known discrepancies, only 2 reports should be passed "
                            "at a time. Multi report support coming soon.")
        # TODO: other validations

    def __add_simulation(self):
        if self.simulation is None:
            return
        for report in self.reports:
            if "https://picker-shard.avantlink.com/rpt" in report.picker_url:
                for x in report.request_object:
                    for col in report.request_object[x]["cols"]:
                        try:
                            if col["fact"] is True and col["id"] != "calculation":
                                col["sim"] = self.simulation
                            if col["id"] == "calculation":
                                for var in col["vars"]:
                                    try:
                                        if col["vars"][var]["fact"] is True:
                                            col["vars"][var]["sim"] = self.simulation
                                    except KeyError as e:
                                        print(e, 'was not specified to be True in calculation variable', var)
                                        pass
                        except KeyError as e:
                            print(e, 'was not specified to be True in', col["id"])
                            pass

    @staticmethod
    def sql_validation(sql_query):
        datasource = None
        keywords = {
            "tracking": "fact_postgres",
            "redshift": "fact_redshift",
            "olap": "olap",
            "cube": "cube_postgres"
        }
        for keyword in keywords:
            if keyword in sql_query[0]:
                datasource = keywords[keyword]
        return datasource

    def remove_spaces(self, string_val):
        cleaned_string = string_val.replace(" ", "")
        return cleaned_string

    def __get_diff(self):
        # Create a new dataframe filled with false values that matches the size of the first report.
        # This is just a simple way of accomplishing this:
        self.diff = pandas.DataFrame(columns=self.reports[0].data.columns.values,
                                     index=range((~self.reports[0].orphans['is_orphan']).sum())).fillna(False)
        edw3_df = self.reports[0].data
        edw2_df = self.reports[1].data
        edw3_sql = self.reports[0].report["_queries"]
        data_source = self.sql_validation(edw3_sql)

        edw3_ro = json.dumps(self.reports[0].request_object)
        edw2_ro = json.dumps(self.reports[1].request_object)

        # Exists in EDW3 Only -Boolean
        edw3_orphans_bool = self.reports[0].orphans['is_orphan']
        edw2_orphans_bool = self.reports[1].orphans['is_orphan']

        # This line will give you ONLY rows that exist in both,
        # removing the tilde would give you the rows that only exist in edw3
        edw3_matches_found = edw3_df[~edw3_orphans_bool].reset_index(drop=True)
        edw2_matches_found = edw2_df[~edw2_orphans_bool].reset_index(drop=True)

        # Check if length of dataframes are equal
        # If not, drop the last few rows
        try:
            assert len(edw3_df.index) == len(edw2_df.index)
        except AssertionError:
            difference = len(edw3_df.index) - len(edw2_df.index)
            if difference < 0:
                print(edw2_df)
                print(edw3_df)
                print('WARNING: EDW2 found more results than edw3.')
                print('Trying to drop 0s from edw2. If that does not solve this a discrepency will be posted')
                column_name = edw2_df.columns[1]
                print('New edw2 df:')
                edw2_df = edw2_df.loc[edw2_df[column_name] != '$0.00']
                print(edw2_df)
            else:
                print('WARNING: Results did not match. Adjusting by dropping extra rows from edw3 result')
                print('Initial results:')
                print('EDW2: ', len(edw2_df.index))
                print('EDW3: ', len(edw3_df.index))
                edw3_df.drop(edw3_df.tail(difference).index, inplace=True)
                print('EDW3 (adjusted): ', len(edw3_df.index))

        # Present in both - but don't match
        try:
            matching = edw3_matches_found == edw2_matches_found
            not_matching = edw3_matches_found != edw2_matches_found
        except:
            print(edw2_matches_found)
            print('\n\n')
            print(edw3_matches_found)
            print('\n\n')
            print(
                '\n\n****POSSIBLE SOLUTIONS*****\n\n1)Make sure column names are IDENTICAL\n \
                2)May need to remove hidden columns\n\n')
            print(edw2_matches_found.head())
            print(edw3_matches_found.head())
            raise

        matching = matching.assign(sum_of_facts=True)
        not_matching = not_matching.assign(sum_of_facts=True)

        for fact in self.reports[0].facts:
            matching['sum_of_facts'] = matching['sum_of_facts'] & matching[fact]
            not_matching['sum_of_facts'] = not_matching['sum_of_facts'] & not_matching[fact]

        # All records matching and present in both
        self.passing_records = edw3_matches_found[matching['sum_of_facts']]
        # Records found in both without match
        self.edw2_mismatches = edw2_matches_found[~matching['sum_of_facts']]
        self.edw3_mismatches = edw3_matches_found[~matching['sum_of_facts']]
        # Records only found in one report
        self.edw2_orphans = edw2_df[edw2_orphans_bool]
        self.edw3_orphans = edw3_df[edw3_orphans_bool]

        if self.simple_difference:

            col_x = self.simple_difference["comparison_col_name"] + '_edw2'
            col_y = self.simple_difference["comparison_col_name"] + '_edw3'
            regex_query_selector = '([^0-9.-])+'

            matches = self.passing_records.copy()
            matches.rename(columns={self.simple_difference["comparison_col_name"]: col_x}, inplace=True)
            matches[col_y] = matches[col_x]

            # Try to merge on day
            # If that fails, fallback to merging on Date Range
            try:
                mismatches = self.edw2_mismatches.merge(
                    self.edw3_mismatches,
                    on=self.simple_difference["join_on"],
                    how="outer",
                    suffixes=["_edw2", "_edw3"]
                )
            except:
                mismatches = self.edw2_mismatches.merge(
                    self.edw3_mismatches,
                    on=["Date Range"],
                    how="outer",
                    suffixes=["_edw2", "_edw3"]
                )

            edw2_orphans = self.edw2_orphans.copy()
            edw2_orphans.rename(columns={self.simple_difference["comparison_col_name"]: col_x}, inplace=True)
            edw3_orphans = self.edw3_orphans.copy()
            edw3_orphans.rename(columns={self.simple_difference["comparison_col_name"]: col_y}, inplace=True)
            edw2_orphans[col_y] = 0
            edw3_orphans[col_x] = 0
            orphans = pd.concat([edw2_orphans, edw3_orphans], ignore_index=True)
            # Cleaning All non-numeric Characters, convert to float
            orphans[col_x] = orphans[col_x].replace(regex_query_selector, '', regex=True).astype(float)
            orphans[col_y] = orphans[col_y].replace(regex_query_selector, '', regex=True).astype(float)
            mismatches[col_x] = mismatches[col_x].replace(regex_query_selector, '', regex=True).astype(float)
            mismatches[col_y] = mismatches[col_y].replace(regex_query_selector, '', regex=True).astype(float)
            # Adding 'Difference' column
            mismatches['difference'] = mismatches[col_x] - mismatches[col_y]
            orphans['difference'] = orphans[col_x] - orphans[col_y]
            matches['difference'] = 0
            merge = pd.concat([matches, mismatches, orphans])
            merge[col_x] = merge[col_x].replace(regex_query_selector, '', regex=True).astype(float)
            merge[col_y] = merge[col_y].replace(regex_query_selector, '', regex=True).astype(float)
            merge['difference'] = merge[col_x] - merge[col_y]

            # Set pass/fail criteria here
            # If everything is 0 in both arrays, call it a special case pass
            flag = 'PASS!'
            if np.all(merge[col_x].values == 0) and np.all(merge[col_y].values == 0): 
                flag = 'PASS! ALL ZEROS!'
            else:
                for num in merge['difference'].values:
                    if num != 0:
                        flag = 'FAIL!'
            merge['pass/fail'] = flag
            self.simple_difference_comparison = merge

            if self.dashboard_regression:
                merge["Dashboard Report Name"] = self.dashboard_regression["dashboard report name"]
                merge["Dashboard Category"] = self.dashboard_regression["category"]
                merge["merchant"] = self.dashboard_regression["merchant"]
                merge["widget"] = self.dashboard_regression["widget"]
                report_date_range = None
                if self.dashboard_regression["widget"] == "trending_widget":
                    widget_marker = 'TW_'
                elif self.dashboard_regression["widget"] == "top_affiliates_widget":
                    widget_marker = 'TA_'
                else:
                    widget_marker = 'NW_'

                ## Date Validation and addition to report
                try:
                    if merge["Day"] is not None:
                        last_day_index = len(merge["Day"].values) - 1
                        last_day = merge["Day"].values[last_day_index]
                        first_day = merge["Day"].values[0]
                        report_date_range = f"{first_day} - {last_day}"
                except Exception as e:
                    # print(e)
                    pass
                try:
                    if merge["Date Range"][0] is not None:
                        last_range_index = len(merge["Date Range"]) - 1
                        last_range = merge["Date Range"][last_range_index]
                        first_range = merge["Date Range"][0]
                        if first_range == last_range:
                            report_date_range = first_range
                        else:
                            report_date_range = f"Mixed:[{first_range}, {last_range}]"
                except:
                    pass
                finally:
                    self.dashboard_regression["Report Date Range"] = report_date_range
                xlsx_name = self.simple_difference["comparison_col_name"].replace(" ", "")
                xlsx_name = xlsx_name[:26].replace("Average", "Avg").replace("Affiliate", "Affil")
                xlsx_name = widget_marker + xlsx_name
                # noinspection PyTypeChecker
                category_dir = self.dashboard_regression["category"].replace(' ', '_')
                filepath = os.path.join(self.dashboard_regression["path"], self.dashboard_regression["widget"],
                                        category_dir, xlsx_name) + ".xlsx"
            else:

                if self.simple_difference["manual_path"]:
                    filepath = f"{self.simple_difference['manual_path']}/" \
                               + "" + '_' + f"{self.simple_difference['comparison_col_name']}.xlsx"
                else:
                    try:
                        cascade_dir_name = os.path.join(curpath + '/validation_outputs/xlsx/simple_difference')
                        os.mkdir(cascade_dir_name)
                    except FileExistsError:
                        pass
                    finally:
                        filepath = "./validation_outputs/xlsx/simple_difference/" + \
                                   + self.merchant + '_' + self.simple_difference["comparison_col_name"] + '.xlsx'
            merge["SQL_source"] = data_source
            merge['edw2_request_object'] = edw2_ro
            merge['edw3_request_object'] = edw3_ro
            self.merge = merge
            merge.to_excel(filepath)

    def validate_calculations(self):
        # edw3_ro = json.dumps(self.reports[0].request_object)
        # edw2_ro = json.dumps(self.reports[1].request_object)
        # print(edw3_ro)
        # print(edw2_ro)
        pass

    def __get_known_discrepancies(self):
        if len(self.known_discrepancies) == 0:
            return
        self.load_reports(self.reports[0], self.reports[1])

        self.run_known_discrepancies(self.source_report, self.report2, self.known_discrepancies)

    def __make_names_distinct(self):

        for idx in range(len(self.reports)):
            if len([x.report_name for x in self.reports if x.report_name == self.reports[idx].report_name]) > 1:
                self.reports[idx].report_name += ' (%(idx)s)' % {'idx': idx}

    # print("validate3")

    """
        Populate the orphans dataframe on each object. - Orphans are rows which are found in one report but not
        present in all other (missing from at least one other report)
    """

    def __get_orphans(self):

        for idx in range(len(self.reports)):
            self.reports[idx].pack_dims()
        # build the dataframes labeled "orphans" with rows that are missing in at least one other dataframe
        for idxLocal in range(len(self.reports)):
            # we are checking to see if there are any rows present in this report that are missing from ANY other report.
            # We don't need to worry if there are rows in the comparison report has that the local one is missing
            # because that report will be compared to this one when it is the local.

            # Start by populating the orphans with a single column FALSE boolean that otherwise matches the length:
            self.reports[idxLocal].orphans = pandas.DataFrame(columns=['is_orphan', 'missing_in'],
                                                              index=range(self.reports[idxLocal].data.shape[0]))
            self.reports[idxLocal].orphans['is_orphan'].fillna(False, inplace=True)
            for idxCompare in range(len(self.reports)):
                if idxCompare == idxLocal:
                    # Skipping self
                    continue
                orphans = self.reports[idxLocal].packed_dims['col0'].isin(self.reports[idxCompare].packed_dims['col0'])
                self.reports[idxLocal].orphans.loc[~orphans, 'is_orphan'] = True
                self.reports[idxLocal].orphans.loc[
                    ~(orphans & ~(self.reports[idxLocal].orphans['missing_in'].isna())), 'missing_in'] = \
                    self.reports[idxLocal].orphans[orphans & ~(self.reports[idxLocal].orphans['missing_in'].isna())][
                        'missing_in'] + '||'
                self.reports[idxLocal].orphans.loc[
                    ~(orphans & (self.reports[idxLocal].orphans['missing_in'].isna())), 'missing_in'] = ''
                self.reports[idxLocal].orphans.loc[~orphans, 'missing_in'] = self.reports[idxLocal].orphans[~orphans][
                                                                                 'missing_in'] + self.reports[
                                                                                 idxCompare].report_name
            self.has_missing_rows = self.has_missing_rows or self.reports[idxLocal].orphans['is_orphan'].sum() > 0

    def __list_concatenation(self, item_list):

        if not item_list:
            return ""
        item_list = item_list.split('||')
        if len(item_list) == 1:
            return "{}.".format(item_list[0])
        # Join all items except the last one with a comma between them
        out = ", ".join(map(str, item_list[:-1]))
        # Add the last element, separated by "and" and a final "."
        return "{} and {}.".format(out, item_list[-1])
        # print("validate6")

    def output_to_console(self, filter=True):
        if self.output_console:
            pass
        pass

    def clean_name(self, report_name):
        report_name = re.sub("[^0-9a-zA-Z]+", "_", report_name)
        return report_name

    def output_to_excel(self):
        return "testing"
        if self.output_xslx:
            xlsx_filename = ''

            report_dir_name = self.simple_report_name
            try:
                cascade_dir_name = os.path.join(curpath + '/validation_outputs/xlsx/', 'cascade')
                os.mkdir(cascade_dir_name)

            except Exception:
                pass
            try:
                cascade_report_dir_name = os.path.join(
                    curpath + '/validation_outputs/xlsx/cascade/',
                    report_dir_name
                )
                os.mkdir(cascade_report_dir_name)
            except Exception:
                pass
            try:
                cascade_interval_dir_name = os.path.join(
                    curpath + '/validation_outputs/xlsx/cascade/', report_dir_name,
                    self.interval
                )
                os.mkdir(cascade_interval_dir_name)
            except Exception:
                pass
            total_matches = len(self.passing_records)
            total_orphans = len(self.edw3_orphans) + len(self.edw2_orphans)
            total_mismatches = len(self.edw3_mismatches)
            summary_string_extension = "__" + \
                                       str(total_matches) + '--' + \
                                       str(total_mismatches) + '--' + \
                                       str(total_orphans)
            xlsx_filename = self.simple_report_name + summary_string_extension
        xlsx_filename = xlsx_filename + '.xlsx'
        xlsx_filename = os.path.join(curpath + '/validation_outputs/xlsx/', xlsx_filename)
        print('OUTPUTTING IN EXCEL -- ' + xlsx_filename)
        request_objects_hash = pd.DataFrame({
            "request_object_1": self.reports[0].request_object,
            "request_object_2": self.reports[1].request_object
        })
        with pd.ExcelWriter(xlsx_filename, engine='xlsxwriter') as writer:
            self.passing_records.to_excel(writer, sheet_name='passing_records')
            self.edw2_mismatches.to_excel(writer, sheet_name='edw2_mismatches')
            self.edw3_mismatches.to_excel(writer, sheet_name='edw3_mismatches')
            self.edw3_orphans.to_excel(writer, sheet_name='edw3_orphans')
            self.edw2_orphans.to_excel(writer, sheet_name='edw2_orphans')
            request_objects_hash.to_excel(writer, sheet_name='request_objects')
            writer.save()


def output_to_slack(self):
    # TODO
    pass


def output_to_csv(self):
    pass
