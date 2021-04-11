#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan  3 22:25:13 2020

@author: llabori
"""

# Continuacion de los ciclos de control
# En esta oportunidad trabajaremos con break y continue
# AL igual que en lenguaje C, break interumpe la ejecución de un ciclo
# de control en particular
for x in range(2, 11):
    for j in range(2, x+1):
        if x % j == 0:
            print(x, "es igual a ", j, '*', x//j)
            break
        else:
            # loop fell through without finding a factor
            print(x, 'es un numero primo')
            break

# La instruccion continue ejecuta al igual que el lenguaje C
# el siguiente ciclo dentro del loop
for numero in range(2, 10):
    if numero % 2 == 0:
        print(" El numero ", numero, " es un numero par")
        continue
    print('El numero es =', numero, end='\n')
    