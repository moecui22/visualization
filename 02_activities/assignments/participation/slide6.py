import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import scipy
import PIL
import requests

# subplot and combine

# sim data
np.random.seed(613)
x1 = np.arange(50)
y1 = np.random.randint(0, 75,50)
x2 = np.array(["Luffy", "Zoro", "Nami", "Usopp", "Sanji"])
y2 = np.array([110, 180, 240, 99, 220])

# subplot
fig,(ax1, ax2) = plt.subplots(ncols=2,
                                nrows=1,
                                figsize=(7, 3))
ax1.scatter(x1,y1)
ax2.bar(x2,y2)
fig.show()

# grid arrangement for the subplot
fig, someaxes = plt.subplot_mosaic([['ax1', 'ax3'],
                                    ['ax2', 'ax3']],
                                    figsize=(7, 4))

fig, someaxes = plt.subplot_mosaic([['ax1', 'ax3'],
                                    ['ax2', 'ax3']],
                                    figsize=(7, 4))
                                    someaxes["ax1"].scatter(x1,y1)
                                    someaxes["ax2"].bar(x2,y2)
                                    someaxes["ax3"].plot(x1,y1)
                                    plt.show()           

# example
fig, someaxes = plt.subplot_mosaic([['ax1', 'ax3'],
                                    ['ax2', 'ax3']],
                                    figsize=(7, 4),
                                    layout = "constrained")
someaxes["ax1"].scatter(x1,y1)
someaxes["ax2"].bar(x2,y2)
someaxes["ax3"].plot(x1,y1)
someaxes["ax1"].set_xlabel('A Big Label', fontsize=18)
someaxes["ax2"].set_xlabel('Another Label', fontsize=18)
someaxes["ax3"].set_xlabel('Label 2: 2 Fast 2 Furious', fontsize=18)

# first make our sample data
x = np.array(["Luffy", "Zoro", "Nami", "Usopp", "Sanji"])
y1 = np.array([110, 180, 240, 99, 220])
y2 = np.array([170, 100, 90, 120, 50])
# define our figure and axes (just one this time)
fig, ax = plt.subplots(figsize=(7, 3))
# now call both bar and plot elements to the same axes (ax)
ax.bar(x, y1,
color = "indigo")
ax.plot(x, y2,
color = "red")

# error bar?

## adding images to the plots
# library
from PIL import Image # to open images
import requests # to get images from URLs
from io import BytesIO # to store images

response = requests.get('https://upload.wikimedia.org/wikipedia/en/c/cb/Monkey_D_Luffy.png')
image_file = BytesIO(response.content)
image = Image.open(image_file)

fig, ax = plt.subplots(figsize=(7, 3))
ax.plot(x, y2, color = "red")

ax_image = fig.add_axes([0.1, # x coordinate (ON FIGURE, NOT AXES)
                            0.11, # y coordinate (ON FIGURE, NOT AXES)
                            0.15, # image width
                            0.35] # image height)

fig, ax = plt.subplots(figsize=(7, 3))
ax.plot(x, y2,
        color = "red")
ax_image = fig.add_axes([0.1, 0.11, 0.15, 0.35])
ax_image.imshow(image)
ax_image.axis('off’)

# end