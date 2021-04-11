#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 10 21:30:01 2020

@author: llabori
"""

import math

def solve_quadratic(a,b,c):
    d =  (b ** 2) - 2 * a * c
    s1 = (-b + math.sqrt(d)) / ( 2 * a)
    s2 = (-b - math.sqrt(d)) / ( 2 * a)
    return s1, s2