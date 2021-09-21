# -*- coding: utf-8 -*-
"""G.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/12bzu57MLIhBneNVoNVwlghqwTlh1JKpn
"""

import numpy as np
from matplotlib import pyplot as plt


time  = np.arange(0.0, 0.001, 0.00001)

# Signal x(t)
x   = np.sin(2*np.pi*10000*time)
# signal x(1+t/2)
x_s = np.sin(1+(2*np.pi*10000*(time/2)))
# signal y(t)
y = x*x_s
# plot of x(t)
plt.plot(time, x)
plt.grid(True, which='both')
plt.axhline(y=0, color='k')
plt.show()

# plot y(t)
plt.plot(time,y)
plt.grid(True, which='both')
plt.axhline(y=0, color='k')
plt.show()

# DFT of y(t)
fourier=np.fft.fft(y)
freq=np.fft.fftfreq(fourier.shape[0], d=1/1e5)
plt.plot(freq, np.abs(fourier))