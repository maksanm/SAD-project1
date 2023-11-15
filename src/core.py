from os import path
import pandas as pd
import datetime as dt


class DataLoader:
    def __init__(self, data_path):
        self.unrate_adjusted_df = self.get_unrate_df_from_csv(data_path, 'unrate_adjusted.csv')
        self.unrate_unadjusted_df = self.get_unrate_df_from_csv(data_path, 'unrate_unadjusted.csv')
        self.unrate_unadjusted_male_df = self.get_unrate_df_from_csv(data_path, 'unrate_unadjusted_male.csv')
        self.unrate_unadjusted_female_df = self.get_unrate_df_from_csv(data_path, 'unrate_unadjusted_female.csv')

    def get_unrate_df_from_csv(self, data_path, file_name) -> pd.DataFrame:
        if path.exists(path.join(data_path, file_name)):
            df = pd.read_csv(path.join(data_path, file_name))
            df.columns = ['CollectionDate', 'Period', 'Rate']
            df['CollectionDate'] = pd.to_datetime(df['CollectionDate'])
            df = df[(df['CollectionDate'] > dt.datetime(1997, 1, 1)) & (df['CollectionDate'] < dt.datetime(2023, 10, 1))]
            return df
        else:
            return None