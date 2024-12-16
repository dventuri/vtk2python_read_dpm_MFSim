import glob
import re
import pyvista as pv    #https://docs.pyvista.org/version/stable/user-guide/simple.html
import numpy as np

#make sure a dpm from a timestep is not
#present in the next one

parcel = 10
length = 14
# length = 30

# window size and num of steps
win_size = 0.2     # meter
step_size = 0.1    # meters

# filenames
base_dir = "/home/dventuri/run/recap_14m_keps_np10_coll_coal_ssd_atmzrepar/output/dpm/pvtp/vtp"
# base_dir = "/home/dventuri/run/repar_30m_keps_np10_coll_coal_ssd_atmz/output/dpm/pvtp/vtp"
base_fname = f"{base_dir}/dpm_*_000.vtp"
timestep_treshold = 0
n_procs = 28
# n_procs = 30

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

x_mins = np.arange(0, length-win_size+step_size, step_size)
for x_min in x_mins:

    mass_inside = 0
    diams = np.zeros(0)
    us = np.zeros(0)
    temps = np.zeros(0)
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

        dpm_diams = dpm.point_data['dpm_diameter'][filter_arr]
        mass = parcel*np.pi/6*dpm_diams**3*980
        mass_inside += np.sum(mass)
        diams = np.concatenate((diams,dpm_diams))
        mean_diameter = np.average(diams)

        dpm_us = dpm.point_data['dpm_u'][filter_arr]
        us = np.concatenate((us,dpm_us))
        mean_u = np.average(us)

        dpm_temps = dpm.point_data['dpm_temp'][filter_arr]
        temps = np.concatenate((temps,dpm_temps))
        mean_temp = np.average(temps)

        print('Points after filtering: ', np.count_nonzero(filter_arr))

    ### save data recap
    x = (x_max + x_min)/2
    print("Saving data")
    with open('recap_14m_keps_np10_coll_coal_ssd_atmzrepar/recap_mass.txt','a') as f:
        f.write(f"{x} {mass_inside}\n")
    with open('recap_14m_keps_np10_coll_coal_ssd_atmzrepar/recap_diam.txt','a') as f:
        f.write(f"{x} {mean_diameter}\n")
    with open('recap_14m_keps_np10_coll_coal_ssd_atmzrepar/recap_u.txt','a') as f:
        f.write(f"{x} {mean_u}\n")
    with open('recap_14m_keps_np10_coll_coal_ssd_atmzrepar/recap_temp.txt','a') as f:
        f.write(f"{x} {mean_temp}\n")

    ### save data repar
    # x = (x_max + x_min)/2
    # print("Saving data")
    # with open('repar_30m_keps_np10_coll_coal_ssd_atmz/repar_mass.txt','a') as f:
    #     f.write(f"{x} {mass_inside}\n")
    # with open('repar_30m_keps_np10_coll_coal_ssd_atmz/repar_diam.txt','a') as f:
    #     f.write(f"{x} {mean_diameter}\n")
    # with open('repar_30m_keps_np10_coll_coal_ssd_atmz/repar_u.txt','a') as f:
    #     f.write(f"{x} {mean_u}\n")
    # with open('repar_30m_keps_np10_coll_coal_ssd_atmz/repar_temp.txt','a') as f:
    #     f.write(f"{x} {mean_temp}\n")
