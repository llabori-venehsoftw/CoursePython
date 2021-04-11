#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan  3 00:29:48 2020

@author: llabori
"""
# Variables generales en Python 3.7.1
start = 1   # variable 1
Low = 23    # variable 2
Get = 23.43 # variable 3

# Operaciones matematicas
resultado1 = start * Low
resultado2 = Low * Get
resultado3 = Get + Low
resultado4 = Get/Low

print(resultado1,end='\n')
print(resultado2,end='\n')
print(resultado3,end='\n')
print(resultado4,end='\n')
print(resultado1, resultado2, sep=' ', end='\n')
print(resultado3, resultado4, sep=' ', end='\n')
s = 'First line.\nSecond line.'
print(s)
print(r'C:\some\name')
print("""\
Usage: thingy [OPTIONS]
     -h                        Display this usage message
     -H hostname               Hostname to connect to
""")

# Concatenacion de String
s = 3
s1 = 'der'
s2 = 'ver'
s3 = 'fer'
s4 = s2 + s3
s5 = 3 * s4
s6 = s1 + s2 + s3 + s4 + s5
print(s4,end='\n')
print(s5,end='\n')
print(s6,end='\n')

# Un Entero + String no es factible de ejecutarlo
s7 = s +s1
print(s7,end='\n')
