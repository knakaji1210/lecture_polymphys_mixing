# Modeling of solvent mixing (time evolution of configurational change only)

import numpy as np
import random as rd
from math import *
import matplotlib.pyplot as plt
import mixFuncs_v3 as mix
import animatplot as amp
from matplotlib import animation

try:
    lattice_x = int(input('Lattice size in x direction (default=40): '))
except ValueError:
    lattice_x = 40

try:
    lattice_y = int(input('Lattice size in y direction (default=20): '))
except ValueError:
    lattice_y = 20

try:
    num_repert = int(input('Number of steps (default=200): '))
except ValueError:
    num_repert = 200

end_point_id = lattice_x * lattice_y

# Building of initial configuration

initialConfig = mix.initialConfig(lattice_x, lattice_y)     # 初期配列の作成
currentConfig = initialConfig                               # 初期配列を現在の配列とする

# Stepwise point exchange

x_blue = []     # ステップ毎の青い粒子群のx座標の格納庫
y_blue = []     # ステップ毎の青い粒子群のy座標の格納庫
x_red = []      # ステップ毎の赤い粒子群のx座標の格納庫
y_red = []      # ステップ毎の赤い粒子群のy座標の格納庫

for i in range(num_repert+1):
    pointsCoordinates = mix.pointsCoordinates(end_point_id, currentConfig)  
    x_blue.append(pointsCoordinates[0])
    y_blue.append(pointsCoordinates[1])
    x_red.append(pointsCoordinates[2])
    y_red.append(pointsCoordinates[3])
    updatedConfig = mix.exchangePairs(lattice_x, lattice_y, end_point_id, currentConfig)    # 全ての格子点で粒子の交換を行う
    currentConfig = updatedConfig                                                           # 新しい配列を現在の配列として、それを繰り返す

# Animation of mixing configration

t = np.linspace(0, num_repert, num_repert+1)

timeline = amp.Timeline(t, units=' steps', fps=10)

fig = plt.figure(figsize=(8.0, 6.0))

range_x = lattice_x/2
range_y = lattice_y/2
p_size = int(np.sqrt(lattice_y))

fig_title = "Solvent Mixing"
savefile = "./gif/Solvent_Mixing_Configration_{0}x{1}x{2}steps".format(lattice_x,lattice_y,num_repert)

ax1 = fig.add_subplot(111, title=fig_title, xlabel='$X$', ylabel='$Y$',
                                xlim=[-range_x, range_x], ylim=[-range_y , range_y])
ax1.set_xticks(np.linspace(-range_x, range_x, 5))
ax1.set_yticks(np.linspace(-range_y, range_y, 5))
#ax1.set_xticks(np.linspace(-range_x, range_x, lattice_x + 1))
#ax1.set_yticks(np.linspace(-range_y, range_y, lattice_y + 1))
#ax1.grid(visible=True, which='major', color='#999999', linestyle='-')

configration_blue = amp.blocks.Scatter(x_blue, y_blue, s=p_size, ax=ax1, color='blue')
configration_red = amp.blocks.Scatter(x_red, y_red, s=p_size, ax=ax1, color='red')

anim = amp.Animation([configration_blue, configration_red], timeline)
anim.controls()
anim.save_gif(savefile)

plt.show()