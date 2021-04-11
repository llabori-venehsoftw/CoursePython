#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb  8 01:20:06 2020

@author: llabori
"""
"""  Ejemplo de Polimorfismo """

class Perro():
    
    def avanzar(self):
        print("Tenemos 4 patas")
        
class Perico():
    
    def avanzar(self):
        print("Volar")
        
def mover(animal):                  # Implementacion del Polimorfismo
    animal.avanzar()
    
perro = Perro()
perico = Perico()
perro.avanzar()
perico.avanzar()
mover(perro)
mover(perico)
