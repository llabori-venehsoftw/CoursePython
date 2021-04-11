#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 10 18:03:31 2020

@author: llabori
"""
""" Ejemplo de programacion funcional """
def lower(elementos):
    return elementos.lower()

lista = ["Jose", "MARia", "Patricia"]
print(list(map(lower,lista)))          # map Ligada a la programación funcional en Python
#print(filter)
print([cad.lower() for cad in lista])  # cad tambien esta ligada a la programacion funcional