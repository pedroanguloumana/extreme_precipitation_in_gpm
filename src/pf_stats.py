import pandas as pd
from src.regions import Region

def load_pf_stats(region, trim_region=True, just_tropics=True, maxpr_min=0):
    file = f'/Users/pedro/extreme_precipitation_in_gpm/data/precipitation_feature_database/merged/merged.gpm_pf_stats.{region.name}.csv'
    df = pd.read_csv(file, index_col=False)
    if trim_region:
        # select the region
        region_mask = (df['mean_latitude']<=region.lat_north)
        region_mask = region_mask & (df['mean_latitude']>=region.lat_south)
        region_mask = region_mask & (df['mean_longitude']<=region.lon_east)
        region_mask = region_mask & (df['mean_longitude']>=region.lon_west)
        df = df[region_mask]

    if just_tropics:
        tropics_mask = abs(df['mean_latitude']) <=30
        df = df[tropics_mask]
        
    df = df[df['max_precip']>maxpr_min]
    return df

def load_feb_pf_stats(region, trim_region=True, just_tropics=True, maxpr_min=0):
    file = f'/Users/pedro/extreme_precipitation_in_gpm/data/precipitation_feature_database/merged/merged.gpm_pf_stats.{region.name}.csv'
    df = pd.read_csv(file, index_col=False)
    times = pd.DatetimeIndex(pd.to_datetime(df['observation_time'], format='%Y%m%d_%H:%M:%S'))
    df = df[times.month==2]

    if trim_region:
        # select the region
        region_mask = (df['mean_latitude']<=region.lat_north)
        region_mask = region_mask & (df['mean_latitude']>=region.lat_south)
        region_mask = region_mask & (df['mean_longitude']<=region.lon_east)
        region_mask = region_mask & (df['mean_longitude']>=region.lon_west)
        df = df[region_mask]

    if just_tropics:
        tropics_mask = abs(df['mean_latitude']) <=30
        df = df[tropics_mask]
        
    df = df[df['max_precip']>maxpr_min]
    return df