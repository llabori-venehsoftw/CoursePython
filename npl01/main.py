#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 10 22:33:32 2020

@author: llabori
"""

import spacy

print(spacy.__version__)

nlp = spacy.load("en_core_web_sm")
doc = nlp("The quick brown fox jumps over the lazy dog.")
for token in doc:
    print(token.text)
    
"""
En este script se importa una libreria para ejecutar Natural Lenguague procesing
A la libreria se le pasa el modelo en_core_web_sm y finalmente se le 
suministra una cadena para que separe la misma en las palabras/caracteres
que contiene tal cadena 

Con estos comando se ejecuto la instalación tanto de la libreria como
del modelo utilizado

# pip install spacy
# python -m spacy download en_core_web_sm

"""