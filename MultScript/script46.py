#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 17 12:00:44 2020

@author: llabori
"""
""" Ejemplo #1 Respecto a Loop en Python (While) """

# Loop conteniendo un ciclo particular de valores
count = 0
while count < 9:
    print(count)
    count = count + 1
print("Fin de la ejecucion")

# Loop infinito
var = 1
while var == 1:    # Esto desarrolla un Loop infinito
    num = input("Enter a number :")    # En Python 2 la funcion a utilizar es raw_input(). Recordar que siempre retorna un String
    print(" You entered =", num)
print("Good Bye!")

