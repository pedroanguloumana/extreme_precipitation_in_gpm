import xarray as xr
from glob import glob

def region_core_files(region_name):
    path = f'/Users/pedro/extreme_precipitation_in_gpm/data/gsam_cores/{region_name}*.nc'
    file_list = sorted(glob(path))
    return file_list