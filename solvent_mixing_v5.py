# Modeling of solvent mixing

import numpy as np
import random as rd
from math import *
import matplotlib.pyplot as plt
import matplotlib.patches as pat
import mixFuncs_v5 as mix
import animatplot as amp
from matplotlib import animation

try:
    lattice_x = int(input('Lattice size in x direction (default=40): '))
except ValueError:
    lattice_x = 40

try:
    lattice_y = int(input('Lattice size in y direction (default=21): '))
except ValueError:
    lattice_y = 21

try:
    probe_point = int(input('x-position of probe point (-Lx/2 < x < Lx, default=-15): '))
except ValueError:
    probe_point = -15

try:
    boxSize = int(input('Box size for averaging (3, 5, 7, default=7): '))
except ValueError:
    boxSize = 7

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

x_blue = []     # ステップ毎の青い粒子群のx座標の格納庫
y_blue = []     # ステップ毎の青い粒子群のy座標の格納庫
x_red = []      # ステップ毎の赤い粒子群のx座標の格納庫
y_red = []      # ステップ毎の赤い粒子群のy座標の格納庫

num_step = []
probe_point_status_mean_list = []

for i in range(num_repert+1):
    num_step.append(i)
    probe_point_status_mean = mix.probePointMean(probe_point_id, lattice_y, currentConfig, boxSize)  # プローブ点周囲の状態の平均
    probe_point_status_mean_list.append(probe_point_status_mean)                            # そのリスト
    pointsCoordinates = mix.pointsCoordinates(end_point_id, currentConfig)  
    x_blue.append(pointsCoordinates[0])
    y_blue.append(pointsCoordinates[1])
    x_red.append(pointsCoordinates[2])
    y_red.append(pointsCoordinates[3])
    updatedConfig = mix.exchangePairs(lattice_x, lattice_y, end_point_id, currentConfig)    # 全ての格子点で粒子の交換を行う
    currentConfig = updatedConfig  

fig = plt.figure(figsize=(16.0, 6.0))

# Animation of mixing configration

range_x = lattice_x/2
range_y = lattice_y/2
p_size = int(np.sqrt(lattice_y))
aveBox = pat.Rectangle(xy=(probe_point - (boxSize-1)/2, - boxSize/2), width=boxSize, height=boxSize, lw=1.5, ec='k', fill=False)

fig_title1 = "Solvent Mixing"

ax1 = fig.add_subplot(121, title=fig_title1, xlabel='$X$', ylabel='$Y$',
                                xlim=[-range_x, range_x], ylim=[-range_y , range_y])
ax1.set_xticks(np.linspace(-range_x, range_x, 5))
ax1.set_yticks(np.linspace(-range_y, range_y, 5))

ax1.add_patch(aveBox)

configration_blue = amp.blocks.Scatter(x_blue, y_blue, s=p_size, ax=ax1, color='blue')
configration_red = amp.blocks.Scatter(x_red, y_red, s=p_size, ax=ax1, color='red')

# Animation of statistics of probe point status

fig_title2 = "Concentration averaged in a box centered at ({0},0)".format(probe_point)

ax2 = fig.add_subplot(122, title=fig_title2, xlabel='$N$', ylabel='$C$', xlim=[0, num_repert], ylim=[0, 1])
ax2.set_xticks(np.linspace(0, num_repert, 6))
ax2.set_yticks(np.linspace(0, 1, 5))
ax2.grid(visible=True, which='major', color='#666666', linestyle='--')

step, probe_point_mean = mix.drawStepEvolutionFunc(num_repert, num_step, probe_point_status_mean_list)

concentration = amp.blocks.Line(step, probe_point_mean, ax=ax2)

t = np.linspace(0, num_repert, num_repert+1)
timeline = amp.Timeline(t, units=' steps', fps=30)

anim = amp.Animation([configration_blue, configration_red, concentration], timeline)
anim.controls()

savefile = "./gif/Solvent_Mixing_{0}x{1}x{2}steps".format(lattice_x,lattice_y,num_repert)
anim.save_gif(savefile)

plt.show()