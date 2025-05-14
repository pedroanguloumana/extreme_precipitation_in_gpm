import pandas as pd
from glob import glob

def gsam_feature_database():
    path = f'/Users/pedro/extreme_precipitation_in_gpm/data/gsam_pf_data_may7aa.csv'
    df = pd.read_csv(path, index_col=0).reset_index(drop=True)
    return df

