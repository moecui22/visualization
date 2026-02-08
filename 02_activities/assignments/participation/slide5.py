import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import scipy
import PIL
import requests

# customizing

np.random.seed(613)
x = np.arange(50)
y1 = np.random.randint(0, 100,50)
y2 = np.random.randint(0, 100,50)

fig, ax = plt.subplots(figsize=(5, 3))
ax.plot(x,y1)
ax.plot(x,y2)
fig.show()

## adding legend
fig, ax = plt.subplots(figsize=(5, 3))
ax.plot(x,y1, label = "Person 1" )
ax.plot(x,y2, label = "Person 2" )
ax.legend(loc='lower right')
fig.show()

# customizing legend
fig, ax = plt.subplots(figsize=(5, 3))
ax.plot(x,y1, label = "Person 1")
ax.plot(x,y2, label = "Person 2")
ax.legend(loc='lower right', #*** change the parameters here
            frameon = True, #add frame around the legend
            fontsize = 12, #change font size
            ncol = 2, #specify number of columns
            shadow = True )
fig.show()

# you can also customizing the location of it
# ax.legend(loc=‘upper left’, bbox_to_anchor =(1, 1))

# text and annotation
fig, ax = plt.subplots(figsize=(5, 3))
ax.scatter(x,y1, label = "Person 1")
ax.scatter(x,y2, label = "Person 2")
ax.legend(loc='lower right')

ax.text(10, 95, "This value is important!")
fig.show()

ax.text(10, 95, "This value is important!",
            ha='center', ##alignment of text
            color = 'red', ##modify font colour
            size = 20) ##modify font size
fig.show()

# change the position of the text / annotation
fig, ax = plt.subplots()
ax.axis([0, 10, 0, 10])

ax.text(1, 5, ". Data:(1, 5)", transform=ax.transData )
ax.text(0.5, 0.1, ". Axes:(0.5, 0.1)", transform=ax.transAxes )
ax.text(0.2, 0.2, ". Figure:(0.2, 0.2)", transform=fig.transFigure )

## adding arrows to your annotation
ax.annotate('This is important!', xy=(10, 95), xytext=(20, 94),
arrowprops=dict(facecolor='black'))

## advanced: changing styles of the arrow:
ax.annotate('This is important!’,
xy=(10, 95), xytext=(20, 94),
arrowprops = dict(arrowstyle = "wedge",
color = " hotpink "))

# axis/label
fig, ax = plt.subplots(figsize=(5, 3))
ax.scatter(x,y1, label = "Person 1")
ax.scatter(x,y2, label = "Person 2")
ax.legend(loc='lower right')
ax.yaxis.set_major_locator(plt.NullLocator())
ax.xaxis.set_major_formatter(plt.NullFormatter())

# ticks
fig, ax = plt.subplots(figsize=(5, 3))
ax.scatter(x,y1, label = "Person 1")
ax.scatter(x,y2, label = "Person 2")
ax.legend(loc='lower right')
ax.xaxis.set_major_locator(plt.MaxNLocator(3))

# tick interval
fig, ax = plt.subplots(figsize=(5, 3))
ax.scatter(x,y1, label = "Person 1")
ax.scatter(x,y2, label = "Person 2")
ax.legend(loc='lower right')
ax.xaxis.set_major_locator(plt.MultipleLocator(5))

# rotate ticks
fig, ax = plt.subplots(figsize=(5, 3))
ax.scatter(x,y1, label = "Person 1")
ax.scatter(x,y2, label = "Person 2")
ax.legend(loc='lower right’)
plt.xticks(rotation=45, ha='right')

# font of the ticks
font1 = {' family':'serif','color':'indigo'}
fig, ax = plt.subplots(figsize=(5, 3))
ax.scatter(x,y1, label = "Person 1")
ax.scatter(x,y2, label = "Person 2")
ax.legend(loc='lower right')
plt.xlabel('Shiny New X Axis!', fontsize = 18, fontdict = font1)

# styles: changing the aesthetic dimensions of the plots
plt.style.use('fivethirtyeight')
np.random.seed(613)
x = np.arange(50)
y1 = np.random.randint(0, 100,50)
y2 = np.random.randint(0, 100,50)
fig, ax = plt.subplots(figsize=(5, 3))
ax.plot(x,y1)
ax.plot(x,y2)
fig.show()

# end