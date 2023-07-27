import glob
import re
import pyvista as pv    #https://docs.pyvista.org/version/stable/user-guide/simple.html
import numpy as np
import matplotlib.pyplot as plt

#make sure a dpm from a timestep is not
#present in the next one

# filenames
base_dir = "/home/dventuri/run/canal_30m/output/dpm/pvtp/vtp"
base_fname = f"{base_dir}/dpm_*_*.vtp"
timestep_treshold = 60000

# 'x' cutoff position
x_cut = 29.9    # meters

### function - sort numerically
def numericalSort(value):
    numbers = re.compile(r'(\d+)')  #regex to match any repeating numerical Unicode character
    parts = numbers.split(value)    #splits the string using "numbers"
    parts = map(int, parts[1::2])   #returns only the numbers converted to ints
    return tuple(parts)

### function - compare timesteps
def timestep_above(value, threshold):
    parts = numericalSort(value)
    return parts[-2] >= threshold   #uses second to last number (last is partition number)

# generate list o filenames to read (numerically sorted and only above timestep threshold)
fnames = sorted(glob.glob(base_fname), key=numericalSort)   #sorts the list of names using the converted numbers
fnames = [fname for fname in fnames if timestep_above(fname, timestep_treshold)]

# start iterating on files
dpm_diam_all = []
for fname in fnames:
    # read vtp data
    dpm = pv.read(fname)

    # cehck if x_max < x_cutoff
    if (dpm.bounds[1] < x_cut): continue

    # print filename
    print('\nReading file ', fname)

    # what are the mesh bounds?
    print('Bounds: ', dpm.bounds)

    # how many points are in this mesh
    print('Total points in file: ', dpm.n_points)

    # access a point data array inside de vtk
    dpm_diam = dpm.point_data['dpm_diameter']
    if (dpm_diam.size != dpm.n_points):
        raise ValueError("Wrong number of points for diameter point data")

    # access dpm x position
    dpm_x = dpm.points[:,0]
    if (dpm_x.size != dpm.n_points):
        raise ValueError("Wrong number of points for position point data")

    # filter only values at (x > x_cutoff)
    filter_arr = dpm_x > x_cut
    dpm_diam_filtered = dpm_diam[filter_arr]
    print('Points after filtering: ', dpm_diam_filtered.size)
    dpm_diam_all.append(dpm_diam_filtered)


# consolidate complete vector
dpm_diam_all = np.hstack(dpm_diam_all)
print('\nTotal points: ', dpm_diam_all.size)

#https://matplotlib.org/stable/gallery/statistics/hist.html
#https://matplotlib.org/stable/gallery/statistics/histogram_cumulative.html#sphx-glr-gallery-statistics-histogram-cumulative-py
fig, ax = plt.subplots(tight_layout=True)
ax.hist(dpm_diam_all, bins=20)
# ax.hist(dpm_diam_all, bins=10, cumulative=True, histtype='step')
ax.set_xlabel('Droplet diameter (m)')
ax.set_ylabel('Likelihood of occurrence')
# ax.set_xscale('log')
