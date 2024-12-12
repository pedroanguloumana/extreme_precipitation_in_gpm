import matplotlib.pyplot as plt
import xarray as xr

def array_midpoints(x):
    return (x[1:] + x[:-1])/2

def save_figure(fig, filename):
    path_to_save = f'/Users/pedro/extreme_precipitation_in_gpm/figures/{filename}.pdf'
    fig.savefig(path_to_save, format='pdf')

def load_example_pf():
    file = '/Users/pedro/extreme_precipitation_in_gpm/data/pf_082.GPM2Ku7_uw4_20150321.182456_to_20150321.183647_006023_CIO.nc'
    return xr.open_dataset(file)