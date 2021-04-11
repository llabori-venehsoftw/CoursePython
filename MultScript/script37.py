#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 15 18:41:46 2020

@author: llabori
"""
""" Ejemplo con Tuplas """

# Las Tuplas se declarn utilizando Parentesis
# Las tuplas pueden ser vistas como una lista Only read
# Los elementos de las tuplas no pueden ser alterados

tupla = ('version', 10.9, 'barco', 38, 'camion', 39.67)
short_tupla = (125, 'john')

print(tupla)
print(tupla[0:4])
print(tupla[3:])
print(tupla[5])
print(short_tupla * 2)
print(tupla + short_tupla)
tupla[4] = 'pruebas'           # Esto genera un error debido a que los valores de las tuplas no se pueden modificar