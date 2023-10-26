
# This generates the merchant_map json file give a downloaded csv file
# TODO: Would be nice to eventually build the csv itself on a cron

import json
import os
import pandas as pd

if __name__ == '__main__':
    # Put in file and path here
    fid = 'merchant_map.csv'

    # Import to df, output columns
    df = pd.read_csv(fid, index_col=False)
    columns = (list(df.columns))

    # Load into dict
    data_dict = {}
    for index, row in df.iterrows():
        data_dict[row['merchant_uuid']] = [{'merchant_name': row['merchant_name']}, {'merchant_network': row['merchant_network']}]

    # Save dict to file
    js_dict = json.dumps(data_dict)
    with open('merchant_map.json', 'w+') as f:
        f.write(js_dict)