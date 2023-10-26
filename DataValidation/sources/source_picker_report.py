import json
import os

import http3
import numpy as np
import pandas as pd
import requests
from sources import constants
from sources.base import SourceBase

path = os.getcwd()
configs = json.load(open('../config.json'))


class PickerReport(SourceBase):
    constants = constants.PickerConstants()
    picker_url: str
    auth: str
    request_object: dict
    gathered_headers: list
    user_id: str
    filters: list
    tz = ''
    fmonth = ''
    currency = ''
    default_currency = ''
    error = None
    report = None
    report_name = None
    sql_query = None
    order_number = None
    report_key = 'none'

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        for constant in [attr for attr in dir(self.constants) if
                         not callable(getattr(self.constants, attr)) and not attr.startswith('__')]:
            setattr(self, constant, kwargs.get(constant, getattr(self.constants, constant)))
        # Header Properties
        self.report = None
        self.order_number = None
        # TODO: add support for restricted pickers

        # If no error, check if we should use currency
        # If not, it's fine to force it USD
        if self.args.no_error is True and self.args.native is False:
            self.currency = 'USD'

        # For edw2, force the merchant network to come from the merchant_map
        # This is required because edw2 doesn't support native currency
        if self.request_type == 'edw2':
            self.currency = self.merchant_network + 'D'

    def reset(self):
        # Set all constants
        for constant in [attr for attr in dir(self.constants) if
                         not callable(getattr(self.constants, attr)) and not attr.startswith('__')]:
            setattr(self, constant, getattr(self.constants, constant))
        # Now set all values not represented by constants
        self.request_object = {}
        self.report_name = 'default'
        self.report_key = 'none'
        self.error = None
        self.filters = []

    def __get_headers(self):
        return {
            "user_id": self.user_id,
            "tz": self.tz,
            "fmonth": self.fmonth,
            "currency": self.currency,
            "default_currency": self.default_currency,
        }



    def __gather_headers(self):
        self.gathered_headers = []
        ro_key = ''
        for key in self.request_object:
            ro_key = key
        ro = self.request_object[ro_key]
        # print(f"\n {self.request_object} 71 source picker report")
        for col_obj in ro["cols"]:
            for prop in col_obj:
                if prop == "name":
                    self.gathered_headers.append(col_obj[prop])
        return self.gathered_headers

    async def load(self):
        """
        Return the report that is sent back from the picker. Takes no input.
        """
        client = http3.AsyncClient()
        if self.request_object == {}:
            raise AttributeError("Use Picker_Report.request_object_gen(params) to generate a request object first")
            # Post a request object to Picker 1.0
        data_request = await client.post(self.picker_url, data={
            "q": json.dumps(self.request_object)
        }, headers=self.__get_headers(), verify=False, timeout=2900000)
        self.report = data_request.json()
        self.report_key = [x for x in list(self.report.keys()) if x[0] != '_'][0]
        col_data = []
        if self.report_name is None:
            self.report_name = self.report_key
        self.report_key = [x for x in list(self.report.keys()) if x[0] != '_'][0]
        while 'request_id' in self.report[self.report_key]:
            data_request = await client.get(
                self.picker_url[:-3] + 'nag/' + self.report[self.report_key]['request_id'],
                headers=self.__get_headers(), verify=False)
            res = data_request.json()
            if "_queries" in res:
                self.sql_query = res["_queries"]
                pass
            else:
                self.sql_query = "No Query Returned"
            if 'request_id' in res:
                continue
            if 'file' in res:
                data_request = await client.get(res['file'])
                self.report[self.report_key] = data_request.json()
        if self.report_name is None:
            self.report_name = self.safe_name(self.report_key)
        if 'data' not in self.report[self.report_key][0]:
            self.__gather_headers()
            for header in self.gathered_headers:
                col_data.append('No Data Was Found')
            print('** No Data Error', self.report_key, self.picker_url)
            # print(json.dumps(self.request_object), '\n')
            self.error = self.report[self.report_key]
            self.report_name = self.report_name + '_EMPTY_'
        else:
            self.dimensions = self.report[self.report_key][0]['dims']
            columns = self.report[self.report_key][0]['headers']
            self.data = pd.DataFrame(np.array(self.report[self.report_key][0]['data']),
                                     columns=self.columns or columns)
