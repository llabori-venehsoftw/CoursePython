#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 10 20:40:56 2020

@author: llabori
"""
""" Ejemplo de modificadores """
import re

regex = re.compile(r"ab", re.IGNORECASE)                  # Uso de modificadores
mostrar = regex.search("fgfhdhgdjkpituyertabfcavfbgrtt")
print(mostrar)