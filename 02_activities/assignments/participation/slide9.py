import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import scipy
import PIL
import requests

tips = sns.load_dataset("tips")
print(tips)

# basic plot
sns.lineplot(data=tips, # choose our dataset
                x='total_bill', # define our x variable
                y='tip') # define our y variable
sns.set_style('whitegrid') # pre style

tipgraph = sns.lineplot(data=tips,
                        x='total_bill',
                        y='tip')
tipgraph.set(title='Tips vs. Total Bill',
xlabel='Total Bill ($)',
ylabel='Tip Amount ($)')

# improve
fig = plt.subplots(figsize=(10, 3))
tipgraph = sns.lineplot(data=tips,
                            x='total_bill',
                            y='tip',
                            color = 'hotpink',
                            linestyle = '--',
                            linewidth = 3,
                            marker = 'o',
                            markerfacecolor = 'indigo')

## discussion on seaborn
tipgraph = sns.scatterplot(data=tips, x='total_bill',
                y='tip’, style = 'time', hue =
                'day’, palette = ['purple’,
                'hotpink', 'deepskyblue’,
                'yellowgreen'])
tipgraph.set(title='Tips vs. Total Bill',
xlabel='Total Bill ($)',
ylabel='Tip Amount ($)')

# relplot
daysplot = sns.relplot(
            data=tips,
            x="total_bill",
            y="tip",
            hue="sex",
            col="day",
            kind="scatter",
            col_wrap=2)
