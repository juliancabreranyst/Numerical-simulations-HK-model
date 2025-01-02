import numpy as np
import matplotlib.pyplot as plt
#plt.rc('text', usetex=True)
plt.rcParams.update({
    "text.usetex": True,
    "font.family": "serif",
    "font.serif": ["Palatino"],
#     "font.serif": ["Computer Modern"],
})
plt.style.use('fast')
data = np.loadtxt('grafo_grupos.txt')

t= data[:,0]
x_1 = data[:,1]
x_2 = data[:,2]
x_3 = data[:,3]
x_4 = data[:,4]
x_5 = data[:,5]
x_6 = data[:,6]
x_7 = data[:,7]
x_8 = data[:,8]
x_9 = data[:,9]
x_10 = data[:,10]
x_11 = data[:,11]
x_12 = data[:,12]
x_13 = data[:,13]
x_14 = data[:,14]
x_15 = data[:,15]
x_16 = data[:,16]
x_17 = data[:,17]
x_18 = data[:,18]
x_19 = data[:,19]
media = data[:,20]
plt.figure()
#plt.ylim(-2.2,2.2)
plt.plot(t,x_1,linestyle='solid',linewidth=1.5,color=(0.314, 0.631, 0.49), label=r'Grupo 1', markersize=2)
plt.plot(t,x_2,linestyle='solid',linewidth=1.5,color=(0.314, 0.631, 0.49),markersize=1)
plt.plot(t,x_3,linestyle='solid',linewidth=1.5,color=(0.314, 0.631, 0.49),  markersize=2)
plt.plot(t,x_4,linestyle='solid',linewidth=1.5,color=(0.314, 0.631, 0.49), markersize=2)
plt.plot(t,x_5,linestyle='solid',linewidth=1.5,color=(0.314, 0.631, 0.49), markersize=2)
plt.plot(t,x_6,linestyle='solid',linewidth=1.5,color=(0.314, 0.631, 0.49), markersize=2)
plt.plot(t,x_7,linestyle='solid',linewidth=1.5,color=(0.314, 0.631, 0.49), markersize=2)
plt.plot(t,x_8,linestyle='solid',linewidth=1.5,color=(1, 0.686, 0.255), label=r'Grupo 2', markersize=2)
plt.plot(t,x_9,linestyle='solid',linewidth=1.5,color=(1, 0.686, 0.255), markersize=2)
plt.plot(t,x_10,linestyle='solid',linewidth=1.5,color=(1, 0.686, 0.255), markersize=2)
plt.plot(t,x_11,linestyle='solid',linewidth=1.5,color=(1, 0.686, 0.255), markersize=2)
plt.plot(t,x_12,linestyle='solid',linewidth=1.5,color=(1, 0.686, 0.255), markersize=2)
plt.plot(t,x_13,linestyle='solid',linewidth=1.5,color=(1, 0.686, 0.255), markersize=2)
plt.plot(t,x_14,linestyle='solid',linewidth=1.5,color=(1, 0.686, 0.255), markersize=2)
plt.plot(t,x_15,linestyle='solid',linewidth=1.5,color=(0.31, 0.596, 0.62),label=r'Grupo 3', markersize=2)
plt.plot(t,x_16,linestyle='solid',linewidth=1.5,color=(0.31, 0.596, 0.62), markersize=2)
plt.plot(t,x_17,linestyle='solid',linewidth=1.5,color=(0.31, 0.596, 0.62), markersize=2)
plt.plot(t,x_18,linestyle='solid',linewidth=1.5,color=(0.31, 0.596, 0.62), markersize=2)
plt.plot(t,x_19,linestyle='solid',linewidth=1.5,color=(0.31, 0.596, 0.62), markersize=2)
plt.plot(t,media,linestyle='dashed',linewidth=2,color=(0.784, 0.22, 0.322), label=r'$\overline{X}(t)$', markersize=2)
plt.xlabel(r'tiempo $t$', fontsize=15)
plt.ylabel(r'opiniones $x_i(t)$', fontsize=15)
plt.legend(
           shadow=True, 
           loc=(0.7, 0.5),
           handlelength=1.5, fontsize=14)
plt.title(r'Red unión disjunta de componentes fuertemente conexas')
#plt.xticks(np.arange(0, 20+1, 2.0),fontsize=10)
#plt.yticks(np.arange(-1, 1.5, 0.5),fontsize=10)
plt.savefig('grafo_grupos.pdf', dpi=400)