import numpy as np
import matplotlib.pyplot as plt

ts, dpm_count = np.loadtxt("./dpm_inside.txt",
                           dtype=float,
                           skiprows=0,
                           delimiter=' ',
                           unpack=True)

plt.style.use('singleColumn.mplstyle')
fig, ax = plt.subplots()
ax.set_xlabel('Time-step number')
ax.set_ylabel('Number of DPMs')
# ax.axis([0.0, 70000, 416.75, 418.1])
# ax.xaxis.set_major_locator(plt.MultipleLocator(10000))
# ax.xaxis.set_minor_locator(plt.MultipleLocator(5000))
# ax.yaxis.set_major_locator(plt.MultipleLocator(.25))
# ax.yaxis.set_minor_locator(plt.MultipleLocator(.125))
ax.scatter(ts, dpm_count,
           s=25,
           c='white',
           marker='o',
           edgecolors='black',
           linewidths='1')
fig.tight_layout(pad=0.01)
# plt.savefig('./milena_30m/figures/temperature_ts.png',
#             dpi=1200,
#             format='png')
