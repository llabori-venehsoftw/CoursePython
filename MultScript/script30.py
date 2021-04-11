#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 10 21:22:26 2020

@author: llabori
"""
""" Ejemplo para comprimir cadenas de caracteres bz2 """

import bz2

cadena = b"Cadena Cadena Cadena Cadena Cadena"
cadena_c=bz2.compress(cadena)
print(bz2.decompress(cadena_c))