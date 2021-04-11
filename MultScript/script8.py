#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb  8 01:27:04 2020

@author: llabori
"""
""" Trabajar con la instrospeccion """

class Introsp():
    Introspver = 9               # Con esto podemos constatar la existencia o no del valor en la clase
    def __init__(self,valor):
        self.valor = valor
        
    def segundo(self):
        print("Segundo")
        
    def tercero(self):
        print("Tercero")

dato = Introsp("Valor")
dir(dato)                         # Con esta instruccion se formaliza la instrospeccion
print(dir(dato))
print(isinstance(dato,Introsp))   # Le preguntamos si un dato es una instancia de una clase Preguntamos por Dato, Deberia devolver True o False
print(hasattr(dato,"Introspver")) # Le preguntamos si dato tiene el atributo Instrospver ( O puede acceder al mismo )