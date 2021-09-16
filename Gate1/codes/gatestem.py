# -*- coding: utf-8 -*-
"""Gatestem.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1xetbXwE5sI1h40FjRotBuRPQAsSSZSX_
"""

import numpy as np
from matplotlib import pyplot as plt
from scipy import pi
from scipy.fftpack import fft
 
 
# sampling at 60kHz
samp_rate = 60000
N = 2*samp_rate
time  = np.linspace(0,2,N)
 
# Signal x(t)
x   = np.cos(2*np.pi*10000*time)
# signal x(1+t/2)
x_s = np.cos(2*np.pi*10000*(1+(time/2)))
# signal y(t)
y = x*x_s
# plot of x(t)
plt.plot(time[0:100], x[0:100])
plt.grid(True, which='both')
plt.axhline(y=0, color='k')
plt.show()
 
# plot y(t)
plt.stem(time[0:100],y[0:100])
plt.grid(True, which='both')
plt.axhline(y=0, color='k')
plt.show()
 
# fourier transform of y(t)
freq = np.linspace(0.0,30000,samp_rate)
freq_data = fft(y)
four = np.abs(freq_data)
plt.plot(freq,four[0:samp_rate])