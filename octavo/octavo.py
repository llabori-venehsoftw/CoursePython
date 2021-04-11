#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan  3 23:00:57 2020

@author: llabori
"""

# Trabajamos con funciones
def fib(n): # Escribe una serie de Fibonacii hasta el numero n
    """ Print una serie de fibonacii hasta el numero n """
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()

fib(2000)
        