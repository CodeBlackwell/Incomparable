from sources.base import SourceBase
import pandas as pd
import numpy as np


class CSVReport(SourceBase):
    report_name = None
    report_location: None

    def __init__(self, location, **kwargs):
        super().__init__(**kwargs)
        self.reset()
        if self.report_name is None:
            self.report_name = self.safe_name(location)
        self.report_location = location

    def reset(self):
        self.report_name = ''
        self.report_location = None

    def load(self):
        headers, data = self.fetch_to_arrays(self.report_location)
        data = np.array(data)
        self.data = pd.DataFrame(data, columns=headers)
