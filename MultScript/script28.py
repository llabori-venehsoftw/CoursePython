#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 10 21:07:10 2020

@author: llabori
"""
""" Ejemplo con archivos comprimidos .zip """
import zipfile
from zipfile import ZipFile

with zipfile.ZipFile('archivo.zip', 'w') as fzip:
    fzip.write('Python.docx')
    fzip.write('Python.jpg')
    fzip.write('Archivo.docx')   
    fzip.printdir()              # Para imprimir todos lo archivos dentro de un zip
    fzip.extracall()             # Para extraer todos los archvos que se encuentran comprimidos en otro