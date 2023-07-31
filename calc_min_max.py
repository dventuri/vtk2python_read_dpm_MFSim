import glob
import re
import pyvista as pv    #https://docs.pyvista.org/version/stable/user-guide/simple.html
import numpy as np

#make sure a dpm from a timestep is not
#present in the next one

# filenames
base_dir = "/home/dventuri/run/mmvillar/canal30m_ewf/output/dpm/pvtp/vtp"
base_fname = f"{base_dir}/dpm_*_000.vtp"
timestep_treshold = 0
n_procs = 120

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
IB_radius = 0.3207
global_u_min = 1e40
global_u_max = 0
for fname in fnames:

    ts_u_min = 1e40
    ts_u_max = 0
    for proc in range(n_procs):

        # read vtp data
        new_fname = fname[:name_size-7]+str(proc).zfill(3)+".vtp"
        dpm = pv.read(new_fname)

        # print filename
        print('\nReading file ', new_fname)

        # access a point data array inside de vtk
        try:
            dpm_u = dpm.point_data['dpm_u']
        except:
            print('Empty file')
            continue

        # check for possible size error
        if (dpm_u.size != dpm.n_points):
            raise ValueError("Wrong number of points for velocity point data")

        # filter droplets outside the IB
        if (dpm.points.shape[0] != dpm.n_points):
            raise ValueError("Wrong number of points for position point data")

        r_pos = np.linalg.norm(dpm.points[:,1:] - 0.5, axis=1)
        filter_arr = r_pos <= IB_radius

        dpm_u_filtered = dpm_u[filter_arr]
        print('Points after filtering: ', dpm_u_filtered.size)

        # get timestep max and min values
        tmp_max = np.max(dpm_u_filtered)
        tmp_min = np.min(dpm_u_filtered)
        if(tmp_min < ts_u_min): ts_u_min = tmp_min
        if(tmp_max > ts_u_max): ts_u_max = tmp_max

    # print values
    print('')
    print('Timestep minimum velocity is: ', ts_u_min)
    print('Timestep maximum velocity is: ', ts_u_max)

    ### save data
    print("Saving data")
    with open('dpm_u_max_min.txt','a') as f:
        f.write(f"{fname[-15:-8]} {ts_u_min} {ts_u_max}\n")

    # get global max and min values
    if(ts_u_min < global_u_min): global_u_min = ts_u_min
    if(ts_u_max > global_u_max): global_u_max = ts_u_max

    # print values
    print('')
    print('New minimum velocity value is: ', global_u_min)
    print('New maximum velocity value is: ', global_u_max)
