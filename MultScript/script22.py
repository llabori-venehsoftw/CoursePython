#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 10 20:34:41 2020

@author: llabori
"""
""" Ejemplo de busqueda + Sustitucion """
import re

#mostrar = re.sub(r"\d","*","mang8uera990")     #Sustitucion de digitos por asteriscos
mostrar = re.sub(r"\d","*", "mang8uera990",2)   # Sustitucion de los primeros 2 digitos por asteriscos
print(mostrar)