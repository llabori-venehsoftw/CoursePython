#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb  8 00:37:08 2020

@author: llabori
"""
""" Ejemplo uso Metodo de Instancia"""
class Persona():
   
   def __init__(self):                    # Metodo Inicializador
       pass
            
   def despedir(self):                    # Metodo de Instancia
       print("Hasta luego")

   @classmethod                           # Decorador Metodo de Clase, No necesitamos crear el objeto
   def saludar(cls, nombre):              # Metodo de Instancia
       print("Estoy saludando "+nombre)

Persona.saludar("Maria")