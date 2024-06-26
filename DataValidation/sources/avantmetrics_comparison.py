# !#/bin/python3 

import json
import asyncio
import copy
import json
import subprocess
import traceback
import os
import re
import sys
import sources
import http3
import copy

from compare_reports import Comparison

configs = json.load(open('../config.json'))


class AvantMetricsComparison:
    report_name = ''
    reports = []
    prepared_col_map = {}
    performance_report_request_objects = {}
    edw2_url = 'https://picker-dev.avantlink.com/rpt?timeout=2800000'
    edw3_url = 'https://picker-shard.avantlink.com/rpt?timeout=2800000'


    def __init__(self, report_name, reports):
        self.report_name = report_name
        self.reports = reports
        with open('./sources/json_sources/avm_performance_request_objects.json') as f:
            self.performance_report_request_objects = json.load(f)
    
    @staticmethod
    def __convert_date_range_for_classic__(date_range):
        # Convert the date range to the format that the classic system expects
        # Give the date range in the format of "MM/DD/YYYY - MM/DD/YYYY"
        # return a 6 part tuple of the format (start_day, start_month, start_year, end_day, end_month, end_year)
        start_date, end_date = date_range.split(' - ')
        start_month, start_day, start_year = start_date.split('/')
        end_month, end_day, end_year = end_date.split('/')
        return (start_day, start_month, start_year, end_day, end_month, end_year)

    @staticmethod
    def search_merchant(environment, merchant_name=None, merch_id=None):
        if environment.lower() == 'EDW2'.lower() or environment.lower() == 'EDW3'.lower():
            merchant_map = json.load(open('./sources/json_sources/merchant_map.json'))
            # Remove "_ from merchant passed as argument"
            if merchant_name:
                if "_" in merchant_name:
                    merchant_name = merchant_name.replace("_", " ")
                for merchant_id in merchant_map:
                    if merchant_map[merchant_id][0]["merchant_name"].lower() == merchant_name.lower():
                        return merchant_id, merchant_map[merchant_id][1]["merchant_network"]
            if merch_id:
                return merchant_map[merch_id][0]["merchant_name"], merchant_map[merch_id][1]["merchant_network"]

    @staticmethod
    def replace_merchant(ro, merchant_id, environment):
        if environment.lower() == 'EDW2'.lower() or environment.lower() == 'EDW3'.lower():
            for report_id in ro:
                for filter in ro[report_id]["filters"]:
                    if filter["field"] == "dim_merchant-merchant_uuid":
                        new_filter = {
                            "field": "dim_merchant-merchant_uuid",
                            "op": "eq",
                            "values": [
                                f"{merchant_id}"
                            ],
                            "alias": "merchant_filter1"
                        }
                        del filter
                        ro[report_id]["filters"].append(new_filter)

    def fetch_csv_report(self, location):
            csv_report = sources.CSVReport(location)
            csv_report.load()
            self.reports.append(csv_report)
            return csv_report.data

    async def get_prepared_cols(self):
        client = http3.AsyncClient()
        headers = {
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            # 'Accept-Encoding': 'gzip, deflate, br',
            'user_id': configs["root_user_id"],
            'tz': 'America/Denver',
            'fmonth': 'jan',
            'currency': 'USD',
            'default_currency': 'USD',
        }

        # Catch timeouts from the API here
        try:
            response = await client.get('https://picker-shard.avantlink.com/prepared_cols', headers=headers, timeout=3000000)
        except http3.exceptions.ReadTimeout:
            self.timeout = True
            return
        self.prepared_col_map = response.json()
        return response

    def __retrieve_request_object__(self, type, report_name, environment):
        if type == 'performance':
            return self.performance_report_request_objects[environment.lower()][report_name]
         

    def insert_edw2_avantmetrics_request_filters(self, request_object):
        # Inject filters for "Multiple Affilliates != 'N/A'" and "Is Affiliate Order == 'Yes'"
        report_key = request_object.keys()[0]
        true = True
        filters = [{
               "op":"eq",
               "field":"is_affiliate_order",
               "values":[
                  "Yes"
               ],
               "case_insensitive":true
            },
            {
               "op":"ne",
               "field":"has_multiple_affiliates",
               "values":[
                  "N/A"
               ],
               "case_insensitive":true
            }]
        
        new_request_object = copy.deepcopy(request_object)
        new_request_object[report_key]['filters'].append(filters)
        return new_request_object

    async def fetch_classic_report(self, report_id, date_range, **kwargs):
        date_begin, date_end = date_range.split(' - ')
        classic_report = sources.ClassicReport(report_id, begin=date_begin, end=date_end, **kwargs)
        return await classic_report.request()

    async def fetch_picker_report(self, request_object, environment):
        if environment == 'EDW2':
            picker_url = self.edw2_url
        elif environment == 'EDW3':
            picker_url = self.edw3_url
        picker_report = sources.PickerReport(
            picker_url = picker_url,
            report_name = self.report_name,
            request_object = request_object,
            request_type = environment.lower()
        )
        await picker_report.load()
        self.reports.append(picker_report)

        
        return picker_report
    
    async def async_comparison_wrapper(self, request_object, name):
        comparison = Comparison(
            sources.PickerReport(picker_url=self.edw3_url,
                                 report_name=name,
                                 request_object=request_object,
                                 request_type='edw3')
        )

        test_result = await comparison.run_and_barf()
        return test_result

    def compare_reports(self):
        # Compare the performance_reports
        pass

    def compare_website_order_details(self):
        # Compare the website order details
        pass

    def compare_referral_group_order_details(self):
        # Compare the referral group order details
        pass


async def main():
    comparison = AvantMetricsComparison(report_name="Referral Group Order Details", reports=[])
    report_id = 8
    date_range = "11/01/2023 - 11/02/2023"
    merchant_id = 10008
    edw3_report_location =    'file://./sources/json_sources/EDW3_RGOD_Nov2023_CampSaver_com.csv'
    edw2_report_location =    'file://./sources/json_sources/EDW2_RGOD_Nov2023_CampSaver_com.csv'
    classic_report_location = 'file://./sources/json_sources/Classic_RGOD_Nov2023_CampSaver_com.csv'
    # comparison.fetch_csv_report(edw3_report_location, 'edw3')
    # comparison.fetch_csv_report(edw2_report_location, 'edw2')
    # comparison.fetch_csv_report(classic_report_location, 'classic')


    for report in comparison.reports:
        print(report.report_environment)
        print(len(report.data))
        # print(report.data)
    report_data = await comparison.fetch_classic_report(report_id, date_range, mi=merchant_id)
    # print(report_data)
    edw3_env = 'EDW3'
    edw3_request_object = comparison.__retrieve_request_object__('performance', 'Referral Group Order Details', edw3_env)
    edw3_picker_report_data = await comparison.async_comparison_wrapper(edw3_request_object, 'Referral Group Order Details')
    print(edw3_picker_report_data.data)

if __name__ == '__main__':
    asyncio.run(main())