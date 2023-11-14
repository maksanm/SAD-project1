from os import path
import pandas as pd


class DataLoader:
    def __init__(self, data_path):
        self.unrate_adjusted_df = pd.read_csv(path.join(data_path, 'unrate_adjusted.csv'))
        self.unrate_adjusted_df.columns = ['Date', 'Period', 'Rate']
        self.unrate_adjusted_df['Date'] = pd.to_datetime(self.unrate_adjusted_df['Date'])

        self.unrate_unadjusted_df = pd.read_csv(path.join(data_path, 'unrate_unadjusted.csv'))
        self.unrate_unadjusted_df.columns = ['Date', 'Period', 'Rate']
        self.unrate_unadjusted_df['Date'] = pd.to_datetime(self.unrate_unadjusted_df['Date'])