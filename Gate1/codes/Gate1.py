# -*- coding: utf-8 -*-
"""EE3900_GATE1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1IiPONGMMaxkWIaNwBwM_INWxoaoAbZrZ
"""

import numpy as np
from matplotlib import pyplot as plt

SAMPLE_RATE = 40000  # Hertz
DURATION = 5  # Seconds

# function to generate a sine wave in specified length of time interval
# x(t)
def generate_sine_wave(freq, sample_rate, duration):
    x = np.linspace(0, duration, sample_rate * duration, endpoint=False)
    frequencies = x * freq
    y = np.sin((2 * np.pi) * frequencies)
    return x, y

# Generate a baseband signal with bandwidth 10k Hertz
# signal with frequency near zero
x, f1 = np.multiply(generate_sine_wave(1, SAMPLE_RATE, DURATION),1)
# signal with frequency 100 Hz
_, f2 = np.multiply(generate_sine_wave(100, SAMPLE_RATE, DURATION),0.1)
# signal with frequency 1000 Hz
_, f3 = np.multiply(generate_sine_wave(1000, SAMPLE_RATE, DURATION),0.2)
# signal with frequency 10000 Hz
_, f4 = np.multiply(generate_sine_wave(10000, SAMPLE_RATE, DURATION),0.3)
# add all the pure signals
mixed_tone = f1+f2+f3+f4
# final baseband
normalized_tone = np.int16((mixed_tone / mixed_tone.max()) * 32767)

# plot the baseband
plt.plot(normalized_tone[:1000])
plt.title('x(t)')
plt.show()
#########
#########
# function to generate a time scaled sine wave in specified length of time interval
# x(1+(t/2))
def time_shift_generation(freq, sample_rate, duration):
    y = np.linspace(0, duration, sample_rate * duration, endpoint=False)
    frequencies = (1+(y/2)) * (freq)
    z = np.sin((2 * np.pi) * frequencies)
    return y, z

# generating the signal
x1, ft1 = np.multiply(time_shift_generation(1, SAMPLE_RATE, DURATION),1)
_, ft2 = np.multiply(time_shift_generation(100, SAMPLE_RATE, DURATION),0.1)
_, ft3 = np.multiply(time_shift_generation(1000, SAMPLE_RATE, DURATION),0.2)
_, ft4 = np.multiply(time_shift_generation(10000, SAMPLE_RATE, DURATION),0.3)

mixed_tone_t = ft1+ft2+ft3+ft4
normalized_tone_t = np.int16((mixed_tone_t / mixed_tone_t.max()) * 32767)

# plotting
plt.plot(normalized_tone_t[:1000])
plt.title('x(1+(t/2))')
plt.show()

##########
##########
# product of above two signals
mixed_tone_f = np.multiply(mixed_tone,mixed_tone_t)
normalized_tone_f = np.int16((mixed_tone_f/ mixed_tone_f.max()) * 32767)

# plotting
plt.plot(normalized_tone_f[:1000])
plt.title('y(t)')
plt.show()

##########
##########
# find the frequencies in the final signal
from scipy.fft import fft, fftfreq

#Number of samples in normalized_tone
N = SAMPLE_RATE * DURATION

yf = fft(normalized_tone_f)
xf = fftfreq(N, 1 / SAMPLE_RATE)

plt.plot(xf, np.abs(yf))
plt.xlabel('frequencies present in y(t)')
plt.show()