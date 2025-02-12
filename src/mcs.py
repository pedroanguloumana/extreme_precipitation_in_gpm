import xarray as xr
def load_mcs():
    file = '/Users/pedro/Datasets/Feng_etal_Global_MCS/tracks/mcs_tracks_final_extc_20150101.0000_20160101.0000.nc'
    ds = xr.open_dataset(file)
    return ds