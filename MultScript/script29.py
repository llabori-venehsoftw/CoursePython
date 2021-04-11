#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 10 21:17:17 2020

@author: llabori
"""

""" Ejemplo con archivos comprimidos gzip """
 
import gzip

with open('python.docx', 'rb') as original:
    with gzip.open('archivo.txt.gz', 'wb') as archivo1:
        archivo1.writelines(original)
        
