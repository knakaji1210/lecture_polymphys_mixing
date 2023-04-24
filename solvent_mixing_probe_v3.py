# Modeling of solvent mixing (statistics of probe point status only)

import numpy as np
import random as rd
from math import *
import matplotlib.pyplot as plt
import mixFuncs_v3 as mix
import animatplot as amp

try:
    lattice_x = int(input('Lattice size in x direction (default=40): '))
except ValueError:
    lattice_x = 40

try:
    lattice_y = int(input('Lattice size in y direction (default=20): '))
except ValueError:
    lattice_y = 20

try:
    probe_point = int(input('x-position of probe point (-Lx/2 < x < Lx, default=-15): '))
except ValueError:
    probe_point = -15

try:
    num_repert = int(input('Number of steps (default=200): '))
except ValueError:
    num_repert = 200

end_point_id = lattice_x * lattice_y
probe_point_id = int(lattice_y*(lattice_x/2+probe_point) + lattice_y/2)     # 濃度をチェックするプローブ点の決定

# Building of initial configuration

initialConfig = mix.initialConfig(lattice_x, lattice_y)     # 初期配列の作成
currentConfig = initialConfig                               # 初期配列を現在の配列とする

# Stepwise point exchange & Status check of probe point 

num_step = []
probe_point_status_mean_list = []

for i in range(num_repert+1):
    num_step.append(i)
    probe_point_status_mean = mix.probePointMean(probe_point_id, lattice_y, currentConfig)  # プローブ点周囲の状態の平均
    probe_point_status_mean_list.append(probe_point_status_mean)                            # そのリスト
    updatedConfig = mix.exchangePairs(lattice_x, lattice_y, end_point_id, currentConfig)    # 全ての格子点で粒子の交換を行う
    currentConfig = updatedConfig 

# Animation of statistics of probe point status

fig = plt.figure(figsize=(8.0, 6.0))

fig_title = "Concentration at Probe Point ({0}, 0)".format(probe_point)
savefile = "./gif/Probe_Point_Concentration_{0}x{1}x{2}steps".format(lattice_x,lattice_y,num_repert)

ax1 = fig.add_subplot(111, title=fig_title, xlabel='$N$', ylabel='$C$', xlim=[0, num_repert], ylim=[0, 1])
ax1.set_xticks(np.linspace(0, num_repert, 6))
ax1.set_yticks(np.linspace(0, 1, 5))
ax1.grid(visible=True, which='major', color='#666666', linestyle='--')

step, probe_point_mean = mix.drawStepEvolutionFunc(num_repert, num_step, probe_point_status_mean_list)

t = np.linspace(0, num_repert, num_repert+1)

concentration = amp.blocks.Line(step, probe_point_mean, ax=ax1)
timeline = amp.Timeline(t, units=' steps', fps=10)

anim = amp.Animation([concentration], timeline)
anim.controls()
anim.save_gif(savefile)

plt.show()