#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 10 17:11:01 2020

@author: llabori
"""
""" Deinir Excepciones en Python """
class Err(Exception):
    
    def __init__(self,valor):
        print("Fue el error por: ", valor)
    
try:
    raise Err(4)
except:
    print(" Error escritos ")