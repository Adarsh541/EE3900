# -*- coding: utf-8 -*-
"""EE3900_As2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1uHWDoIIP311H0kO5MG6hPAK7IMt3Mp2E
"""

import numpy as np
import math

# Matries
A = np.array([[1,2,-3],[5,0,2],[1,-1,1]])
B = np.array([[3,-1,2],[4,2,5],[2,0,3]])
C = np.array([[4,1,2],[0,3,2],[1,-2,3]])
# Sum of matrcies A and B
a_plus_b = A+B
# difference between matrices B and C
b_minus_c = B-C
print("A+B: ",a_plus_b)
print("B-C: ",b_minus_c)
# (A+B)-C
Q = a_plus_b - C
# A+(B-C)
R = A + b_minus_c
# If Q and R are identical then Q-R should be a null matrix 
print("verification: ",Q-R)

