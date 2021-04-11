#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 13 17:41:45 2020

@author: llabori
"""

def has_duplicates(l):
    
    # La suposición inicial es que se le pasara una lista a la funcion
    ans = False
    for i in range(0,len(l)):
        p = l[i]
        for j in range(i+1,len(l)):
            if p == l[j]:
                ans = True
                break
        if ans == True:
            break
    return ans
    
pru = [1,2,3,4,5,6,7,8,9]
ver = has_duplicates(pru)
print(ver)
prue = [1,2,3,4,5,6,7,8,2]
ver2 = has_duplicates(prue)
print(ver2)