import pandas as pd
import xarray as xr
import numpy as np
from src.configs import *

def load_pf_stats(region):
    file = merged_pf_stats_file(region)
    df = pd.read_csv(file, index_col=0)
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

def load_pf_pc(region, radius=5):
     file = f'{project_root_dir()}/data/{region}.tropical_pf_pc_data_{radius}deg.csv'
     return pd.read_csv(file)

def load_cmorph_daily():
    file = f'{project_root_dir()}/data/merged.cmorph.daily_precip.nc'
    return xr.open_dataset(file).cmorph

def label_xaxis_theta(ax):
    # Set x-axis ticks and labels
    tick_positions = np.arange(-7*np.pi/8, 7*np.pi/8 + np.pi/8, np.pi/4)
    tick_labels = [r'$-\dfrac{7\pi}{8}$',
                r'$-\dfrac{5\pi}{8}$',
                r'$-\dfrac{3\pi}{8}$',
                r'$-\dfrac{\pi}{8}$',
                r'$\dfrac{\pi}{8}$',
                r'$\dfrac{3\pi}{8}$',
                r'$\dfrac{5\pi}{8}$',
                r'$\dfrac{7\pi}{8}$']
    ax.set_xticks(tick_positions)
    ax.set_xticklabels(tick_labels)
    ax.set_xlim(-7*np.pi/8, 7*np.pi/8)
    return ax