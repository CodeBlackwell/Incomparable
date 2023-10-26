from sources import constants
import http3
from datetime import datetime, timedelta
import urllib
import pandas as pd
import numpy as np

from sources.base import SourceBase


class ClassicReport(SourceBase):
    constant = constants.PickerConstants()
    url = ''
    module = {}
    report_id = None
    begin = 0
    end = 0
    params = {}

    def __init__(self, report_id, begin=0, end=0, columns=None, **kwargs):
        super().__init__(columns=columns, **kwargs)
        self.url = self.constant.classic_url
        self.module = self.constant.module
        self.report_id = report_id
        self.begin = (self.yesterday(), begin)[begin]
        self.end = (self.today(), end)[end]
        self.params = kwargs


    @staticmethod
    def today():
        return datetime.today().strftime('%Y-%m-%d')

    @staticmethod
    def yesterday():
        yesterday = datetime.today() - timedelta(1)
        return yesterday.strftime('%Y-%m-%d')

    async def request(self):
        client = http3.AsyncClient()
        query_string = self.url
        # If you get an error on the following line, make sure you are using Python 3.6 or newer.
        params = {**self.params,
            "auth_key": self.constant.auth,
            "module": self.module,
            "report_id": self.report_id,
            "output": 'csv',
            "date_begin": self.begin,
            "date_end": self.end
        }
        query_string = query_string + urllib.parse.urlencode(params)
        r = await client.get(query_string)
        headers, data = self.interpret_csv(r.text)

        data = np.array(data)
        self.data = pd.DataFrame(data, columns=headers)