#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 13 17:09:57 2020

@author: llabori
"""

def middle(l):
    
    #La suposicion inicial es que se pasa una lista a la funcion
    lnew = l[1:(len(l) -1)]
    return lnew
            
p = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
n = middle(p)
print(n)
print(p)
