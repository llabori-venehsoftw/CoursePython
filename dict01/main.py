#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 16 00:55:44 2020

@author: llabori
"""

import numpy as np
from matplotlib import pyplot as plt
#from histogram import Histogram, plothist

def inverse_dic(d):
    
    inverse = dict()
    for key in d:
         valor = d[key]
         if valor not in inverse:
             inverse.__setitem__(valor, key)
         else:
             inverse[valor] += ' ' + key
                              
    return inverse

x = ['p', 'a', 'r', 'r', 'o', 't']

dict01 = {'a':1, 'p':1, 'r':2, 'o':1, 't':1 }
print(dict01)
print("--------------------------")
dict02 = inverse_dic(dict01)
print(dict02)

plt.hist(x, bins=10)
plt.show()