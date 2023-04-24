# 

import numpy as np
import random as rd
from math import *
import matplotlib.pyplot as plt

fig = plt.figure()

ax = fig.add_subplot(111,title='', xlabel='X', ylabel='Y',
                      xlim=[-10, 10], ylim=[-5, 5])

ax.set_xticks(np.linspace(-10, 10, 21))
ax.set_xticklabels([])

ax.set_yticks(np.linspace(-5, 5, 11))
ax.set_yticklabels([])

plt.grid(b=True, which='major', color='#999999', linestyle='-')

numRed = 0
numBlue = 0

coordinate_list = []

while numRed < 100:
    x = int((rd.random()-0.5)*20)+0.5
    y = int((rd.random()-0.5)*10)+0.5
    coordinate = [x, y]
    if coordinate in coordinate_list:
        pass
    else:
        coordinate_list.append(coordinate)
        ax.plot(x, y, marker=".", color="red")
        numRed+=1

print(numRed)
print(len(coordinate_list))

for i in range(20):
    for j in range(10):
        x = i-9.5
        y = j-4.5
        coordinate = [x, y]
        if coordinate in coordinate_list:
            pass
        else:
            ax.plot(x, y, marker=".", color="blue")
            numBlue+=1

print(numBlue)

fig.savefig("./png/mixing.png", dpi=300)

plt.show()