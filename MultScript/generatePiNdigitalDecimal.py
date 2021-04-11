#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 17 21:45:21 2020

@author: llabori
"""
""" Generar PI hasta el numero decimal introducido por el teclado """
import math

def pi_ndigit_decimal(number):
    var_pi = math.pi // 1.000
    return var_pi

print(pi_ndigit_decimal(2))