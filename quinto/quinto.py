#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan  3 20:53:30 2020

@author: llabori
"""

# Ejemplo de listas
square = [3, 5, 12, 67]

# Las listas pueden ser indexadas y accesar a un rango especifico
# de valores
print(square[0], end='\n')
print(square[2:], end='\n')
print(square[:2], end='\n')
print(square[-1], end='\n')
print(square[:], end='\n')

# Con la siguiente instruccion se constata el mismo concepto
# expuesto con los string, El conjunto el excluyente hacia el 
# extremo superior
print(square[0:2], end='\n')

# Las listas soportan la concatenación, situación distinta a la
# observada con los string
square1 = [2, 45, 67, 89, 5]
Total = square + square1
print(Total, end ='\n')

# De forma distinta a los String (los cuales son inmitables) las
# listas pueden mutar
square[3] = 15
print(square[:], end='\n')

# Por ser mutables laslistas cuentas con metodos a traves de los 
# cuales se pueden anexar datos a la misma
square.append(23)
square.append(34)
print(square[:], end='\n')

# Es factible cambiar un rango particular de valores
# dentro de la lista
square[2:5] = [56, 90, 56]
print(square[:], end='\n')

# Se puede contar con una Lista totalmente vacia
square = []
print(square[:], end='\n')

# Se puede cococer la cantidad de elementos que se encuentran
# interno a la lista
square = [2, 34, 2, 56, 89, 45]
Long = len(square)
print(Long, end='\n')

# Es posible incluir listas dentro de otras listas
square2 = [2, 56, 89, 0, 47, 12]
square3 = [square, square2]
print(square3[0], end='\n')
print(square3[1], end='\n')

# Se puede accesar a un valor particualr cuandolas listas se
# encuentran enlazadas
print(square3[0][0], end='\n')
print(square3[0][1], end='\n')
print(square3[1][0], end='\n')
print(square3[1][3], end='\n')
