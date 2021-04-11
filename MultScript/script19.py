#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 10 18:36:17 2020

@author: llabori
"""

""" Tercer ejemplo con programacion funcional """
from functools import reduce

numeros = (1, 2, 3, 4, 5, 6)
def suma(x,y):
    return x + y

suma = reduce(suma, numeros)
print(suma)