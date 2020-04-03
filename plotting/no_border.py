# -*- coding: utf-8 -*-
"""
Created on Fri Apr  3 10:07:15 2020

@author: Alex
"""


import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0, 4 * np.pi, 0.001)
y = np.sin(x)

fig1 = plt.figure(facecolor="white")
ax1 = plt.axes(frameon=False)
ax1.set_frame_on(False)

ax1.axes.get_yaxis().set_visible(False)
ax1.axes.get_xaxis().set_visible(False)
plt.fill_between(x, y, y + 0.1, color="k")


## the following lines are used to create a picture without white border

# set figure to use the full window (0 to 1)
plt.subplots_adjust(
    top=1,
    bottom=0,
    right=1,
    left=0,
    hspace=0,
    wspace=0,
    )

# set margin to zero on both axes
plt.margins(0, 0)

# the following may help for figures with ticks but is not necessary here
# ax1.xaxis.set_major_locator(plt.NullLocator())
# ax1.yaxis.set_major_locator(plt.NullLocator())

# save the figure with explicitly no padding and a tight bounding box
plt.savefig(
    "sin_template.png",
    dpi=300,
    bbox_inches='tight',
    pad_inches=0,
    )
