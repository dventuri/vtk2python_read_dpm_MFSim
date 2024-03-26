import glob
import re
import pyvista as pv    #https://docs.pyvista.org/version/stable/user-guide/simple.html
import numpy as np

#make sure a dpm from a timestep is not
#present in the next one

# filenames
base_dir = "/home/dventuri/run/jmvedovoto/spraysingle/caso10/output/dpm/pvtp/vtp"
base_fname = f"{base_dir}/dpm_*_*.vtp"
timestep_treshold = 20000

# geometric parameters
x_cut = 0.0    # meters
IB_radius = 10

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

    # print filename
    print('\nReading file ', fname)

    # access a point data array inside de vtk
    try:
        dpm_diam = dpm.point_data['dpm_diameter']
    except:
        print('Empty file')
        continue

    # check for possible size error
    if (dpm_diam.size != dpm.n_points):
        raise ValueError("Wrong number of points for diameter point data")

    if (dpm.points.shape[0] != dpm.n_points):
        raise ValueError("Wrong number of points for position point data")

    # how many points are in this mesh
    print('Total points in file: ', dpm.n_points)

    # filter droplets before x_cut
    dpm_x = dpm.points[:,0]
    filter_arr1 = dpm_x > x_cut
    dpm_points_filtered = dpm.points[filter_arr1]

    # filter droplets outside the IB
    r_pos = np.linalg.norm(dpm_points_filtered[:,1:] - 0.5, axis=1)
    filter_arr2 = r_pos <= IB_radius

    # apply filters
    dpm_diam_filtered = dpm_diam[filter_arr1]
    dpm_diam_filtered = dpm_diam_filtered[filter_arr2]
    print('Points after filtering: ', dpm_diam_filtered.size)
    dpm_diam_all.append(dpm_diam_filtered)

# consolidate complete vector
dpm_diam_all = np.hstack(dpm_diam_all)
print('\nTotal points: ', dpm_diam_all.size)

# save array to file
np.savetxt('dpm_diam_caso10.txt', dpm_diam_all)
