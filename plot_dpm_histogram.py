import numpy as np
import matplotlib.pyplot as plt

dpm_diam_all = np.loadtxt('dpm_diam_caso10.txt')

#https://matplotlib.org/stable/gallery/statistics/hist.html
#https://matplotlib.org/stable/gallery/statistics/histogram_cumulative.html#sphx-glr-gallery-statistics-histogram-cumulative-py
fig, ax = plt.subplots(tight_layout=True)
plt.xscale('log')
ax.hist(dpm_diam_all, bins=500)
# ax.hist(dpm_diam_all, bins=10, cumulative=True, histtype='step')
ax.set_xlabel('Droplet diameter (m)')
ax.set_ylabel('Likelihood of occurrence')
# ax.set_xlim(0,1e-4)
