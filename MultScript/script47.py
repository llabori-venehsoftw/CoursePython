#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 15:23:33 2020

@author: llabori
"""
""" Ejemplo #2 respecto a Loop en python (for) """

# Recorriendo un string con un for
for letter in 'Python':
    print('Current letter = ', letter)

# Recorriendo ua lista con un for
fruits = ['pear', 'melon', 'banana', 'apple', 'mango', 'grapes']
for fruit in fruits:
    print('Current fruit =', fruit)
print('Good Bye 1!')

# Conociendo la longuitud de la lista iterar por la misma a traves del indixe
fruits1 =  ['pear', 'melon', 'banana', 'apple', 'mango', 'grapes', 'watermelon', 'strawberry']
for index in range(len(fruits1)):
    print('Current fruit =', fruits1[index])
print('Good Bye 2!')

# Uso de instruccion else tanto en un ciclo for como en uno while
# Si el Else es utilizado en un ciclo For tal condicion se ejecuta una vez que el ciclo a alcanzado su ultimo valor 
# Si el Else es utilizado en un ciclo While la condicion misma del Else se ejecuta una vez que la variable o la 
# condicion pasa a falso. 
for num in range(10,20):            # La iteraccion se ejecuta entre 10 y 20
    for i in range(2,num):          # La iteraccion se ejecuta entre 2 y el valor actual valor de num
        if num%i == 0:              # To determine the first factor
            j = num/i               # To calculate the second factor
            print('{} equals {} * {}'.format(num,i,j))
            break                   # To move to the next number, the first #FOR
    else:                           # else part of the loop
        print('Este es el primer numero =', num)

