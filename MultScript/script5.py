#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb  8 00:58:23 2020

@author: llabori
"""
""" Ejemplo de Metodos Especiales """
class Clase():
    
    def __new__ (cls):                # No se requiere el Self, este motodo se ejecuta y luego 
         print("New")                 # se ejecuta el init (Trabajo estandar de Python)
         return super().__new__(cls)  # Con esto se esta devolviendo una instancia, si no se ustiliza no se ejecuta el metodo especial New
    
    def __init__ (self):              # Tareas de inicializacion
        print("Init")
    
C = Clase()
