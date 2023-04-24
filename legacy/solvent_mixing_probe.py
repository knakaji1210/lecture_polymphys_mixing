# probe-point concentration of solvent mixing

import numpy as np
import random as rd
from math import *
import matplotlib.pyplot as plt
from matplotlib import animation
import mixFuncs as mix

fig = plt.figure(figsize=(8.0, 6.0))

lattice_x = 40
lattice_y = 20
idFinal = lattice_x * lattice_y

initConfig = mix.initConfig(lattice_x, lattice_y)
#img = mix.drawPoints(lattice_x, lattice_y, idFinal, initConfig)
#fig.savefig("./png/mixing0.png", dpi=300)

curConfig = initConfig

repNum = 5000

stat = []

for i in range(repNum):
    probePoint = curConfig[210]
    stat.append(probePoint[1])
    newConfg = mix.exchangePairs(lattice_x, lattice_y, idFinal, curConfig)
    #img = mix.drawPoints(lattice_x, lattice_y, idFinal, newConfg)
    #fig.savefig("./png/mixing"+str(i+1)+".png", dpi=300)
    curConfig = newConfg

numExt = 50
stat_mean = []
for i in range(repNum - numExt):
    stat_ext = []
    for j in range(numExt):
        stat_ext.append(stat[i+j])
    stat_mean.append(np.mean(stat_ext))

t_list = np.arange(0, repNum - numExt)
plt.title('Concentration of Probe Point')
plt.xlabel('t')
plt.ylabel('p')
plt.ylim(0, 1)
plt.plot(t_list, stat_mean)

#np.savetxt("./data/stat_list.txt", stat)
fig.savefig("./png/solvent_mixing_probe.png", dpi=300)

plt.show()
plt.close()