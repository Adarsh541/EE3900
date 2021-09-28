# -*- coding: utf-8 -*-
"""Gate3.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1dtJBPPB7psRiE7E7opl4zfW5TSU3BuIg
"""

import numpy as np
from matplotlib import pyplot as plt

sr = 300000
t = np.linspace(0,1,sr)
T = 1/sr
f1 = 15/2
f2 = 10
# Signal x(t)
s1 = 4*np.sin(2*np.pi*f1*t)
s2 = 8*np.cos(2*np.pi*f2*t-(np.pi/2))
s = s1+s2
P = np.linalg.norm(s)**2/sr
print('Power: ',P)
plt.plot(t,s,color='orange')
plt.grid()
plt.xlabel('time')
plt.ylabel('s(t)')