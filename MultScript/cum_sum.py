#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 13 16:47:53 2020

@author: llabori
"""

def cumsum(l):
    
    # La asunción inicial es que se le pasara una lista de enteros a la función
    lisf = []
    lisf = l
    total = 0
    for i in range(0,len(l)):
        total += l[i]
        if i == len(l)-1:
            lisf[i] = total
    return lisf

p = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
ver = cumsum(p)
print(ver)
