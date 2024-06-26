# before running in cluster use: ml gnu/13.2.0 python/3.11.4

import glob
import re
import pyvista as pv    #https://docs.pyvista.org/version/stable/user-guide/simple.html
import numpy as np

# filenames
base_dir = "/home/dventuri/run/evap_kurose/case01_1dpm/output/dpm/pvtp/vtp"
base_fname = f"{base_dir}/dpm_*_000.vtp"
timestep_treshold = 0
n_procs = 8
time_step = 1E-04

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

# generate list of filenames to read (numerically sorted and only above timestep threshold)
fnames = sorted(glob.glob(base_fname), key=numericalSort)   #sorts the list of names using the converted numbers
fnames = [fname for fname in fnames if timestep_above(fname, timestep_treshold)]

# generate list of timesteps following fnames (to calculate time)
timesteps = []
for i in range(len(fnames)):
    timesteps.append(numericalSort(fnames[i])[2])

# start iterating on files
name_size = len(fnames[0])
for fname, ts in zip(fnames, timesteps):

    for proc in range(n_procs):

        # read vtp data
        new_fname = fname[:name_size-7]+str(proc).zfill(3)+".vtp"
        dpm = pv.read(new_fname)

        # print filename
        print('\nReading file ', new_fname)

        # access a point data array inside de vtk
        try:
            dpm_diam = dpm.point_data['dpm_diameter']
            dpm_T = dpm.point_data['dpm_temp']
        except:
            print('Empty file')
            continue

    ### save data
    print("Saving data")
    with open('dpm_diameter_kurose.txt','a') as f:
        f.write(f"{ts*time_step} {dpm_diam[0]}\n")
    with open('dpm_temperature_kurose.txt','a') as f:
        f.write(f"{ts*time_step} {dpm_T[0]}\n")
