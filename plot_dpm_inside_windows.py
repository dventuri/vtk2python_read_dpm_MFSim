import numpy as np
import matplotlib.pyplot as plt

xs, dpm_count = np.loadtxt("./dpm_inside_recap.txt",
                           dtype=float,
                           skiprows=0,
                           delimiter=' ',
                           unpack=True)

fig, ax = plt.subplots()
ax.set_xlabel('Posição [m]')
ax.set_ylabel('DPMs')
ax.axis([0.0, 14, 90000, 135000])
ax.xaxis.set_major_locator(plt.MultipleLocator(1))
ax.xaxis.set_minor_locator(plt.MultipleLocator(0.5))
ax.yaxis.set_major_locator(plt.MultipleLocator(5000))
ax.yaxis.set_minor_locator(plt.MultipleLocator(2500))
ax.scatter(xs, dpm_count,
           s=25,
           c='white',
           marker='o',
           edgecolors='black',
           linewidths=1,
           label='RECAP')
ax.grid(color='gray',ls=':')
ax.legend(loc='lower right')
fig.tight_layout(pad=0.01)
# plt.savefig('./milena_30m/figures/temperature_ts.png',
#             dpi=1200,
#             format='png')

xs, dpm_count = np.loadtxt("./dpm_mass_inside_recap_old.txt",
                           dtype=float,
                           skiprows=0,
                           delimiter=' ',
                           unpack=True)

fig, ax = plt.subplots()
ax.set_xlabel('Posição [m]')
ax.set_ylabel('Massa de gotas [kg]')
# ax.axis([0.0, 14, 90000, 135000])
# ax.xaxis.set_major_locator(plt.MultipleLocator(1))
# ax.xaxis.set_minor_locator(plt.MultipleLocator(0.5))
# ax.yaxis.set_major_locator(plt.MultipleLocator(5000))
# ax.yaxis.set_minor_locator(plt.MultipleLocator(2500))
ax.scatter(xs, dpm_count,
           s=25,
           c='white',
           marker='o',
           edgecolors='black',
           linewidths=1,
           label='RECAP')
ax.grid(color='gray',ls=':')
ax.legend(loc='lower right')
fig.tight_layout(pad=0.01)

fig, ax = plt.subplots()
ax.set_xlabel('Posição [m]')
ax.set_ylabel('Fração de líquido [-]')
# ax.axis([0.0, 14, 90000, 135000])
# ax.xaxis.set_major_locator(plt.MultipleLocator(1))
# ax.xaxis.set_minor_locator(plt.MultipleLocator(0.5))
# ax.yaxis.set_major_locator(plt.MultipleLocator(5000))
# ax.yaxis.set_minor_locator(plt.MultipleLocator(2500))
vol = 1*(24-2*0.375)*0.0254
ax.scatter(xs, dpm_count/(vol*2.3),
           s=25,
           c='white',
           marker='o',
           edgecolors='black',
           linewidths=1,
           label='RECAP')
ax.grid(color='gray',ls=':')
ax.legend(loc='lower right')
fig.tight_layout(pad=0.01)



xs1, dpm_mass = np.loadtxt("./dpm_mass_inside_repar.txt",
                           dtype=float,
                           skiprows=0,
                           delimiter=' ',
                           unpack=True)

xs2, dpm_mass_40 = np.loadtxt("./dpm_mass_inside_repar_UL_40.txt",
                           dtype=float,
                           skiprows=0,
                           delimiter=' ',
                           unpack=True)

fig, ax = plt.subplots()
ax.set_xlabel('Posição [m]')
ax.set_ylabel('Fração de líquido [-]')
# ax.axis([0.0, 14, 90000, 135000])
# ax.xaxis.set_major_locator(plt.MultipleLocator(1))
# ax.xaxis.set_minor_locator(plt.MultipleLocator(0.5))
# ax.yaxis.set_major_locator(plt.MultipleLocator(5000))
# ax.yaxis.set_minor_locator(plt.MultipleLocator(2500))
vol = 1*(26-2*0.375)*0.0254
# ax.scatter(xs1, dpm_mass/(vol*2.3),
#            s=25,
#            c='white',
#            marker='o',
#            edgecolors='black',
#            linewidths=1,
#            label='REPAR')
ax.scatter(xs2, dpm_mass_40/(vol*2.3),
           s=25,
           c='white',
           marker='s',
           edgecolors='black',
           linewidths=1,
           label='REPAR UL 40')
ax.grid(color='gray',ls=':')
ax.legend(loc='best')
fig.tight_layout(pad=0.01)
