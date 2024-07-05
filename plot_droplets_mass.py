import numpy as np
import matplotlib.pyplot as plt


xs1, dpm_mass1 = np.loadtxt("./recap_14m_10p_old.txt",
                           dtype=float,
                           skiprows=0,
                           delimiter=' ',
                           unpack=True)
xs2, dpm_mass2 = np.loadtxt("./recap_14m_10p.txt",
                           dtype=float,
                           skiprows=0,
                           delimiter=' ',
                           unpack=True)

fig, ax = plt.subplots()
ax.set_xlabel('Comprimento [m]')
ax.set_ylabel('Fração de líquido [-]')
ax.axis([0.0, 14, 0, 0.2])
ax.xaxis.set_major_locator(plt.MultipleLocator(2))
ax.xaxis.set_minor_locator(plt.MultipleLocator(1))
ax.yaxis.set_major_locator(plt.MultipleLocator(0.05))
ax.yaxis.set_minor_locator(plt.MultipleLocator(0.025))
vol = 1*(24-2*0.375)*0.0254
ax.scatter(xs1, dpm_mass1/vol,
           s=25,
           c='white',
           marker='o',
           edgecolors='black',
           linewidths=1,
           label=r'RECAP $d_p \approx O(-4)$')
ax.scatter(xs2, dpm_mass2/vol,
           s=25,
           c='white',
           marker='s',
           edgecolors='black',
           linewidths=1,
           label=r'RECAP $d_p \approx O(-3)$')
ax.grid(color='gray',ls=':')
ax.legend(loc='best')
fig.tight_layout(pad=0.01)
plt.savefig('./recap_mass.png',
            dpi=1200,
            format='png')



xs1, dpm_mass1 = np.loadtxt("./repar_30m_mix_1p.txt",
                           dtype=float,
                           skiprows=0,
                           delimiter=' ',
                           unpack=True)
xs2, dpm_mass2 = np.loadtxt("./repar_30m_UL_40p.txt",
                           dtype=float,
                           skiprows=0,
                           delimiter=' ',
                           unpack=True)

fig, ax = plt.subplots()
ax.set_xlabel('Comprimento [m]')
ax.set_ylabel('Fração de líquido [-]')
ax.axis([0.0, 30, 0, 0.01])
ax.xaxis.set_major_locator(plt.MultipleLocator(5))
ax.xaxis.set_minor_locator(plt.MultipleLocator(2.5))
ax.yaxis.set_major_locator(plt.MultipleLocator(0.002))
ax.yaxis.set_minor_locator(plt.MultipleLocator(0.001))
vol = 1*(26-2*0.375)*0.0254
ax.scatter(xs1, dpm_mass1/(vol*2.3),
           s=25,
           c='white',
           marker='o',
           edgecolors='black',
           linewidths=1,
           label='REPAR 1p')
ax.grid(color='gray',ls=':')
ax.legend(loc='best')
fig.tight_layout(pad=0.01)
plt.savefig('./repar1_mass.png',
            dpi=1200,
            format='png')


fig, ax = plt.subplots()
ax.set_xlabel('Comprimento [m]')
ax.set_ylabel('Fração de líquido [-]')
ax.axis([0.0, 30, 0, 0.40])
ax.xaxis.set_major_locator(plt.MultipleLocator(5))
ax.xaxis.set_minor_locator(plt.MultipleLocator(2.5))
ax.yaxis.set_major_locator(plt.MultipleLocator(0.05))
ax.yaxis.set_minor_locator(plt.MultipleLocator(0.025))
vol = 1*(26-2*0.375)*0.0254
ax.scatter(xs1, dpm_mass1*40/(vol*2.3),
           s=25,
           c='white',
           marker='o',
           edgecolors='black',
           linewidths=1,
           label='REPAR 1p*40')
ax.scatter(xs2, dpm_mass2/(vol*2.3),
           s=25,
           c='white',
           marker='s',
           edgecolors='black',
           linewidths=1,
           label='REPAR 40p')
ax.grid(color='gray',ls=':')
ax.legend(loc='lower left')
fig.tight_layout(pad=0.01)
plt.savefig('./repar40_mass.png',
            dpi=1200,
            format='png')
