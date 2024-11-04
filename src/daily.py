# Functions for handiling daily data, including ERA5 and CMORPH
import xarray as xr
def load_merged_cmorph_daily():
    file = '/Users/pedro/extreme_precipitation_in_gpm/data/remapped.merged.cmorph.daily_precip.nc'
    ds = xr.open_dataset(file).cmorph
    ds['time'] = ds['time'].dt.floor('D')
    return ds

def load_merged_era5_daily_crh():
    file = '/Users/pedro/extreme_precipitation_in_gpm/data/era5.merged.daily_crh.nc'
    ds = xr.open_dataarray(file)
    ds['time'] = ds['time'].dt.floor('D')
    return ds

