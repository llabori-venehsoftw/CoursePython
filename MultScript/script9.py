#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 10 16:57:27 2020

@author: llabori
"""
""" Capturar Excepciones """
lista = [1, 2]
try:
    print(lista[1])
except IndexError:
    print(" Error: Error en el Indice ")
else:
    print(" No hay Error ")
finally:
    print(" Se ejecuto todo ")      # Lo que finalmente se ejecuta sin importar si hay o no error alguno