from glob import glob
import xarray as xr
import pandas as pd
import numpy as np

def get_radar_files(region):
    path = f'/Users/pedro/extreme_precipitation_in_gpm/data/precipitation_feature_database/{region.name}/gpm_pf_radar_profiles.{region.name}*.nc'
    files = sorted(glob(path))
    return files

def load_merged_radar(region, trim_region=True, maxpr_min=0):
    radar_files = [f for f in get_radar_files(region)]
    radar = xr.open_mfdataset(
        radar_files, 
        chunks='auto', 
        concat_dim='features', 
        combine='nested'
    )

    if trim_region:
        file = f'/Users/pedro/extreme_precipitation_in_gpm/data/precipitation_feature_database/merged/merged.gpm_pf_stats.{region.name}.csv'
        df = pd.read_csv(file, index_col=False) 
        assert df.shape[0]==radar.features.size
    
        region_mask = (df['mean_latitude']<=region.lat_north)
        region_mask = region_mask & (df['mean_latitude']>=region.lat_south)
        region_mask = region_mask & (df['mean_longitude']<=region.lon_east)
        region_mask = region_mask & (df['mean_longitude']>=region.lon_west)

        # only get features
        radar = radar.isel(features=np.where(region_mask)[0])

        
    return radar