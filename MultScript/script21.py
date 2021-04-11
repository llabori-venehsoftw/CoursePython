#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 10 20:26:34 2020

@author: llabori
"""
""" Segundo ejemplo con expresiones regulares """

import re

if (re.search("\Aa[0-9].*(end|fin)$","a5 es una marca de fin")):
    print("Se encontro el patron")