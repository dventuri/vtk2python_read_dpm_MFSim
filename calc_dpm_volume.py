import glob
import re
import pyvista as pv    #https://docs.pyvista.org/version/stable/user-guide/simple.html
import numpy as np

# filenames
base_dir = "/home/dventuri/run/evap_shear_test/case01/output/dpm/pvtp/vtp"
base_fname = f"{base_dir}/dpm_*_000.vtp"
timestep_treshold = 0
n_procs = 8

# physical properties
dpm_rho = 980     #kg/m³

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
            dpm_diam = dpm.point_data['dpm_diameter']
        except:
            print('Empty file')
            continue

        # calculate timestep mass flow
        dpm_volume = (np.pi*dpm_diam**3)/6
        dpm_mass_flow += np.sum(dpm_volume*dpm_rho)

    ### save data
    print("Saving data")
    with open('dpm_mass.txt','a') as f:
        f.write(f"{fname[-15:-8]} {dpm_mass_flow}\n")
