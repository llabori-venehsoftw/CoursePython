#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 10 17:47:32 2020

@author: llabori
"""
""" Ejemplo de cierres """
def funcionA(x):
    def funcionB(y):
        return(x+y)
    return funcionB

funcion = funcionA(3)
print(funcion(8))

""" Son acciones que se requieren utilizar a la respuesta de algo """