#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 10 18:44:13 2020

@author: llabori
"""
""" Ejemplo con expresiones regulares """
""" Alternacion, Cuantificacion, Agrupacion """
""" Patrones """
import re
#letras = re.search(r"k","kilo912metros")        # Busca la letra K dentro del string
#letras = re.search(r"\d\d\d","kilo912metros")   # Busca un patron de 3 digitos

patron= re.compile("\d\d\d")                     # Otra forma de hacer una busqueda pero ya a traves de un patron
letras = patron.search("kilo912metros").group()  # Aqui se va a imprimir el patron que se esta buscando de existir el mismo
print(letras)