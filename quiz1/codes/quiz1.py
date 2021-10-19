# -*- coding: utf-8 -*-
"""quiz1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1kJG_IH3Zn7YCNPaGkzpxkuQigGhUNB0n
"""

import matplotlib.pyplot as plt
import numpy as np

n = np.linspace(0,10,11,endpoint=True)
# x[n]
x = (5**n)
# h[n]
def unit(time):
  x=[]
  for i in time:
    if i<0:
      x.append(0)
    else:
      x.append(1)
  return x
# input signal    
plt.stem(n,x)
plt.grid()
plt.xlabel("n")
plt.ylabel("x[n]")
plt.show()
# output signal
plt.stem(n,np.convolve(unit(n),x)[0:11])
plt.grid()
plt.xlabel("n")
plt.ylabel("y[n]")
plt.show()
print((np.convolve(unit(n),x)[0:11])/(x))

import matplotlib.pyplot as plt
import numpy as np

n = np.linspace(0,10,11,endpoint=True)
x = (5**n)*np.e**(2j*np.pi*n)
def unit(time):
  x=[]
  for i in time:
    if i<0:
      x.append(0)
    else:
      x.append(1)
  return x  
plt.stem(n,x)
plt.show()
plt.stem(n,np.convolve(unit(n),x)[0:11])
plt.grid()
plt.xlabel("n")
plt.ylabel("y[n]")
plt.show()
print((np.convolve(unit(n),x)[0:11])/(x))