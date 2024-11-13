import xarray as xr

def load_cmorph_daily():
    file = '/Users/pedro/extreme_precipitation_in_gpm/data/mean.merged.cmorph.daily_precip.nc'
    return xr.open_dataset(file).cmorph