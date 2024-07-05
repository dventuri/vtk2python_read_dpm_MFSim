import glob
import re
import pyvista as pv    #https://docs.pyvista.org/version/stable/user-guide/simple.html
import numpy as np

#make sure a dpm from a timestep is not
#present in the next one

# filenames
base_dir = "/home/dventuri/run/recap_14m_10p/output/dpm/pvtp/vtp"
base_fname = f"{base_dir}/dpm_*_000.vtp"
timestep_treshold = 0
n_procs = 28

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
name_size = len(fnames[0])

# choosing only last time-step
fname = fnames[-1]

# window size and num of steps
win_size = 1        # meter
step_size = 0.25    # meters
x_mins = np.arange(0, 14-win_size+step_size, step_size)
for x_min in x_mins:

    dpm_inside = 0
    for proc in range(n_procs):

        # read vtp data
        new_fname = fname[:name_size-7]+str(proc).zfill(3)+".vtp"
        dpm = pv.read(new_fname)

        # print filename
        print('\nReading file ', new_fname)

        # how many points are in this mesh
        print('Total points in file: ', dpm.n_points)
        if(dpm.n_points < 1):
            print("Skipping file")
            continue

        # filter droplets outside the IB
        if (dpm.points.shape[0] != dpm.n_points):
            raise ValueError("Wrong number of points for position point data")

        # x_max position
        x_max = x_min + win_size

        # filter
        x_pos = dpm.points[:,0]
        filter_arr = np.logical_and(x_pos >= x_min, x_pos < x_max)

        dpm_points_filtered = dpm.points[filter_arr]

        dpm_inside += np.count_nonzero(filter_arr)

        print('Points after filtering: ', np.count_nonzero(filter_arr))

    ### save data
    x = (x_max + x_min)/2
    print("Saving data")
    with open('dpm_inside_recap.txt','a') as f:
        f.write(f"{x} {dpm_inside}\n")
