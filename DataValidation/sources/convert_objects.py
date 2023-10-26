from pprint import pprint
from requests import post
import json

from sources.test_objects import set_1
from sources.column_map import columns_map
from sources.source_picker_report import PickerReport
from sources.prepared_columns_map import prepared_columns_map


true = True
false = False


class ConvertRequestObject(object):
    """
    Converts an EDW2 Request Object into an EDW3 Request Object.
    Can be retrieved at:
     -- self.edw3_request_object
      ----# As a Python Dictionary
    or
     -- self.json
      ----# As a JSON dump
    """

    def __init__(self, edw2_request_object=None):
        self.edw2_request_object = edw2_request_object
        self.edw3_columns = []
        self.edw3_filters = []
        self.edw3_request_object = edw2_request_object
        self.json = None
        self.errors = []
        self.picker_url = 'https://picker-dev.avantlink.com/rpt'
        self.report_name = [x for x in edw2_request_object if x[0] != '_'][0]
        self.run()

    def __convert_columns(self):
        """
        accepts an edw2 column literal object and returns an edw3 equivalent
        :param edw2_column_literal:
        :return: edw3_column_literal
        """
        for x in self.edw3_request_object:
            for prop in self.edw3_request_object[x]:
                if prop == "cols":
                    for column in self.edw3_request_object[x][prop]:
                        if "prepared_id" in column:
                            self.edw3_columns.append(column)
                            continue
                        # Process non-calculation columns
                        try:
                            if column["id"] != "calculation":
                                self.edw3_columns.append(self.convert_fact(column))
                                continue
                        except KeyError as e:
                            print("this column does not have an 'id'. Check for 'prepared_id' :: " % column)
                        else:
                            # Process calculation columns
                            calculation_conversion = column.copy()
                            converted_variables = {}
                            for var in column["vars"]:
                                converted_variables[var] = self.convert_fact(column["vars"][var])
                            calculation_conversion["vars"] = converted_variables
                            self.edw3_columns.append(calculation_conversion)
                    self.edw3_request_object[x][prop] = self.edw3_columns
                if prop == "filters":
                    for filter_literal in self.edw3_request_object[x][prop]:
                        self.edw3_filters.append(self.__convert_filter(filter_literal))
                    self.edw3_request_object[x][prop] = self.edw3_filters

    def convert_fact(self, fact_literal):
        # @TODO: NOTE: aggregate will default to -- distinct == false
        # Do not process dimension columns. They are unchanged
        global agg_function, agg_distinct
        agg_filter = None
        try:
            if prepared_columns_map[fact_literal["id"]] != "fact" or "pk" in fact_literal["id"]:
                return fact_literal
        except KeyError as e:
            print("pushing error for ",  e)
            self.errors.append({
                "missing_from": "Prepared Columns Map",
                "columns_name": e
            })
            return fact_literal
        except TypeError as e:
            print("pushing TYPE error for ", e)
            self.errors.append({
                "typeError": e,
            })
            return fact_literal
        conversion = fact_literal.copy()
        edw2_table_id = fact_literal["id"]
        try:
            conversion["id"] = columns_map[edw2_table_id]["table_id"]
        except KeyError as e:
            print("pushing error for ",  e)
            self.errors.append({
                "missing_from": "Columns_map",
                "columns_name": e
            })
            return fact_literal

        if "aggregate" not in conversion:
            conversion["aggregate"] = [{
                "func": columns_map[edw2_table_id]["aggregate"],
                "distinct": false
            }]

        if "aggregate" in conversion:
            for idx, literal in enumerate(conversion["aggregate"]):
                if "func" in literal and "distinct" in literal:
                    agg_function = literal["func"]
                    agg_distinct = literal["distinct"]
                    del conversion["aggregate"][idx]

        if "fact_calculation" in conversion["id"]:
            agg_filter = {
                "func": "filter",
                "op": "eq",
                "field": "dim_calculation_type-calculation_type_name",
                "values": [
                    columns_map[edw2_table_id]["filter"]
                ]
            }

        if "fact_event" in conversion["id"]:

            agg_filter = {
                "func": "filter",
                "op": "eq",
                "field": "dim_event_type-event_type_name",
                "values": [
                    columns_map[edw2_table_id]["filter"]
                ]
            }
        if agg_filter is not None:
            conversion["aggregate"].append(agg_filter)
        conversion["aggregate"].append({
            "distinct": agg_distinct or false,
            "func": agg_function
        })
        return conversion

    def process_filter(self, filter_literal):
        if filter_literal['op'] in ['AND', 'OR']:
            sub_filters = []
            for sub_filter in filter_literal['sub_filters']:
                sub_filters.append(self.process_filter(sub_filter))
            filter_literal['sub_filters'] = sub_filters
            return filter_literal
        else:
            edw2_table_id = filter_literal["field"]
            if edw2_table_id in columns_map:
                filter_literal["field"] = columns_map[edw2_table_id]["table_id"]
            return filter_literal

    def __convert_filter(self, filter_literal):
        conversion = filter_literal.copy()
        conversion = self.process_filter(conversion)
        return conversion

    def run(self):
        self.__convert_columns()
        self.json = json.dumps(self.edw3_request_object)

# pp = pprint(set_1[0], indent=2)
# tester = ConvertRequestObject(set_1[1])

# pprint(tester.edw3_request_object,indent=2)