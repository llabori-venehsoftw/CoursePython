#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 10 18:20:32 2020

@author: llabori
"""
""" Segundo ejemplo con funciones de ordenes superior"""
def saludo(idioma):
    def saludo_es():
        print("HOLA")
    def saludo_en():
        print("HI")
    idioma_func = {"es":saludo_es, 
                   "en":saludo_en}    # Esto es un diccionario
    return idioma_func[idioma]
    
saludar=(saludo("es"))
saludar()