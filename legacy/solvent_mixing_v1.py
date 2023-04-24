# Animation of solvent mixing

import numpy as np
import random as rd
from math import *
import matplotlib.pyplot as plt
from matplotlib import animation
import mixFuncs as mix

fig = plt.figure(figsize=(8.0, 12.0))

lattice_x = 40
lattice_y = 20
idFinal = lattice_x * lattice_y

xRange = lattice_x/2
yRange = lattice_y/2

ax1 = fig.add_subplot(211, title='Solvent Mixing', xlabel='X', ylabel='Y',
        xlim=[-xRange, xRange], ylim=[-yRange , yRange])
#ax1.set_xticks(np.linspace(-xRange, xRange, lattice_x + 1))
#x1.set_yticks(np.linspace(-yRange, yRange, lattice_y + 1))
ax1.set_xticks(np.linspace(-xRange, xRange, 5))
ax1.set_yticks(np.linspace(-yRange, yRange, 5))
#ax1.grid(b=True, which='major', color='#999999', linestyle='-')

imgs1_rep = []

initConfig = mix.initConfig(lattice_x, lattice_y)
imgs1 = mix.drawPoints(idFinal, initConfig)
imgs1_rep = imgs1_rep + imgs1

curConfig = initConfig

repNum = 100

status_list = []
probePointNum = int(lattice_x*lattice_y/4 + lattice_y/2)

lattice_x = 40
lattice_y = 20

for i in range(repNum):
    probePoint = curConfig[probePointNum]
    status_list.append(probePoint[1])
    newConfg = mix.exchangePairs(lattice_x, lattice_y, idFinal, curConfig)
    imgs1 = mix.drawPoints(idFinal, newConfg)
    imgs1_rep = imgs1_rep + imgs1
    curConfig = newConfg

numExt = 20
t_list = []
stat_mean = []
imgs2_rep = []

for i in range(repNum):
    status_ext = []
    if i > repNum - numExt:
        pass
    else:
        for j in range(numExt):
            status_ext.append(status_list[i+j])
    t_list.append(i)
    stat_mean.append(np.mean(status_ext))

ax2 = fig.add_subplot(212, title='Concentration of Probe Point', xlabel='t', ylabel='p', ylim=[0, 1])

imgs2 = mix.drawFunc(repNum, t_list, stat_mean)
imgs2_rep = imgs2_rep + imgs2

ani = animation.ArtistAnimation(fig, imgs1_rep, interval=100)
ani.save('./gif/solvent_mixing_ani.gif', writer = 'pillow', fps = 10)

ani = animation.ArtistAnimation(fig, imgs2_rep, interval=100)
ani.save('./gif/solvent_concentrqtio_ani.gif', writer = 'pillow', fps = 10)

plt.show()
plt.close()