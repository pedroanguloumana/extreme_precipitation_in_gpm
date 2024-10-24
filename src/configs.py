 
def project_root_dir():
    return "/Users/pedro/extreme_precipitation_in_gpm"

def data_dir(filename=''):
    return (project_root_dir() + f'/data/{filename}')

def merged_pf_stats_file(region):
    return project_root_dir() + f'/data/gpm_pf_stats.{region}.merged.csv'

def merged_era5_var_file(var=''):
    file = project_root_dir() + f'/data/era5.merged.daily_{var}.nc'
    return file

