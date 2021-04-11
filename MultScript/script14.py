#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 10 17:42:12 2020

@author: llabori
"""
""" Ejemplo con generador o Generadores """
def numeros():
    n = 1
    while True:
        yield n
        n = n+1

i = numeros()
print(i)
print(i.__next__())
print(i.__next__())