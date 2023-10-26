import pandas
import sources
from sources.comparison import define_join_on

import re
import asyncio
import json
from datetime import datetime
from pprint import pprint
import sys
import copy
import os

import pandas as pd

false = False
true = True
null = None

request_objects = json.load(open('./sources/json_sources/manual_comparison_objects.json'))


def extract_words(messy_string):
    """
    Accepts a calculation string and extracts individual variable names.

    Args:
        messy_string: str: calculation string i.e. (sale+ppb)/cpc

    Returns: []: extracted variable names i.e. ["sale", "ppb", "cpc"]
    """
    regex = re.compile('[^a-zA-Z]')
    messy_string = regex.sub(' ', messy_string)
    cleaned_string = " ".join(messy_string.split())
    return cleaned_string


def breakdown_calculations(calc_request_object: object) -> object:
    report_id = None
    calculation_variables = None
    for ro_id in calc_request_object:
        report_id = ro_id
    for col in calc_request_object[report_id]["cols"]:
        if col["id"] == "calculation":
            calculation = col["calc"]
            calculation_variables = extract_words(calculation).split(' ')
    return calculation_variables


def build_single_var_request_object(calc_request_object, col_name):
    edw2_new_report_id = f"edw2_{col_name}"
    edw3_new_report_id = f"edw3_{col_name}"
    new_request_object = {}
    report_id = None
    calc_object = copy.deepcopy(calc_request_object)

    for id in calc_request_object:
        report_id = id
    for col in calc_object[report_id]["cols"]:
        if col["id"] == "calculation":
            col["calc"] = col_name
            col["name"] = col_name
            col["alias"] = col_name

    if "edw2" in report_id:
        new_request_object[edw2_new_report_id] = calc_object[report_id]
    if "edw3" in report_id:
        new_request_object[edw3_new_report_id] = calc_object[report_id]
    return {"ro": new_request_object, "var_name": col_name}


def build_var_separated_request_objects(calc_request_object):
    result = []
    calculation_vars = breakdown_calculations(calc_request_object)
    for var in calculation_vars:
        separated_object = build_single_var_request_object(calc_request_object, var)
        result.append(separated_object)
    return result


def match_var_object_pairs(edw2_objects_list, edw3_objects_list):
    pairs_literal = {}
    for single_var_request in edw2_objects_list:
        if single_var_request["var_name"] not in pairs_literal:
            pairs_literal[single_var_request["var_name"]] = []
        pairs_literal[single_var_request["var_name"]].append(single_var_request["ro"])
    for single_var_request in edw3_objects_list:
        pairs_literal[single_var_request["var_name"]].append(single_var_request["ro"])
    return pairs_literal


def combine_reports(dir_path):
    reports = []
    combined_report_name = os.path.join(dir_path, "cb.xlsx")
    for report_name in os.listdir(dir_path):
        report_filepath = os.path.join(dir_path, report_name)
        df = pandas.read_excel(report_filepath)
        reports.append(df)
    # Notes: the issue in writing the combined report has to do
    # with the length of the filename it has to write to.
    # consider abbreviating using './local/notation'
    print(len(combined_report_name))
    with pd.ExcelWriter(combined_report_name) as writer:
        for idx, dataframe in enumerate(reports):
            dataframe.to_excel(writer, sheet_name=idx)
    print("Calculation Breakdown, All Done")


def run_reports(request_object_pairs_list, source=None):
    timestamp = datetime.now().strftime("%x %X")
    timestamped_label = '/validation_outputs/xlsx/calc_breakdown--' + timestamp.replace("/", "_")
    calc_breakdown_report_dir_path = os.path.join(os.getcwd() + timestamped_label)
    os.mkdir(calc_breakdown_report_dir_path)

    for key in request_object_pairs_list.keys():
        comparison = sources.Cascade()
        edw2_request_object = request_object_pairs_list[key][0]
        edw3_request_object = request_object_pairs_list[key][1]
        join_on = define_join_on(edw2_request_object, edw3_request_object)
        loop = asyncio.new_event_loop()
        print(f"Currently running comparison over {key}")
        try:
            start = datetime.now()
            # code ...
            loop.run_until_complete(
                comparison.run_simple_difference(
                    {"join_on": join_on,
                     "comparison_col_name": key},
                    edw2_ro=edw2_request_object, edw3_ro=edw3_request_object, sim=None, source=source,
                    report_name=key, manual_path=calc_breakdown_report_dir_path)
            )
            print("Total runtime: ", datetime.now() - start)
        except KeyboardInterrupt:
            sys.exit()
        except asyncio.TimeoutError as e:
            print(e)
        finally:
            loop.close()
    # @TODO: combine the reports if/when possible. MVP viable without combination.
    # combine_reports(calc_breakdown_report_dir_path)


if __name__ == '__main__':
    edw2_var_objects = build_var_separated_request_objects(request_objects["edw2_request_object"])
    edw3_var_objects = build_var_separated_request_objects(request_objects["edw3_request_object"])
    pairs = match_var_object_pairs(edw2_var_objects, edw3_var_objects)

    run_reports(pairs, source='fact_redshift')
