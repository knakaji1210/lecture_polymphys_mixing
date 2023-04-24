# Modeling of solvent mixing

import numpy as np
import random as rd
from math import *
import matplotlib.pyplot as plt
import mixFuncs_v2 as mix
import animatplot as amp
from matplotlib import animation

fig = plt.figure(figsize=(16.0, 6.0))

lattice_x = 100
lattice_y = 50
range_x = lattice_x/2
range_y = lattice_y/2
end_point_id = lattice_x * lattice_y
probe_point_id = int(lattice_x*lattice_y/4 + lattice_y/2)

num_repert = 200
num_sample = 50
num_status_mean = num_repert - num_sample

x_blue = []
y_blue = []
x_red = []
y_red = []

probe_point_status = []
probe_point_status_mean = []
num_step = []

# Building of initial configuration

initialConfig = mix.initialConfig(lattice_x, lattice_y)
currentConfig = initialConfig

# Stepwise point exchange & Status check of probe point 

for i in range(num_repert):
    probe_point = currentConfig[probe_point_id]
    probe_point_status.append(probe_point[1])
    pointsCoordinates = mix.pointsCoordinates(end_point_id, currentConfig)
    x_blue.append(pointsCoordinates[0])
    y_blue.append(pointsCoordinates[1])
    x_red.append(pointsCoordinates[2])
    y_red.append(pointsCoordinates[3])
    updatedConfig = mix.exchangePairs(lattice_x, lattice_y, end_point_id, currentConfig)
    currentConfig = updatedConfig

#  Stepwise evolution of statistics of probe point status

for i in range(num_repert):
    probe_point_status_extracted = []
    if i > num_status_mean:
        pass
    else:
        for j in range(num_sample):
            probe_point_status_extracted.append(probe_point_status[i+j])
    num_step.append(i)
    probe_point_status_mean.append(np.mean(probe_point_status_extracted))

#  Animation of statistics of probe point status

ax1 = fig.add_subplot(121, title='Solvent Mixing', xlabel='X', ylabel='Y',
        xlim=[-range_x, range_x], ylim=[-range_y , range_y])
#ax1.set_xticks(np.linspace(-range_x, range_x, lattice_x + 1))
#ax1.set_yticks(np.linspace(-range_y, range_y, lattice_y + 1))
ax1.set_xticks(np.linspace(-range_x, range_x, 5))
ax1.set_yticks(np.linspace(-range_y, range_y, 5))
#ax1.grid(b=True, which='major', color='#999999', linestyle='-')

configration_blue = amp.blocks.Scatter(x_blue, y_blue, ax=ax1, color='blue')
configration_red = amp.blocks.Scatter(x_red, y_red, ax=ax1, color='red')

ax2 = fig.add_subplot(122, title='Step evolution of probe point concentration', xlabel='Steps', ylabel='Concentration',            xlim=[0, num_repert], ylim=[0, 1])
ax2.set_xticks(np.linspace(0, num_repert, 6))
ax2.set_yticks(np.linspace(0, 1, 5))
ax2.grid(b=True, which='major', color='#666666', linestyle='--')

step, probe_point_mean = mix.drawStepEvolutionFunc(num_repert, num_step, probe_point_status_mean)

concentration = amp.blocks.Line(step, probe_point_mean, ax=ax2)

t = np.linspace(0, num_repert-1, num_repert)
timeline = amp.Timeline(t, units='steps', fps=30)

anim = amp.Animation([configration_blue, configration_red, concentration], timeline)
anim.controls()
anim.save_gif("./gif/solvent_mix")

plt.show()