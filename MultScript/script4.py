#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb  8 00:47:25 2020

@author: llabori
"""
""" Ejemplo metodo estatico """

class Persona():
    def __init__ (self):
        pass
    
    def brincar(self):
        print("Brinco")
  
    @classmethod                 # Decorador Metodo de Clase
    def correr(cls):
        print("Corro")
    
    @staticmethod                # Decorador Metodo Estatico
    def nadar():
        print("Nado")

Jose = Persona()
Jose.nadar()