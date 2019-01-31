import matplotlib.pyplot as plt
import numpy as np
from math import *
from pylab import *
from matplotlib.patches import Circle

bg = np.transpose(np.loadtxt('laplace_bg_015.txt'))
hg = np.transpose(np.loadtxt('laplace_hg_015.txt'))
hd = np.transpose(np.loadtxt('laplace_hd_015.txt'))
bd = np.transpose(np.loadtxt('laplace_bd_015.txt'))
hh = np.transpose(np.loadtxt('laplace_hh_015.txt'))
gg = np.transpose(np.loadtxt('laplace_gg_015.txt'))
dd = np.transpose(np.loadtxt('laplace_dd_015.txt'))

fig,ax = plt.subplots(figsize=(10,10))

# plt.plot(0.2,0.2,color='red',marker='x',markersize=10)
# plt.plot(bg[1],bg[2],
# color='red',linestyle='-',linewidth=2,label='[0.2,0.2]')
#
# plt.plot(0.2,0.8,color='red',marker='x',markersize=10)
# plt.plot(hg[1],hg[2],
# color='red',linestyle='-',linewidth=2,label='[0.2,0.8]')
#
# plt.plot(0.8,0.8,color='red',marker='x',markersize=10)
# plt.plot(hd[1],hd[2],
# color='red',linestyle='-',linewidth=2,label='[0.8,0.8]')
#
# plt.plot(0.8,0.2,color='red',marker='x',markersize=10)
# plt.plot(bd[1],bd[2],
# color='red',linestyle='-',linewidth=2,label='[0.8,0.2]')
#
# plt.plot(0.5,0.2,color='red',marker='x',markersize=10)
# plt.plot(bb[1],bb[2],
# color='red',linestyle='-',linewidth=2,label='[0.5,0.2]')
#
# plt.plot(0.5,0.8,color='red',marker='x',markersize=10)
# plt.plot(hh[1],hh[2],
# color='red',linestyle='-',linewidth=2,label='[0.5,0.8]')
#
# plt.plot(0.2,0.5,color='red',marker='x',markersize=10)
# plt.plot(gg[1],gg[2],
# color='red',linestyle='-',linewidth=2,label='[0.2,0.5]')
#
# plt.plot(0.8,0.5,color='red',marker='x',markersize=10)
# plt.plot(dd[1],dd[2],
# color='red',linestyle='-',linewidth=2,label='[0.8,0.5]')
#
# circle = Circle((0.5, 0.5), 0.05, facecolor='None', edgecolor='k', linewidth=2)
# ax.add_patch(circle)
#
# plt.ylabel('y')
# plt.xlabel('x')
#
# plt.axis([0,1,0,1])
#
# filename="Projet_PI_005.png"

plt.plot(bg[0,1:],log10(bg[4,1:]),
color='blue',linestyle='-',linewidth=2,label='[0.2,0.2]')

plt.plot(bd[0,1:],log10(bd[4,1:]),
color='black',linestyle='-',linewidth=2,label='[0.8,0.2]')

plt.plot(hg[0,1:],log10(hg[4,1:]),
color='blue',linestyle='-',linewidth=2,label='[0.2,0.8]')

plt.plot(hd[0,1:],log10(hd[4,1:]),
color='black',linestyle='-',linewidth=2,label='[0.8,0.8]')

plt.plot(hh[0,1:],log10(hh[4,1:]),
color='red',linestyle='-',linewidth=2,label='[0.5,0.8]')

plt.plot(bb[0,1:],log10(bb[4,1:]),
color='red',linestyle='-',linewidth=2,label='[0.5,0.2]')

plt.plot(gg[0,1:],log10(gg[4,1:]),
color='orange',linestyle='-',linewidth=2,label='[0.2,0.5]')

plt.plot(dd[0,1:],log10(dd[4,1:]),
color='cyan',linestyle='-',linewidth=2,label='[0.8,0.5]')

plt.ylabel('err')
plt.xlabel('k')
plt.legend(loc=0)

plt.axis([0,60,-4,3])

filename="Projet_PI_err_005.png"

fig.savefig(filename)
