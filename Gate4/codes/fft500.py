# -*- coding: utf-8 -*-
"""fft500.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1CsZc4xd4NBG9AMXJP1Gv8iULlunBWJbG
"""

import numpy as np
from matplotlib import pyplot as plt
from scipy import pi
from scipy.fft import fft,fftshift
# Nyquist rate = 700
# sampling rate  
samp_rate = 400
time = np.linspace(-1,1,2*samp_rate)
output = np.sinc(700*time)+np.sinc(500*time)
# plot of the given signal
plt.plot(time,output)
plt.xlim(-0.015,0.015)
plt.grid()
plt.show()
# sampling rate = 1/(length of input sequence)
freq = np.linspace(-200,200,800)
freq_data = fft(output)
four = np.abs(freq_data)
plt.plot(freq,fftshift(four))
plt.xlabel("Frequency")
plt.ylabel("Amplitude")
plt.grid()
plt.show()