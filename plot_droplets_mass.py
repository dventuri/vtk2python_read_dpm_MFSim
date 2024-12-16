import numpy as np
import matplotlib.pyplot as plt

import locale
locale.setlocale(locale.LC_NUMERIC, "pt_BR.UTF-8")

plt.rcdefaults()
plt.rcParams['axes.formatter.use_locale'] = True


# xs1, dpm_mass1 = np.loadtxt("./recap_14m_10p_old.txt",
#                            dtype=float,
#                            skiprows=0,
#                            delimiter=' ',
#                            unpack=True)
# xs2, dpm_mass2 = np.loadtxt("./recap_14m_10p.txt",
#                            dtype=float,
#                            skiprows=0,
#                            delimiter=' ',
#                            unpack=True)

# fig, ax = plt.subplots()
# ax.set_xlabel('Comprimento [m]')
# ax.set_ylabel('Fração de líquido [-]')
# ax.axis([0.0, 14, 0, 0.2])
# ax.xaxis.set_major_locator(plt.MultipleLocator(2))
# ax.xaxis.set_minor_locator(plt.MultipleLocator(1))
# ax.yaxis.set_major_locator(plt.MultipleLocator(0.05))
# ax.yaxis.set_minor_locator(plt.MultipleLocator(0.025))
# vol = 1*(24-2*0.375)*0.0254
# ax.scatter(xs1, dpm_mass1/vol,
#            s=25,
#            c='white',
#            marker='o',
#            edgecolors='black',
#            linewidths=1,
#            label=r'RECAP $d_p \approx O(-4)$')
# ax.scatter(xs2, dpm_mass2/vol,
#            s=25,
#            c='white',
#            marker='s',
#            edgecolors='black',
#            linewidths=1,
#            label=r'RECAP $d_p \approx O(-3)$')
# ax.grid(color='gray',ls=':')
# ax.legend(loc='best')
# fig.tight_layout(pad=0.01)
# plt.savefig('./recap_mass.png',
#             dpi=1200,
#             format='png')



# xs1, dpm_mass1 = np.loadtxt("./repar_30m_mix_1p.txt",
#                            dtype=float,
#                            skiprows=0,
#                            delimiter=' ',
#                            unpack=True)
# xs2, dpm_mass2 = np.loadtxt("./repar_30m_UL_40p.txt",
#                            dtype=float,
#                            skiprows=0,
#                            delimiter=' ',
#                            unpack=True)

# fig, ax = plt.subplots()
# ax.set_xlabel('Comprimento [m]')
# ax.set_ylabel('Fração de líquido [-]')
# ax.axis([0.0, 30, 0, 0.01])
# ax.xaxis.set_major_locator(plt.MultipleLocator(5))
# ax.xaxis.set_minor_locator(plt.MultipleLocator(2.5))
# ax.yaxis.set_major_locator(plt.MultipleLocator(0.002))
# ax.yaxis.set_minor_locator(plt.MultipleLocator(0.001))
# vol = 1*(26-2*0.375)*0.0254
# ax.scatter(xs1, dpm_mass1/(vol*2.3),
#            s=25,
#            c='white',
#            marker='o',
#            edgecolors='black',
#            linewidths=1,
#            label='REPAR 1p')
# ax.grid(color='gray',ls=':')
# ax.legend(loc='best')
# fig.tight_layout(pad=0.01)
# plt.savefig('./repar1_mass.png',
#             dpi=1200,
#             format='png')


# fig, ax = plt.subplots()
# ax.set_xlabel('Comprimento [m]')
# ax.set_ylabel('Fração de líquido [-]')
# ax.axis([0.0, 30, 0, 0.40])
# ax.xaxis.set_major_locator(plt.MultipleLocator(5))
# ax.xaxis.set_minor_locator(plt.MultipleLocator(2.5))
# ax.yaxis.set_major_locator(plt.MultipleLocator(0.05))
# ax.yaxis.set_minor_locator(plt.MultipleLocator(0.025))
# vol = 1*(26-2*0.375)*0.0254
# ax.scatter(xs1, dpm_mass1*40/(vol*2.3),
#            s=25,
#            c='white',
#            marker='o',
#            edgecolors='black',
#            linewidths=1,
#            label='REPAR 1p*40')
# ax.scatter(xs2, dpm_mass2/(vol*2.3),
#            s=25,
#            c='white',
#            marker='s',
#            edgecolors='black',
#            linewidths=1,
#            label='REPAR 40p')
# ax.grid(color='gray',ls=':')
# ax.legend(loc='lower left')
# fig.tight_layout(pad=0.01)
# plt.savefig('./repar40_mass.png',
#             dpi=1200,
#             format='png')



# xs1, dpm_mass1 = np.loadtxt("./canal_teste_dpms_medias.txt",
#                            dtype=float,
#                            skiprows=0,
#                            delimiter=' ',
#                            unpack=True)

# fig, ax = plt.subplots()
# ax.set_xlabel('Comprimento [m]')
# ax.set_ylabel('Fração de líquido [-]')
# ax.axis([0, 1, 0, 0.01])
# ax.xaxis.set_major_locator(plt.MultipleLocator(0.2))
# ax.xaxis.set_minor_locator(plt.MultipleLocator(0.1))
# ax.yaxis.set_major_locator(plt.MultipleLocator(0.001))
# ax.yaxis.set_minor_locator(plt.MultipleLocator(0.0005))
# ax.scatter(xs1, dpm_mass1/(1*0.1*0.1*2.3),
#            s=25,
#            c='white',
#            marker='o',
#            edgecolors='black',
#            linewidths=1,
#            label='Canal teste')
# ax.grid(color='gray',ls=':')
# ax.legend(loc='best')
# fig.tight_layout(pad=0.01)
# plt.savefig('./canal_teste_mass.png',
#             dpi=1200,
#             format='png')


# xs1, dpm_mass1 = np.loadtxt("./recap_mass.txt",
#                            dtype=float,
#                            skiprows=0,
#                            delimiter=' ',
#                            unpack=True)
# xs2, dpm_mass2 = np.loadtxt("./recap_mass_cons.txt",
#                            dtype=float,
#                            skiprows=0,
#                            delimiter=' ',
#                            unpack=True)
# xs3, dpm_mass3 = np.loadtxt("./recap_mass_dt.txt",
#                            dtype=float,
#                            skiprows=0,
#                            delimiter=' ',
#                            unpack=True)
# xs4, dpm_mass4 = np.loadtxt("./recap_mass_dtdpm.txt",
#                            dtype=float,
#                            skiprows=0,
#                            delimiter=' ',
#                            unpack=True)

# fig, ax = plt.subplots()
# ax.set_xlabel('Comprimento [m]')
# ax.set_ylabel('Massa de gotas [kg]')
# ax.axis([0, 14, 0, 0.03])
# ax.xaxis.set_major_locator(plt.MultipleLocator(2))
# ax.xaxis.set_minor_locator(plt.MultipleLocator(1))
# ax.yaxis.set_major_locator(plt.MultipleLocator(0.005))
# ax.yaxis.set_minor_locator(plt.MultipleLocator(0.0025))
# ax.scatter(xs1, dpm_mass1,
#            s=25,
#            c='white',
#            marker='o',
#            edgecolors='black',
#            linewidths=1,
#            label='Caso padrão')
# ax.scatter(xs2, dpm_mass2,
#            s=25,
#            c='white',
#            marker='s',
#            edgecolors='black',
#            linewidths=1,
#            label='Conservativo')
# ax.scatter(xs3, dpm_mass3,
#            s=25,
#            c='white',
#            marker='*',
#            edgecolors='black',
#            linewidths=1,
#            label='Dt menor')
# ax.scatter(xs4, dpm_mass4,
#            s=25,
#            c='white',
#            marker='^',
#            edgecolors='black',
#            linewidths=1,
#            label='Dt_dpm menor')
# ax.grid(color='gray',ls=':')
# ax.legend(loc='best')
# fig.tight_layout(pad=0.01)
# # plt.savefig('./recap_mass.png',
# #             dpi=1200,
# #             format='png')


# fig, ax = plt.subplots()
# ax.set_xlabel('Comprimento [m]')
# ax.set_ylabel('Fração de líquido [-]')
# ax.axis([0, 14, 0, 0.25])
# ax.xaxis.set_major_locator(plt.MultipleLocator(2))
# ax.xaxis.set_minor_locator(plt.MultipleLocator(1))
# ax.yaxis.set_major_locator(plt.MultipleLocator(0.05))
# ax.yaxis.set_minor_locator(plt.MultipleLocator(0.025))
# ax.scatter(xs1, dpm_mass1/(np.pi*0.295275**2.*0.2*2.3),
#            s=25,
#            c='white',
#            marker='o',
#            edgecolors='black',
#            linewidths=1,
#            label='Caso padrão')
# ax.scatter(xs2, dpm_mass2/(np.pi*0.295275**2.*0.2*2.3),
#            s=25,
#            c='white',
#            marker='s',
#            edgecolors='black',
#            linewidths=1,
#            label='Conservativo')
# ax.scatter(xs3, dpm_mass3/(np.pi*0.295275**2.*0.2*2.3),
#            s=25,
#            c='white',
#            marker='*',
#            edgecolors='black',
#            linewidths=1,
#            label='Dt menor')
# ax.scatter(xs4, dpm_mass4/(np.pi*0.295275**2.*0.2*2.3),
#            s=25,
#            c='white',
#            marker='^',
#            edgecolors='black',
#            linewidths=1,
#            label='Dt_dpm menor')
# ax.grid(color='gray',ls=':')
# ax.legend(loc='best')
# fig.tight_layout(pad=0.01)
# # plt.savefig('./recap_mass.png',
# #             dpi=1200,
# #             format='png')


# xs1, dpm_diam1 = np.loadtxt("./recap_diam.txt",
#                            dtype=float,
#                            skiprows=0,
#                            delimiter=' ',
#                            unpack=True)
# xs2, dpm_diam2 = np.loadtxt("./recap_diam_cons.txt",
#                            dtype=float,
#                            skiprows=0,
#                            delimiter=' ',
#                            unpack=True)
# xs3, dpm_diam3 = np.loadtxt("./recap_diam_dt.txt",
#                            dtype=float,
#                            skiprows=0,
#                            delimiter=' ',
#                            unpack=True)
# xs4, dpm_diam4 = np.loadtxt("./recap_diam_dtdpm.txt",
#                            dtype=float,
#                            skiprows=0,
#                            delimiter=' ',
#                            unpack=True)

# fig, ax = plt.subplots()
# ax.set_xlabel('Comprimento [m]')
# ax.set_ylabel('Diâmetro médio [m]')
# ax.axis([0, 14, 0.00079, 0.00081])
# ax.xaxis.set_major_locator(plt.MultipleLocator(2))
# ax.xaxis.set_minor_locator(plt.MultipleLocator(1))
# ax.yaxis.set_major_locator(plt.MultipleLocator(0.000005))
# ax.yaxis.set_minor_locator(plt.MultipleLocator(0.0000025))
# ax.scatter(xs1, dpm_diam1,
#            s=25,
#            c='white',
#            marker='o',
#            edgecolors='black',
#            linewidths=1,
#            label='Caso padrão')
# ax.scatter(xs2, dpm_diam2,
#            s=25,
#            c='white',
#            marker='s',
#            edgecolors='black',
#            linewidths=1,
#            label='Conservativo')
# ax.scatter(xs3, dpm_diam3,
#            s=25,
#            c='white',
#            marker='*',
#            edgecolors='black',
#            linewidths=1,
#            label='Dt menor')
# ax.scatter(xs4, dpm_diam4,
#            s=25,
#            c='white',
#            marker='^',
#            edgecolors='black',
#            linewidths=1,
#            label='Dt_dpm menor')
# ax.grid(color='gray',ls=':')
# ax.legend(loc='best')
# fig.tight_layout(pad=0.01)
# # plt.savefig('./recap_diam.png',
# #             dpi=1200,
# #             format='png')


# xs1, dpm_u1 = np.loadtxt("./recap_u.txt",
#                            dtype=float,
#                            skiprows=0,
#                            delimiter=' ',
#                            unpack=True)
# xs2, dpm_u2 = np.loadtxt("./recap_u_cons.txt",
#                            dtype=float,
#                            skiprows=0,
#                            delimiter=' ',
#                            unpack=True)
# xs3, dpm_u3 = np.loadtxt("./recap_u_dt.txt",
#                            dtype=float,
#                            skiprows=0,
#                            delimiter=' ',
#                            unpack=True)
# xs4, dpm_u4 = np.loadtxt("./recap_u_dtdpm.txt",
#                            dtype=float,
#                            skiprows=0,
#                            delimiter=' ',
#                            unpack=True)

# fig, ax = plt.subplots()
# ax.set_xlabel('Comprimento [m]')
# ax.set_ylabel('Velocidade média (U) [m/s]')
# ax.axis([0, 14, 0, 30])
# ax.xaxis.set_major_locator(plt.MultipleLocator(2))
# ax.xaxis.set_minor_locator(plt.MultipleLocator(1))
# ax.yaxis.set_major_locator(plt.MultipleLocator(5))
# ax.yaxis.set_minor_locator(plt.MultipleLocator(2.5))
# ax.scatter(xs1, dpm_u1,
#            s=25,
#            c='white',
#            marker='o',
#            edgecolors='black',
#            linewidths=1,
#            label='Caso padrão')
# ax.scatter(xs2, dpm_u2,
#            s=25,
#            c='white',
#            marker='s',
#            edgecolors='black',
#            linewidths=1,
#            label='Conservativo')
# ax.scatter(xs3, dpm_u3,
#            s=25,
#            c='white',
#            marker='*',
#            edgecolors='black',
#            linewidths=1,
#            label='Dt menor')
# ax.scatter(xs4, dpm_u4,
#            s=25,
#            c='white',
#            marker='^',
#            edgecolors='black',
#            linewidths=1,
#            label='Dt_dpm menor')
# ax.grid(color='gray',ls=':')
# ax.legend(loc='best')
# fig.tight_layout(pad=0.01)
# # plt.savefig('./recap_u.png',
# #             dpi=1200,
# #             format='png')


# xs1, dpm_temp1 = np.loadtxt("./recap_temp.txt",
#                            dtype=float,
#                            skiprows=0,
#                            delimiter=' ',
#                            unpack=True)
# xs2, dpm_temp2 = np.loadtxt("./recap_temp_cons.txt",
#                            dtype=float,
#                            skiprows=0,
#                            delimiter=' ',
#                            unpack=True)
# xs3, dpm_temp3 = np.loadtxt("./recap_temp_dt.txt",
#                            dtype=float,
#                            skiprows=0,
#                            delimiter=' ',
#                            unpack=True)
# xs4, dpm_temp4 = np.loadtxt("./recap_temp_dtdpm.txt",
#                            dtype=float,
#                            skiprows=0,
#                            delimiter=' ',
#                            unpack=True)

# fig, ax = plt.subplots()
# ax.set_xlabel('Comprimento [m]')
# ax.set_ylabel('Temperatura média [K]')
# ax.axis([0, 14, 330, 350])
# ax.xaxis.set_major_locator(plt.MultipleLocator(2))
# ax.xaxis.set_minor_locator(plt.MultipleLocator(1))
# ax.yaxis.set_major_locator(plt.MultipleLocator(5))
# ax.yaxis.set_minor_locator(plt.MultipleLocator(2.5))
# ax.scatter(xs1, dpm_temp1,
#            s=25,
#            c='white',
#            marker='o',
#            edgecolors='black',
#            linewidths=1,
#            label='Caso padrão')
# ax.scatter(xs2, dpm_temp2,
#            s=25,
#            c='white',
#            marker='s',
#            edgecolors='black',
#            linewidths=1,
#            label='Conservativo')
# ax.scatter(xs3, dpm_temp3,
#            s=25,
#            c='white',
#            marker='*',
#            edgecolors='black',
#            linewidths=1,
#            label='Dt menor')
# ax.scatter(xs4, dpm_temp4,
#            s=25,
#            c='white',
#            marker='^',
#            edgecolors='black',
#            linewidths=1,
#            label='Dt_dpm menor')
# ax.grid(color='gray',ls=':')
# ax.legend(loc='best')
# fig.tight_layout(pad=0.01)
# # plt.savefig('./recap_temp.png',
# #             dpi=1200,
# #             format='png')






### RECAP ###

xs1, dpm_mass1 = np.loadtxt("recap_14m_keps_np10_coll_coal_ssd_atmzrepar/recap_mass.txt",
                           dtype=float,
                           skiprows=0,
                           delimiter=' ',
                           unpack=True)
fig, ax = plt.subplots()
ax.set_xlabel('Comprimento [m]')
ax.set_ylabel('Concentração de gotas [kg/m3]')
ax.axis([0, 14, 0, 0.75])
ax.xaxis.set_major_locator(plt.MultipleLocator(2))
ax.xaxis.set_minor_locator(plt.MultipleLocator(1))
ax.yaxis.set_major_locator(plt.MultipleLocator(0.15))
ax.yaxis.set_minor_locator(plt.MultipleLocator(0.075))
ax.scatter(xs1, dpm_mass1/(np.pi*0.295275**2.*0.2),
           s=25,
           c='white',
           marker='o',
           edgecolors='black',
           linewidths=1)
ax.grid(color='gray',ls=':')
fig.tight_layout(pad=0.01)
plt.savefig('recap_14m_keps_np10_coll_coal_ssd_atmzrepar/recap_conc.png',
            dpi=1200,
            format='png')


fig, ax = plt.subplots()
ax.set_xlabel('Comprimento [m]')
ax.set_ylabel('Fração mássica de líquido [%]')
ax.axis([0, 14, 0, 20])
ax.xaxis.set_major_locator(plt.MultipleLocator(2))
ax.xaxis.set_minor_locator(plt.MultipleLocator(1))
ax.yaxis.set_major_locator(plt.MultipleLocator(5))
ax.yaxis.set_minor_locator(plt.MultipleLocator(2.5))
ax.scatter(xs1, dpm_mass1/(np.pi*0.295275**2.*0.2*2.7 + dpm_mass1)*100,
           s=25,
           c='white',
           marker='o',
           edgecolors='black',
           linewidths=1)
ax.grid(color='gray',ls=':')
# ax.legend(loc='best')
fig.tight_layout(pad=0.01)
plt.savefig('recap_14m_keps_np10_coll_coal_ssd_atmzrepar/recap_liqmassfrac.png',
            dpi=1200,
            format='png')


fig, ax = plt.subplots()
ax.set_xlabel('Comprimento [m]')
ax.set_ylabel('Fração volumétrica de líquido [%]')
ax.axis([0, 14, 0, 0.07])
ax.xaxis.set_major_locator(plt.MultipleLocator(2))
ax.xaxis.set_minor_locator(plt.MultipleLocator(1))
ax.yaxis.set_major_locator(plt.MultipleLocator(0.005))
ax.yaxis.set_minor_locator(plt.MultipleLocator(0.0025))
ax.scatter(xs1, (dpm_mass1/980)/(np.pi*0.295275**2.*0.2)*100,
           s=25,
           c='white',
           marker='o',
           edgecolors='black',
           linewidths=1)
ax.grid(color='gray',ls=':')
# ax.legend(loc='best')
fig.tight_layout(pad=0.01)
plt.savefig('recap_14m_keps_np10_coll_coal_ssd_atmzrepar/recap_liqvolfrac.png',
            dpi=1200,
            format='png')


xs1, dpm_diam1 = np.loadtxt("recap_14m_keps_np10_coll_coal_ssd_atmzrepar/recap_diam.txt",
                           dtype=float,
                           skiprows=0,
                           delimiter=' ',
                           unpack=True)
fig, ax = plt.subplots()
ax.set_xlabel('Comprimento [m]')
ax.set_ylabel('Diâmetro das gotas [mm]')
ax.axis([0, 14, 0.0, 1.0])
ax.xaxis.set_major_locator(plt.MultipleLocator(2))
ax.xaxis.set_minor_locator(plt.MultipleLocator(1))
ax.yaxis.set_major_locator(plt.MultipleLocator(0.2))
ax.yaxis.set_minor_locator(plt.MultipleLocator(0.1))
ax.scatter(xs1, dpm_diam1*1000,
           s=25,
           c='white',
           marker='o',
           edgecolors='black',
           linewidths=1)
ax.grid(color='gray',ls=':')
# ax.legend(loc='best')
fig.tight_layout(pad=0.01)
plt.savefig('recap_14m_keps_np10_coll_coal_ssd_atmzrepar/recap_diam.png',
            dpi=1200,
            format='png')


xs1, dpm_u1 = np.loadtxt("recap_14m_keps_np10_coll_coal_ssd_atmzrepar/recap_u.txt",
                           dtype=float,
                           skiprows=0,
                           delimiter=' ',
                           unpack=True)
fig, ax = plt.subplots()
ax.set_xlabel('Comprimento [m]')
ax.set_ylabel('Velocidade axial das gotas [m/s]')
ax.axis([0, 14, 0, 30])
ax.xaxis.set_major_locator(plt.MultipleLocator(2))
ax.xaxis.set_minor_locator(plt.MultipleLocator(1))
ax.yaxis.set_major_locator(plt.MultipleLocator(5))
ax.yaxis.set_minor_locator(plt.MultipleLocator(2.5))
ax.scatter(xs1, dpm_u1,
           s=25,
           c='white',
           marker='o',
           edgecolors='black',
           linewidths=1)
ax.grid(color='gray',ls=':')
# ax.legend(loc='best')
fig.tight_layout(pad=0.01)
plt.savefig('recap_14m_keps_np10_coll_coal_ssd_atmzrepar/recap_u.png',
            dpi=1200,
            format='png')


xs1, dpm_temp1 = np.loadtxt("recap_14m_keps_np10_coll_coal_ssd_atmzrepar/recap_temp.txt",
                           dtype=float,
                           skiprows=0,
                           delimiter=' ',
                           unpack=True)
fig, ax = plt.subplots()
ax.set_xlabel('Comprimento [m]')
ax.set_ylabel('Temperatura das gotas [°C]')
ax.axis([0, 14, 60, 85])
ax.xaxis.set_major_locator(plt.MultipleLocator(2))
ax.xaxis.set_minor_locator(plt.MultipleLocator(1))
ax.yaxis.set_major_locator(plt.MultipleLocator(5))
ax.yaxis.set_minor_locator(plt.MultipleLocator(2.5))
ax.scatter(xs1, dpm_temp1-273.15,
           s=25,
           c='white',
           marker='o',
           edgecolors='black',
           linewidths=1)
ax.grid(color='gray',ls=':')
# ax.legend(loc='best')
fig.tight_layout(pad=0.01)
plt.savefig('recap_14m_keps_np10_coll_coal_ssd_atmzrepar/recap_temp.png',
            dpi=1200,
            format='png')


### REPAR ###

xs1, dpm_mass1 = np.loadtxt("repar_30m_keps_np10_coll_coal_ssd_atmz/repar_mass.txt",
                           dtype=float,
                           skiprows=0,
                           delimiter=' ',
                           unpack=True)
fig, ax = plt.subplots()
ax.set_xlabel('Comprimento [m]')
ax.set_ylabel('Concentração de gotas [kg/m3]')
ax.axis([0, 30, 0, 0.6])
ax.xaxis.set_major_locator(plt.MultipleLocator(5))
ax.xaxis.set_minor_locator(plt.MultipleLocator(2.5))
ax.yaxis.set_major_locator(plt.MultipleLocator(0.1))
ax.yaxis.set_minor_locator(plt.MultipleLocator(0.05))
ax.scatter(xs1, dpm_mass1/(np.pi*0.320675**2.*0.2),
           s=25,
           c='white',
           marker='o',
           edgecolors='black',
           linewidths=1)
ax.grid(color='gray',ls=':')
fig.tight_layout(pad=0.01)
plt.savefig('repar_30m_keps_np10_coll_coal_ssd_atmz/repar_conc.png',
            dpi=1200,
            format='png')


fig, ax = plt.subplots()
ax.set_xlabel('Comprimento [m]')
ax.set_ylabel('Fração mássica de líquido [%]')
ax.axis([0, 30, 0, 21])
ax.xaxis.set_major_locator(plt.MultipleLocator(5))
ax.xaxis.set_minor_locator(plt.MultipleLocator(2.5))
ax.yaxis.set_major_locator(plt.MultipleLocator(3))
ax.yaxis.set_minor_locator(plt.MultipleLocator(1.5))
ax.scatter(xs1, dpm_mass1/(np.pi*0.320675**2.*0.2*2.3 + dpm_mass1)*100,
           s=25,
           c='white',
           marker='o',
           edgecolors='black',
           linewidths=1)
ax.grid(color='gray',ls=':')
# ax.legend(loc='best')
fig.tight_layout(pad=0.01)
plt.savefig('repar_30m_keps_np10_coll_coal_ssd_atmz/repar_liqmassfrac.png',
            dpi=1200,
            format='png')


fig, ax = plt.subplots()
ax.set_xlabel('Comprimento [m]')
ax.set_ylabel('Fração volumétrica de líquido [%]')
ax.axis([0, 30, 0, 0.06])
ax.xaxis.set_major_locator(plt.MultipleLocator(5))
ax.xaxis.set_minor_locator(plt.MultipleLocator(2.5))
ax.yaxis.set_major_locator(plt.MultipleLocator(0.01))
ax.yaxis.set_minor_locator(plt.MultipleLocator(0.005))
ax.scatter(xs1, (dpm_mass1/980)/(np.pi*0.320675**2.*0.2)*100,
           s=25,
           c='white',
           marker='o',
           edgecolors='black',
           linewidths=1)
ax.grid(color='gray',ls=':')
# ax.legend(loc='best')
fig.tight_layout(pad=0.01)
plt.savefig('repar_30m_keps_np10_coll_coal_ssd_atmz/repar_liqvolfrac.png',
            dpi=1200,
            format='png')


xs1, dpm_diam1 = np.loadtxt("repar_30m_keps_np10_coll_coal_ssd_atmz/repar_diam.txt",
                           dtype=float,
                           skiprows=0,
                           delimiter=' ',
                           unpack=True)
fig, ax = plt.subplots()
ax.set_xlabel('Comprimento [m]')
ax.set_ylabel('Diâmetro das gotas [mm]')
ax.axis([0, 30, 0.0, 0.6])
ax.xaxis.set_major_locator(plt.MultipleLocator(5))
ax.xaxis.set_minor_locator(plt.MultipleLocator(2.5))
ax.yaxis.set_major_locator(plt.MultipleLocator(0.1))
ax.yaxis.set_minor_locator(plt.MultipleLocator(0.05))
ax.scatter(xs1, dpm_diam1*1000,
           s=25,
           c='white',
           marker='o',
           edgecolors='black',
           linewidths=1)
ax.grid(color='gray',ls=':')
# ax.legend(loc='best')
fig.tight_layout(pad=0.01)
plt.savefig('repar_30m_keps_np10_coll_coal_ssd_atmz/repar_diam.png',
            dpi=1200,
            format='png')


xs1, dpm_u1 = np.loadtxt("repar_30m_keps_np10_coll_coal_ssd_atmz/repar_u.txt",
                           dtype=float,
                           skiprows=0,
                           delimiter=' ',
                           unpack=True)
fig, ax = plt.subplots()
ax.set_xlabel('Comprimento [m]')
ax.set_ylabel('Velocidade axial das gotas [m/s]')
ax.axis([0, 30, 0, 30])
ax.xaxis.set_major_locator(plt.MultipleLocator(5))
ax.xaxis.set_minor_locator(plt.MultipleLocator(2.5))
ax.yaxis.set_major_locator(plt.MultipleLocator(5))
ax.yaxis.set_minor_locator(plt.MultipleLocator(2.5))
ax.scatter(xs1, dpm_u1,
           s=25,
           c='white',
           marker='o',
           edgecolors='black',
           linewidths=1)
ax.grid(color='gray',ls=':')
# ax.legend(loc='best')
fig.tight_layout(pad=0.01)
plt.savefig('repar_30m_keps_np10_coll_coal_ssd_atmz/repar_u.png',
            dpi=1200,
            format='png')


xs1, dpm_temp1 = np.loadtxt("repar_30m_keps_np10_coll_coal_ssd_atmz/repar_temp.txt",
                           dtype=float,
                           skiprows=0,
                           delimiter=' ',
                           unpack=True)
fig, ax = plt.subplots()
ax.set_xlabel('Comprimento [m]')
ax.set_ylabel('Temperatura das gotas [°C]')
ax.axis([0, 30, 65, 90])
ax.xaxis.set_major_locator(plt.MultipleLocator(5))
ax.xaxis.set_minor_locator(plt.MultipleLocator(2.5))
ax.yaxis.set_major_locator(plt.MultipleLocator(5))
ax.yaxis.set_minor_locator(plt.MultipleLocator(2.5))
ax.scatter(xs1, dpm_temp1-273.15,
           s=25,
           c='white',
           marker='o',
           edgecolors='black',
           linewidths=1)
ax.grid(color='gray',ls=':')
# ax.legend(loc='best')
fig.tight_layout(pad=0.01)
plt.savefig('repar_30m_keps_np10_coll_coal_ssd_atmz/repar_temp.png',
            dpi=1200,
            format='png')
