#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 10 17:47:32 2020

@author: llabori
"""
""" Ejemplo con Decorador (No patron Decorador) """
""" Cambia la funcionalidad de una funcion      """

def primerD(funcion):
    def funcionDecorada(*arg,**kkvar):
        print("primer decorador")
    return funcionDecorada

@primerD     # Se llama al decorador
def funcion():
    print("Mi primer decorador")

funcion()
