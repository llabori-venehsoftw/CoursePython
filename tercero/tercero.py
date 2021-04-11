#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan  3 01:16:40 2020

@author: llabori
"""

# Indexacion de un String
palabras = 'lavadodelcabello'
print(palabras[0],end='\n')
print(palabras[-1],end='\n')
print(palabras[3],end='\n')
print(palabras[-6],end='\n')

# Extraccion de SubString desde un String
# Verificación de impresión Excluyendo el 
# extremo superior del arreglo
print(palabras[0:3],end='\n')
print(palabras[6:8],end='\n')
print(palabras[0:6],end='\n')
print(palabras[6:9],end='\n')
print(palabras[9:16],end='\n')

# Extraccion de SubString desde un String
# Verificación de impresión Incluyendo el 
# extremo inferior del arreglo
print(palabras[0:],end='\n')
print(palabras[6:],end='\n')

# Extracion de SubString desde un String
# Verificacion de impresion 
print(palabras[:8],end='\n')
print(palabras[:6],end='\n')

#Verificacion de SubString con ciertas relaciones
letra1 = palabras[6:7]
letra2 = palabras[6]
if letra1 == letra2:
    print(letra1, letra2, sep=' ', end='\n')
    print('Las variables contienen la misma letra',end='\n')
else:
    print('Debe haber un error',end='\n')