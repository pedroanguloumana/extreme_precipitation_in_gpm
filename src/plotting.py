import pandas as pd
import xarray as xr
from src.configs import *

def load_pf_stats(region):
    file = merged_pf_stats_file(region)
    df = pd.read_csv(
        file, 
        index_col=0
    )
    return df

def load_era5_eofs(region):
    file = f'{project_root_dir()}/data/{region}.massflux_EOFs.nc'
    return xr.open_dataarray(file)

def load_era5_pcs(region):
    file = f'{project_root_dir()}/data/{region}.massflux_PCs.nc'
    return xr.open_dataarray(file)

def load_pf_crh(region, radius=5):
     file = f'{project_root_dir()}/data/{region}.tropical_pf_crh_data_{radius}deg.csv'
     return pd.read_csv(file)

def load_cmorph_daily():
    file = f'{project_root_dir()}/data/merged.cmorph.daily_precip.nc'
    return xr.open_dataset(file).cmorph