# This contains classes for all of the data sources
# This will include attributes like what columns to blakclist for the validation run

# This is a global of valid sources to check against
# Note that empty is allowed here for routine data validation
valid_sources = ['', 'fact_redshift', 'fact_postgres', 'olap', 'cube_postgres', 'athena']

class DataSource():

    def __init__(
            self,
            source='',
            blacklist = []
    ):
        '''
        Parameters:
            source: str, gives the string identifier of the source data (e.g. fact_redshift)
            blacklist: list, gives all of the columns we do NOT want to run on this source
            We might not want to run a column if the data contained within it is not available
            in the data source. A good example of this is ROAS in Redshift because Redshift
            does not have silo data
        '''
        self.blacklist = blacklist
        self.source = source

        # Check the source for being valid
        if self.source not in valid_sources:
            valid_string = ', '.join(valid_sources)
            raise TypeError(f'The given source is not valid. Must be in {valid_string} but got {self.source}')

class RedshiftDataSource(DataSource):
    source = 'fact_redshift'
    blacklist = ['ROAS']

    def __init__(self):
        super().__init__(
            source = self.source,
            blacklist = self.blacklist
        )

# NOTE: None of these are really implemented at this point but could have specific blacklists added
class PostgresDataSource(DataSource):
    pass

class OLAPDataSource(DataSource):
    pass

class AthenaDataSource(DataSource):
    pass