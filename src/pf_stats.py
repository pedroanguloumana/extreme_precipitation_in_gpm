import pandas as pd
from src.regions import Region

def load_pf_stats(region, trim_region=False):
    file = f'/Users/pedro/extreme_precipitation_in_gpm/data/monthly_pf_stats/merged.gpm_pf_stats.{region.name}.csv'
    df = pd.read_csv(file, index_col=False)
    if trim_region:
        # select the region
        region_mask = (df['mean_latitude']<=region.lat_north)
        region_mask = region_mask & (df['mean_latitude']>=region.lat_south)
        region_mask = region_mask & (df['mean_longitude']<=region.lon_east)
        region_mask = region_mask & (df['mean_longitude']>=region.lon_west)
        df = df[region_mask]
    return df