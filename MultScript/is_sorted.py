#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 13 17:27:14 2020

@author: llabori
"""

def is_sorted(l):
    
    #La suposicion inicial es que se le suministrara una lista a la funcion
    
    Lmod = sorted(l)
    if Lmod == l:
        ans = True
    else:
        ans = False    
    return ans

p = [2, 3, 4, 5, 6]
prueba = is_sorted(p)
print(prueba)
v= [ 3, 1, 0, 4, 23]
prueba2 = is_sorted(v)
print (prueba2)