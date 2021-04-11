#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 15 18:32:36 2020

@author: llabori
"""
""" Ejemplos con Listas """

# En las listas los elementos que la integran pueden ser de diferente tipo
# En leguaje C todos los elementos tienen que ser del mismo tipo
# En la declaracion las listas se encuentran encerradas entre corchetes
# Los elementos que componen la lista pueden ser cambiados
# El tamaño de una lista puede ser alterado

lista = ['version', 10.9, 'barco', 38, 'camion', 39.67]
short_list = [125, 'john']

print(lista)
print(short_list)
print(lista[0:2])
print(lista[2:])
print(lista[4])
print(short_list * 2)
print(lista + short_list)