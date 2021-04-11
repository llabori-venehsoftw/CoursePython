#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  7 23:45:55 2020

@author: llabori
"""
""" Ejemplo Variables de Instancia y Metodo de Instancias """
class Persona():
   
   edad = 18  # Variable de clase
   def __init__(self, nombre, nacionalidad):
        self.nombre = nombre              # Variable de Instancia
        self.nacionalidad = nacionalidad  # Variable de Instancia
        
   def nadar(self):                       # Metodo de Instancia
       print("Estoy nadando")
       
persona1 = Persona("Jose", "Mexicano")
print(Persona.edad)
print(persona1.nombre)
print(persona1.nacionalidad)
persona1.nadar()