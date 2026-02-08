import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import scipy
import PIL
import requests

np.random.seed(613)
x = np.arange(50)
y = np.random.randint(0, 100,50)

fig, ax = plt.subplots(figsize=(5, 3))
ax.scatter(x,y)

plt.tight_layout()
plt.savefig("participation/slide2_scatter.png", dpi=300)
plt.show()

fig, ax = plt.subplots(figsize=(5, 3))
ax.plot(x,y)

ax.set_title('Total growth over time')
ax.set_ylabel('Total growth')
ax.set_xlabel('Years since start')
fig.tight_layout()

plt.tight_layout()
plt.savefig("participation/slide2_line.png", dpi=300)
plt.show()

font1 = {'family':'sans-serif', 'color':'blue', 'size':20}
font2 = {'family':'monospace', 'color':'green', 'size':14}

fig, ax = plt.subplots(figsize=(5, 3))
ax.plot(x,y)
ax.set_ylabel('Total growth', fontdict = font2)
ax.set_xlabel('Years since start', fontdict = font2)

fig, ax = plt.subplots(figsize=(5, 3))
ax.plot(x, y, marker='*' ,color = 'indigo' ,linestyle = '--',
    linewidth = 2)
fig.show()