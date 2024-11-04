# some functions for handling the TRMM data, on 2x2 grids
import xarray as xr
from glob import glob
def load_region_var(region_name, var):
    path = f'/Users/pedro/trmm_v07_processed/{region_name}/{var}/GPMTRMMv7*.2.00x2.00.{var}.nc'
    return xr.concat([xr.open_dataset(_) for _ in sorted(glob(path))], dim='scenes')