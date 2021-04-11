#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 17 11:52:00 2020

@author: llabori
"""
""" Ejemplo #4 con operadores de desicion, Contatenacion de If """

var1 = 100
if var1 < 200:
    print("Expression value is less than 200")
    if var1 == 150:
        print("Which is 150")
    elif var1 == 100:
        print("Which is 100")
    elif var1 == 50:
        print("Which is 50")
    elif var1 < 50:
        print("Expression value is less than 50")
else:
    print("Could not fit True expression")
print("Good Bye!")