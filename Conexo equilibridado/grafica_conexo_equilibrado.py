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
data = np.loadtxt('grafo_conexo_equilibrado.txt')

t= data[:,0]
x_1 = data[:,1]
x_2 = data[:,2]
x_3 = data[:,3]
x_4 = data[:,4]
x_5 = data[:,5]
media = data[:,6]
plt.figure()
#plt.ylim(-2.2,2.2)
plt.plot(t,x_1,linestyle='solid',linewidth=1.5,color=(0.314, 0.631, 0.49), label=r'$x_i(t)$', markersize=2)
plt.plot(t,x_2,linestyle='solid',linewidth=1.5,color=(0.314, 0.631, 0.49),markersize=1)
plt.plot(t,x_3,linestyle='solid',linewidth=1.5,color=(0.314, 0.631, 0.49),  markersize=2)
plt.plot(t,x_4,linestyle='solid',linewidth=1.5,color=(0.314, 0.631, 0.49), markersize=2)
plt.plot(t,x_5,linestyle='solid',linewidth=1.5,color=(0.314, 0.631, 0.49), markersize=2)
plt.plot(t,media,linestyle='dashed',linewidth=2,color=(0.784, 0.22, 0.322), label=r'$\overline{X}(t)$', markersize=2)
plt.xlabel(r'tiempo $t$', fontsize=15)
plt.ylabel(r'opiniones $x_i(t)$', fontsize=15)
plt.legend(
           shadow=True, 
         #  loc=(0.7, 0.65),
           handlelength=1.5, fontsize=14)
#plt.xticks(np.arange(0, 20+1, 2.0),fontsize=10)
#plt.yticks(np.arange(-1, 1.5, 0.5),fontsize=10)
plt.title(r'Red conexa y equilibrada')
plt.savefig('grafo_conexo_equilibrado.pdf', dpi=400)