#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan  3 21:32:22 2020

@author: llabori
"""

# Flujos de control
# Iniciamos con el condicional If
x = int(input("Introduzca un valor entero = "))
if x < 0:
    x = 0
    print("El valor de X fue ajustado =", x, sep=' ', end='\n')
elif x == 0:
    print(" El valor de x es 0")
elif x == 1:
    print(" El valor de x es igual a la unidad")
else:
    print(" El valor de x es =", x, sep=' ', end='\n')
    
# Trabajemos ahora con el ciclo For
words = [ 'verificar', 'prestaciones', 'puestos']
for w in words:
    print(w, len(w), sep=' tiene ', end=' letras \n')
    
# Recorrido de toda una lista e inclusion de un valor en la misma
# dependiendo de un condicional en particular, utilizaremos el metodo
# insert para incluir een una posicion en particular el valor que
# cumpla con la codicion
for w in words[:]:
    if len(w) < 8:
        words.insert(0, w)
print(words, end='\n')

# Emplearemos la funcion rango para generar un conjunto especifico
# de valores particulares (Si no se eestablece el limite inferior
# el mismo sera considerado como 0)
for i in range(10):
    print("El valor de i es = ", i, end='\n')

# Hagamoslo para un rango en particular, observaremos que el limite 
# superior del rango no se incluye
for j in range(3,26):
    print("El valor de j es = ", j, end='\n')
    
# El rango puede contar con valores de inicio, final y su incremento
for z in range(2, 32, 2):
    print("El valor de w es = ", z, end='\n')

for y in range(-10, -100, -30):
    print("El valor de y es = ", y, end='\n')

# Podemos iterar sobre los valores de una lista podemos utilizar los objetos range()
# y len() para recorrer la misma
palabras = ['prueba', 'prueba2', 'prueba3', 'prueba4']
for q in range(len(palabras)):
    print(" La palabra", q, " es = ", palabras[q], end='\n')

# Para iteraciones tambien podemos utilizar el objeto list() pero primero para el caso
# ejemplificado debemos generar primero el rango
palabras10 = ['minutas', 'frutas', 'verduras', 'hortalizas', 'paltas']
for t in list(range(len(palabras10))):
    print(" La palabra", t, " es = ", palabras10[t], end='\n')
