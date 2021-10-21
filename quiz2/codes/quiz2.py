# -*- coding: utf-8 -*-
"""quiz2

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1y55IzCovrKlHnjLd7ChE2EQzAkPWJ0ft
"""

import numpy as np
import matplotlib.pyplot as pyplot

# inner radius
inner = 2/3

# the two circles
thetas = np.linspace(0,2*np.pi, 200)

xcircle = 2*np.cos(thetas)
ycircle = 2*np.sin(thetas)

x_eigens = np.cos(thetas)* inner
y_eigens = np.sin(thetas) * inner

xs = np.linspace(-2.1,2.1, 801)
ys = np.linspace(-2.1,2.1, 801)

# mesh for contours
xv,yv = np.meshgrid(xs,ys)

# generate the level map
r = xv**2 + yv**2
pyplot.figure(figsize=(5,5))

# plot the contours with two levels only
# notice the xv, yv parameters
pyplot.contourf(xv, yv, r, levels=[inner**2,4], color='orange',label='ROC')

# plot the two circles
pyplot.plot(xcircle, ycircle, color='r', linewidth=2)
pyplot.plot(x_eigens, y_eigens, color='b', linewidth=3)
pyplot.xlim(-3,3)
pyplot.ylim(-3,3)
pyplot.scatter(2,0,label='zero')
pyplot.scatter(0.66,0,label='pole')
pyplot.legend()
pyplot.grid()
pyplot.show()