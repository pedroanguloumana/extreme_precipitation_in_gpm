import matplotlib.pyplot as plt
import matplotlib.colors as colors
import numpy as np
def array_midpoints(x):
    return (x[1:] + x[:-1])/2

def save_figure(fig, filename):
    path_to_save = f'/Users/pedro/extreme_precipitation_in_gpm/figures/{filename}.pdf'
    fig.savefig(path_to_save, format='pdf', bbox_inches='tight')

def make_discrete_cmap(cmap='Blues', N=20):
    """
    Turn any continuous colormap into a ListedColormap with N discrete steps.
    `cmap` can be a string or a Colormap object.
    """
    base = plt.get_cmap(cmap) if isinstance(cmap, str) else cmap
    return colors.ListedColormap(base(np.linspace(0, 1, N)), name=f"{base.name}_{N}")

