import re

from sources.mixin_fetch import MixinFetch
from args import args
import pandas


class SourceBase(MixinFetch):

    report_name = None
    pd = None
    data = None
    columns = None
    df: pandas.DataFrame
    orphans: pandas.DataFrame
    packed_dims: pandas.DataFrame
    dimensions = None
    dim_types = None
    report_name = None
    facts = None

    def __init__(self, columns=None, dims=[], report_name=None, **kwargs):
        self.columns = columns
        self.dimensions = dims
        self.report_name = report_name
        self.args = args

        # Add in args from kwargs
        for (k, v) in kwargs.items():
            setattr(self, k, v)

    def safe_name(self, dirty_name):
        g = re.search(r"([^/.]+)(\.[^/]+)", dirty_name)
        if g is None:
            return 'unnamed_report'
        name = g.group(1)
        return re.sub(r"[^a-zA-Z_\-0-9]+", '_', name)

    def load(self):
        raise NotImplementedError("load is not meant to be called directly. Please call this method from a child class.")

    def __maybe_headerify_dims(self):
        self.dim_types = list(set([type(x) for x in self.data.columns.values[self.dimensions]]))
        if len(self.dimensions) == 0:
            # no dimensions
            return
        if len(self.dim_types) > 1:
            raise Exception("Mixed types provided for dimension names. ")
        if self.dim_types[0] == int:
            for idx in range(len(self.dimensions)):
                self.dimensions[idx] = str(self.data.columns.values[idx])
        else:
            for idx in range(len(self.dimensions)):
                self.dimensions[idx] = str(self.data.columns.values[self.dimensions[idx]])

    def pack_dims(self):
        self.__maybe_headerify_dims()
        self.packed_dims = pandas.DataFrame(columns=['col0'], index=range(self.data.shape[0]))
        if len(self.dim_types) == 0:
            return
        self.packed_dims.loc[:, 'col0'] = self.data[self.dimensions[0]].copy()
        for idx in range(1, len(self.dimensions)):
            self.packed_dims.loc[:, 'col0'] = self.packed_dims['col0'] + '||' + self.data[self.dimensions[idx]]
        self.list_facts() #@TODO: Ask Adam Where to put this call to self.list_facts()

    def list_facts(self):
        facts = []
        for col_idx in range(0, len(self.data.columns)):
            if self.data.columns[col_idx] not in self.dimensions:
                facts.append(self.data.columns[col_idx])
        self.facts = facts
# what are packed_dims - since this is just 1 report
# - when Pack dims match between 2 reports - this validates the row index matching


# what is the list resulted from self.dimensions
