import pandas
from colorama import *
import numpy as np
import math
from sources.base import SourceBase
__author__ = "LeChristopher Blackwell"


class KnownDiscrepancies(SourceBase):
    """
    This Class will accept 2 reports for comparison, as well as a List [] of Acceptable Discrepancies.
    It sorts all discrepancies found between reports into 2 categories
    stored under KnownDiscrepancies.discrepancies_found
    """
    cols_with_discrepancies = {}
    discrepancies_found = {
        "acceptable": {},
        "unacceptable": {}
    }
    known_discrepancies = []
    operators = {}
    report2 = None
    report2_col_literal = {}
    report2_dropped_rows = {}
    source_report = None
    source_dropped_rows = {}
    source_report_col_literal = {}

    def __init__(self):
        self.cols_with_discrepancies = {}
        self.discrepancies_found = {
            "acceptable": {},
            "unacceptable": {}
        }
        self.known_discrepancies = []
        self.operators = {
            "gte": ">=",
            "lte": "<=",
            "range": None
        }
        self.report2 = None
        self.report2_col_literal = {}
        self.report2_dropped_rows = {}
        self.source_report = None
        self.source_report_col_literal = {}
        self.source_report_dropped_rows = {}

    @staticmethod
    def calculate_acceptable_range(source, discrepancy_literal):
        """
        Calculates the acceptable range used to evaluate if a discrepancy found is
        "acceptable" or "unacceptable"

        :param source: integer. The number to be considered the source of truth.
        :param discrepancy_literal: acceptable_discrepancy = {
                                    "column_name": 'column 1',
                                    "op": "gte",  # operation: gte , lte, range
                                    "measure": "%",  # (static, %)
                                    "value": 5  # (any integer or float)
                                    }
        :return: Returns a List [] containing an upper and lower boundary for acceptable discrepancies
        """
        if discrepancy_literal["measure"] != 'static' and discrepancy_literal["measure"] != '%':
            raise AttributeError('the value of "measure" must equal "%" or "static"')

        measure = discrepancy_literal["measure"]
        operand = discrepancy_literal["op"]
        value = discrepancy_literal["value"]
        percent_multiplier = np.multiply(value, .01)
        multiplied_acceptable_difference = np.multiply(source, percent_multiplier)
        add_percent_acceptable_difference = np.add(source, multiplied_acceptable_difference)
        print(add_percent_acceptable_difference)
        add_static_acceptable_difference = np.add(source, value)
        subtract_percent_acceptable_difference = np.subtract(source, multiplied_acceptable_difference)
        subtract_static_acceptable_difference = np.subtract(source, value)

        if operand == "gte":
            if measure == "%":
                return source, add_percent_acceptable_difference
            elif measure == "static":
                return source, add_static_acceptable_difference
        elif operand == "lte":
            if measure == "%":
                return subtract_percent_acceptable_difference, source
            elif measure == "static":
                return subtract_static_acceptable_difference, source
        elif operand == "range":
            if measure == "%":
                return subtract_percent_acceptable_difference, add_percent_acceptable_difference
            elif measure == "static":
                return subtract_static_acceptable_difference, add_static_acceptable_difference

    def cleanse_inputs(self):
        """
        Removes commas from string inputs and converts to a Float. - Mutative.

        :return: Returns Nothing
        """
        for col_name in self.cols_with_discrepancies:
            # Cleanse source report
            self.source_report_col_literal[col_name] = self.source_report_col_literal[col_name].str.replace(',', '')
            self.source_report_col_literal[col_name] = self.source_report_col_literal[col_name].astype(float)
            # Cleanse report 2
            self.report2_col_literal[col_name] = self.report2_col_literal[col_name].str.replace(',', '')
            self.report2_col_literal[col_name] = self.report2_col_literal[col_name].astype(float)

    def evaluate(self):
        """
        This function is responsible for processing a comparison between all respective values
        in the DataFrames provided - calculating an acceptable range based on provided Discrepancy Literals

        Sets the results on self.discrepancies_found under either ["acceptable"] or ["unacceptable"]

        :return: Returns Nothing
        """
        self.cleanse_inputs()
        # Check report1 vs report2 row values by column and index
        for col_name in self.columns:
            for idx, val in self.source_report_col_literal[col_name].items():
                val2 = self.report2_col_literal[col_name][idx]
                if val2 == val:
                    continue
                # If the values do not match, a discrepancy has been found
                else:
                    # If the column has expected discrepancies
                    if col_name in self.cols_with_discrepancies:
                        lower_boundary, upper_boundary = self.calculate_acceptable_range(
                            val,
                            self.cols_with_discrepancies[col_name]
                        )
                        # Check if the value is within the acceptable range
                        if self.range_check(val2, lower_boundary, upper_boundary):
                            # Store it in discrepancies_found:acceptable for reporting
                            self.__manage_discrepancy_index_literal(col_name, "acceptable", idx, val, val2)
                        else:
                            # Store it in discrepancies_found:unacceptable for reporting
                            self.__manage_discrepancy_index_literal(col_name, "unacceptable", idx, val, val2)
                    else:
                        self.__manage_discrepancy_index_literal(col_name, "unacceptable", idx, val, val2)

    def load_discrepancies(self, discrepancy_array):
        """
        :param discrepancy_array: i.e...

        acceptable_discrepancies = [{
            "column_name": 'action amount',
            "op": "gte", (gte, lte, range)
            "measure": "%",  # (static, %)
            "unit": 1  # (any int)
        },

        ^^ This would mean that: within the 'action amount' column, the acceptable discrepancy range for
         any value can be expressed as : source_value <= acceptable_range <= source_value * 1.01

        {
            "column_name": 'network amount',
            "op": "range",
            "measure": "static",  # (static, %)
            "unit": 5  # (any int)
        }]

        ^^ This would mean that: within the 'network amount' column, the acceptable discrepancy range for
         any value can be expressed as : source_value - 5 <= acceptable_range <= source_value + 5


        :return: Returns Nothing
        """
        if not isinstance(discrepancy_array, list):
            raise TypeError('{d} is an invalid input. Input must be a list [...]'.format(d=discrepancy_array))
        for discrepancy_literal in discrepancy_array:
            if not discrepancy_literal["measure"] \
                    or not discrepancy_literal["op"] \
                    or not discrepancy_literal["column_name"] \
                    or not discrepancy_literal["value"]:
                raise AttributeError('The Discrepancy Literal must contain the following keys:'
                                     ' "measure", "op", "column_name", "value"')
            if math.isnan(discrepancy_literal["value"]):
                raise TypeError('discrepancy_literal["value"] must be a numeric value')
            if not isinstance(discrepancy_literal["op"], str):
                raise TypeError('discrepancy_literal["op"] must be of type "str"')

        self.known_discrepancies = discrepancy_array
        for literal in discrepancy_array:
            self.cols_with_discrepancies[literal["column_name"]] = literal

    def load_reports(self, report1, report2):
        """
        Loads the reports into the class and store columns of each report in respective

        Object literals {"col_name": [data]} indexed by column name

        :param report1: {DataFrame/.csv}
        :param report2: {DataFrame/.csv}

        :return: Returns Nothing
        """
        self.source_report = report1 if isinstance(report1, pandas.DataFrame) else pandas.read_csv(report1)
        self.report2 = report2 if isinstance(report2, pandas.DataFrame) else pandas.read_csv(report2)

        for col_name in self.columns:
            self.source_report_col_literal[col_name] = self.source_report[col_name]
            self.report2_col_literal[col_name] = self.report2[col_name]

    def __manage_discrepancy_index_literal(self, col_name, acceptability, idx, val, val2):
        """
        Populates the self.discrepancies_found dictionary. The dictionary is number indexed
        BY THE INDEX OF THE DISCREPANCY FOUND, Not the number of discrepancies found.

        :param col_name: {string}
        :param acceptability: {string - "acceptable" or "unacceptable}
        :param idx: {integer} - index of the current values passed
        :param val: {float} - input value from source report
        :param val2: {float} - input value from report2

        :return: Returns nothing.
        """
        if col_name not in self.discrepancies_found[acceptability]:
            self.discrepancies_found[acceptability][col_name] = {}
        self.discrepancies_found[acceptability][col_name][idx] = [val, val2]

    @staticmethod
    def range_check(number, lower_boundary, upper_boundary):
        """
          Checks to see if the given number is within the range passed

        :param number: Any Numeric Value
        :param lower_boundary: lower_boundary
        :param upper_boundary: upper_boundary
        :return: BOOLEAN - True if the number is within range. False if not.
        """
        if math.isnan(lower_boundary) or math.isnan(upper_boundary) or math.isnan(number):
            raise TypeError("All arguments provided must be numeric values. math.isnan(argument) == false")
        if lower_boundary <= number <= upper_boundary:
            return True
        else:
            return False

    def remove_missing(self):
        """
        Runs a comparison between reports to to find what, if any, records in Report A are missing from Report B.

        Removes Records found in Report B that are not present in report A.
        Removes Records found in Report A that are not present in report B.

        JSON rows removed from both reports in a print statement to the console.

        :return: Returns Nothing
        """
        # See if the DataFrames are equal
        source = self.source_report
        report2 = self.report2
        if source.equals(report2):
            return "No Rows Missing. All Data is equal"
        else:
            df1_null_comparison = source[~source.isin(report2)]
            df1_discrepancies = df1_null_comparison[df1_null_comparison.notnull().any(axis=1)]
            df2_null_comparison = report2[~report2.isin(source)]
            df2_discrepancies = df2_null_comparison[df2_null_comparison.notnull().any(axis=1)]
            print(Back.WHITE + Fore.BLACK + str({
                'records_missing_from_df1': df2_discrepancies,
                'records_missing_from_df2': df1_discrepancies
            }) + Back.RESET + Fore.RESET)
            # Remove rows found in report2 that are not present in the source report
            for idx, val in df2_discrepancies.iterrows():
                print(
                    Back.CYAN + Fore.LIGHTWHITE_EX + 'The following Row located at index position - {index}'
                    ' - is being removed from Report 2: {data}'.format(
                        index=idx,
                        data=report2.loc[idx])
                    + Back.RESET + Fore.RESET
                )
                self.report2_dropped_rows[idx] = report2[idx]
                self.report2 = report2.drop(report2.index[idx])

    def run_known_discrepancies(self, report1, report2, discrepancy_array):
        """
        :param report1: DataFrame
        :param report2: DataFrame
        :param discrepancy_array: Refer to KnownDiscrepancies.load_discrepancies documentation
        :return: Returns a Hash {} of "acceptable" and "unacceptable" discrepancies that were found.
        """
        self.source_report = report1
        self.report2 = report2
        self.load_discrepancies(discrepancy_array)
        self.remove_missing()
        self.load_reports(self.source_report, self.report2)
        self.evaluate()
        print(Back.BLACK + Fore.LIGHTWHITE_EX + str(self.discrepancies_found) + Back.RESET + Fore.RESET)


thing = KnownDiscrepancies()
