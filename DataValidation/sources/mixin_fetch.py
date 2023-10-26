import re
import requests
import boto3
# If you get an error on the following line, make sure you're using Python 3.6 or newer.
from io import StringIO
import csv

class MixinFetch(object):
    """
        We should be able to access any file from any http, s3 or local location.
        The file type should be interpreted so the requesting method can properly interpret the file
    """

    def fetch_to_arrays(self, location):
        contents = self.fetch_to_string(location)
        ext = location.split('.')[-1:][0]
        if ext == 'csv':
            return self.interpret_csv(contents)
        if ext == 'tsv':
            return self.interpret_csv(contents, delimiter='\t')
        # TODO: parquet, excel, any others?

    def fetch_to_string(self, location):
        g = re.search(r"^[^:]+(?=:\/\/)", location)
        if g is not None:
            # Has a protocol!
            proto = g.group(0)
            if proto == 'file':
                print("using __file")
                return self.__file(location)
            if proto == 's3':
                print('using __s3')
                return self.__s3(location)
            if proto == 'http' or proto == 'https':
                print('using __http(s)')
                return self.__http(location)
        else:
            raise Exception('Unable to parse file path: %(location)s\n'
                            'hint: if this is on the local file system, '
                            'try specifying this by prefixing it with file://' % {'location': location})

    def __file(self, location):
        location = location.replace('file://', '')
        with open(location, 'r') as f:
            return f.read()

    def __s3(self, location):
        # Note: this presumes that you have aws set up on your machine
        # (role, credentials file, environment.json variable, etc)
        # You will get an error if this is not configured.

        g = re.search(r'^[^:]+:\/\/([^/]+)(.*)', location)
        key = g.group(2)
        bucket = g.group(1)
        client = boto3.client('s3')
        r = client.Object(bucket, key)
        return r.get()["Body"].read()

    def __http(self, location):
        r = requests.get(location)
        return r.text

    def interpret_csv(self, csv_as_string, delimiter=',', has_headers=True):
        f = StringIO(csv_as_string)
        reader = csv.reader(f, delimiter=delimiter)
        data = [row for row in reader]
        headers = None
        if has_headers:
            headers = data.pop(0)
        return headers, data
