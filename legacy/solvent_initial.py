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

for i in range(10):
    for j in range(10):
        x = i+0.5
        y = j-4.5
        ax.plot(x, y, marker=".", color="red")
        numRed+=1

for i in range(10):
    for j in range(10):
        x = i-9.5
        y = j-4.5
        ax.plot(x, y, marker=".", color="blue")
        numBlue+=1

print(numRed)
print(numBlue)

fig.savefig("./png/initial.png", dpi=300)

plt.show()