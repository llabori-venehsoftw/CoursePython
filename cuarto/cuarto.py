#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan  3 01:42:37 2020

@author: llabori
"""

# Los String no pueden ser cambiados y aque lo smismos sin inmutables
'''
s = 'prueba'
print(s,end='\n')
s[0] = 'J'
print(s,end='\n')
'''

# El factible desarrollar nuevos String
s = 'prueba'
S = 'J'
Ss = S + s[1:]
print(Ss, end='\n')

# Podemos ontener la cantidad de caracteres es un String
ss = 'fbdbfbfbfdbfdbfsdfbsdkbfsdkfb'
Long = len(ss)
print(Long,end='\n')