#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb  8 01:09:24 2020

@author: llabori
"""

""" Propiedades en Python """

class Circulo:

    def __init__(self,radio=1):            # uso de parametro por defecto
        self.radio = radio
    
    @property                              # Decorador de Propiedad
    def area(self):
        return (3.1416) * (self.radio **2)
    
C = Circulo()                              # Objeto instanciado desde la clase circulo
print(C.area)                              # Propiedad area del circulo