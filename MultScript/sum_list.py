#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 13 16:35:53 2020

@author: llabori
"""

def nested_sum(l):
    
    #La suposicion inicial es que se pasara una lista de lista a la funcion
    sum = 0
    for lm in l:
        for lmm in lm:
            sum += lmm
    return sum

t = [[1,2,3], [4], [5,6]]
Total = nested_sum(t)
print(Total)