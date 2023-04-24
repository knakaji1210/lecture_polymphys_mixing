# Modeling of solvent mixing

import numpy as np
import random as rd
from math import *
import matplotlib.pyplot as plt
import mixFuncs_v2 as mix
import animatplot as amp

fig = plt.figure(figsize=(8.0, 6.0))

lattice_x = 40
lattice_y = 20
range_x = lattice_x/2
range_y = lattice_y/2
end_point_id = lattice_x * lattice_y
probe_point_id = int(lattice_x*lattice_y/4 + lattice_y/2)

num_repert = 500
num_sample = 50
num_status_mean = num_repert - num_sample

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

ax1 = fig.add_subplot(111, title='Step evolution of probe point concentration', xlabel='Steps', ylabel='Concentration',
            xlim=[0, num_repert], ylim=[0, 1])
ax1.set_xticks(np.linspace(0, num_repert, 6))
ax1.set_yticks(np.linspace(0, 1, 5))
ax1.grid(b=True, which='major', color='#666666', linestyle='--')

step, probe_point_mean = mix.drawStepEvolutionFunc(num_repert, num_step, probe_point_status_mean)

t = np.linspace(0, num_repert-1, num_repert)

concentration = amp.blocks.Line(step, probe_point_mean, ax=ax1)
timeline = amp.Timeline(t, units='steps', fps=100)

anim = amp.Animation([concentration], timeline)
anim.controls()
anim.save_gif("./gif/probe_point_concentration")

plt.show()