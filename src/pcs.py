import pandas as pd
from src.configs import data_dir

def init_pc_database_dict():
    database_dict = {'pc1': [], 'pc2': []}
    return database_dict
    
def load_pf_pc_database(region, radius_in_degs):
    file = data_dir(f'{region}.tropical_pf_pc_data_{int(radius_in_degs)}deg.csv')
    return pd.read_csv(file)