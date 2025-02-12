from glob import glob

def get_radar_files(region):
    path = f'/Users/pedro/extreme_precipitation_in_gpm/data/precipitation_feature_database/gpm_pf_radar_profiles.{region.name}*.nc'
    files = sorted(glob(path))
    return files
