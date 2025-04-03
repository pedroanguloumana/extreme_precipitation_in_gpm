import matplotlib.pyplot as plt
import xarray as xr

def array_midpoints(x):
    return (x[1:] + x[:-1])/2

def save_figure(fig, filename):
    path_to_save = f'/Users/pedro/extreme_precipitation_in_gpm/figures/{filename}.pdf'
    fig.savefig(path_to_save, format='pdf', bbox_inches='tight')

