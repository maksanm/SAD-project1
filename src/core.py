from os import path
import pandas as pd
import datetime as dt


class DataLoader:
    def __init__(self, data_path):
        df = pd.read_csv(path.join(data_path, 'unrate_adjusted.csv'))
        df.columns = ['CollectionDate', 'Period', 'Rate']
        df['CollectionDate'] = pd.to_datetime(df['CollectionDate'])
        df = df[(df['CollectionDate'] > dt.datetime(1997, 1, 1)) & (df['CollectionDate'] < dt.datetime(2023, 10, 1))]
        self.unrate_adjusted_df = df

        if path.exists(path.join(data_path, 'unrate_unadjusted.csv')):
            df = pd.read_csv(path.join(data_path, 'unrate_unadjusted.csv'))
            df.columns = ['CollectionDate', 'Period', 'Rate']
            df['CollectionDate'] = pd.to_datetime(df['CollectionDate'])
            df = df[(df['CollectionDate'] > dt.datetime(1997, 1, 1)) & (df['CollectionDate'] < dt.datetime(2023, 10, 1))]
            self.unrate_unadjusted_df = df