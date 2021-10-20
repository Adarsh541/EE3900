# -*- coding: utf-8 -*-
"""lnyq

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1V_rAC02xQCTtGhO3QosaTyQxwXFTnR_o
"""

import numpy as np
from matplotlib import pyplot as plt
from scipy import pi
from scipy.fft import fft,fftshift
# Nyquist rate = 700
# sampling rate  
samp_rate = 600
time = np.linspace(-1,1,2*samp_rate)
output = np.sinc(700*time)+np.sinc(500*time)
# sampling rate = 1/(length of input sequence)
freq = np.linspace(-300,300,1200)
freq_data = fft(output)
four = np.abs(freq_data)
plt.subplot(1,2,1)
plt.plot(freq,fftshift(four))
plt.xlabel("Frequency")
plt.ylabel("Amplitude")
plt.grid()
plt.title('Sampling rate = 600Hz')


# Nyquist rate = 700
# sampling rate  
samp_rate = 400
time = np.linspace(-1,1,2*samp_rate)
output = np.sinc(700*time)+np.sinc(500*time)
# sampling rate = 1/(length of input sequence)
freq = np.linspace(-200,200,800)
freq_data = fft(output)
four = np.abs(freq_data)
plt.subplot(1,2,2)
plt.plot(freq,fftshift(four))
plt.xlabel("Frequency")
#plt.ylabel("Amplitude")
plt.grid()
plt.title('Sampling rate = 500Hz')

plt.suptitle("Sampling rate < Nyquist rate")
plt.show()