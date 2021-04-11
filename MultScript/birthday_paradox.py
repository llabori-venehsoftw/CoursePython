#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 13 18:07:04 2020

@author: llabori
"""

def fact(n):
    
    #Calculamos el factorial de un numero
    resultado = 1
    if n > 0:
        for i in range(n, 1, -1):
            resultado *= i         
    return resultado
    
def prob_twoequal_date(n):
    
    # Calculamos la aprobabilidad de que al menos 2 personas compartan el mismo dia de cumpleaños
    # en un grupo compuesto por N integrantes
    dias_t= 365
    count_people = n
    
    pi = fact(dias_t) / ( ( dias_t ** count_people) * ( fact(dias_t - count_people) ) )
    pf = 1 - pi
    return pf

prueb = 10
ver = prob_twoequal_date(prueb)
print(ver)