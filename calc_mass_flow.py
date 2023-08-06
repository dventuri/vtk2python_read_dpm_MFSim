import glob
import re
import pyvista as pv    #https://docs.pyvista.org/version/stable/user-guide/simple.html
import numpy as np

# filenames
base_dir = "/home/dventuri/run/mmvillar/canal30m_ewf/output/dpm/pvtp/vtp"
base_fname = f"{base_dir}/dpm_*_000.vtp"
timestep_treshold = 0
n_procs = 120

# geometric parameters
x_cut = 29.9
L = 30 - x_cut
# L = x_cut - 0
IB_radius = 0.3207

# physical properties
dpm_rho = 998.2     #kg/m³

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
for fname in fnames:

    dpm_mass_flow = 0
    for proc in range(n_procs):

        # read vtp data
        new_fname = fname[:name_size-7]+str(proc).zfill(3)+".vtp"
        dpm = pv.read(new_fname)

        # print filename
        print('\nReading file ', new_fname)

        # access a point data array inside de vtk
        try:
            dpm_u = dpm.point_data['dpm_u']
            dpm_diam = dpm.point_data['dpm_diameter']
        except:
            print('Empty file')
            continue

        # check for possible size error
        if (dpm_u.size != dpm.n_points):
            raise ValueError("Wrong number of points for velocity point data")

        if (dpm_u.size != dpm.n_points):
            raise ValueError("Wrong number of points for velocity point data")

        if (dpm.points.shape[0] != dpm.n_points):
            raise ValueError("Wrong number of points for position point data")

        # filter droplets before x_cut
        dpm_x = dpm.points[:,0]
        filter_arr1 = dpm_x > x_cut
        dpm_points_filtered = dpm.points[filter_arr1]

        # filter droplets outside the IB
        r_pos = np.linalg.norm(dpm_points_filtered[:,1:] - 0.5, axis=1)
        filter_arr2 = r_pos <= IB_radius

        # apply filters
        dpm_u_filtered = dpm_u[filter_arr1]
        dpm_u_filtered = dpm_u_filtered[filter_arr2]

        dpm_diam_filtered = dpm_diam[filter_arr1]
        dpm_diam_filtered = dpm_diam_filtered[filter_arr2]

        print('Points after filtering: ', dpm_u_filtered.size)
        if(dpm_u_filtered.size < 1): continue

        # calculate timestep mass flow
        dpm_volume = (np.pi*dpm_diam_filtered**3)/6
        dpm_mass_flow += np.sum(dpm_u_filtered*dpm_volume*dpm_rho/L)

    ### save data
    print("Saving data")
    with open('dpm_mass_flow.txt','a') as f:
        f.write(f"{fname[-15:-8]} {dpm_mass_flow}\n")
