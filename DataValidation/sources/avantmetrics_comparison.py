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

from compare_reports import Comparison

configs = json.load(open('../config.json'))


class AvantMetricsComparison:
    report_name = ''
    reports = []
    prepared_col_map = {}
    edw2_url = 'https://picker-dev.avantlink.com/rpt?timeout=2800000'
    edw3_url = 'https://picker-shard.avantlink.com/rpt?timeout=2800000'


    def __init__(self, report_name, reports):
        self.report_name = report_name
        self.reports = reports
        self.performance_report_request_objects = json.load(open('./sources/json_sources/avm_performance_request_objects.json'))

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
    def adjust_dates():
        # Adjust the dates of EDW2 or EDW3 reports
        pass

    def convert_edw2_avantmetrics_request(self, request, report_name):
        # Convert the request to the format that AvantMetrics API expects
        pass

    async def fetch_classic_report2(self, report_id, date_range, **kwargs):
        date_begin, date_end = date_range.split(' - ')
        classic_report = sources.ClassicReport(report_id, begin=date_begin, end=date_end, **kwargs)
        return await classic_report.request()

    async def fetch_classic_report(self,
            report_id,
            date_range,
            merchant_id,
            merchant_parent="0",
            merchant_group="0",
            custom_tracking_code="",
            search_affiliates="All Affiliates"
    ):
        RSD, RSM, RSY, RED, REM, REY = self.__convert_date_range_for_classic__(date_range)
        params = {
            "mp":merchant_parent,
            "mi":merchant_id, #10008
            "cmg":merchant_group,
            "r":report_id, #8
            "search_affiliates":search_affiliates,
            "p":"0",
            "cpg":"0",
            "d":"",
            "rsd":{
                "F":RSM,
                "d":RSD,
                "Y":RSY
                },
            "red":{
                "F":REM,
                "d":RED,
                "Y":REY
                },
                "ctc":custom_tracking_code,
                "go":"Select Report"
            }
        classic_request = sources.ClassicReport(params)
        return await classic_request.request()

    def fetch_picker_report(self, request, picker_version="EDW3"):
        # Fetch the report from the EDW3 system
        pass

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
            response = await client.get('https://picker-shard.avantlink.com/prepared_cols', headers=headers, timeout=30)
        except http3.exceptions.ReadTimeout:
            self.timeout = True
            return
        self.prepared_col_map = response.json()
        return response


    def compare_reports(self):
        # Compare the * reports
        pass

    def compare_website_order_details(self):
        # Compare the website order details
        pass

    def compare_referral_group_order_details(self):
        # Compare the referral group order details
        pass


async def main():
    comparison = AvantMetricsComparison(report_name="Your Report Name", reports=[])
    report_id = 8
    date_range = "11/01/2024 - 11/30/2024"
    merchant_id = 10008
    report_data = await comparison.fetch_classic_report2(report_id, date_range, mi=merchant_id)
    print(report_data)

if __name__ == '__main__':
    asyncio.run(main())