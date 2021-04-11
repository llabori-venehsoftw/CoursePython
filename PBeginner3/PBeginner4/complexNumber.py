#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  1 22:29:05 2021

@author: llabori
"""

class MyComplexNumber:
    # Constructor methode
    def __init__(self, real = 0, imag = 0):
        print("MyComplex Number contructor executing....")
        self.real_part = real
        self.imag_part = imag
        
    def displayComplex(self):
        print(" {0} + {1}j".format(self.real_part, self.imag_part))
        
# Instaciamos un objeto de la clase

complex1 = MyComplexNumber(40, 50)
complex1.displayComplex()

# Instanciamos otro objeto de la misma clase

complex2 = MyComplexNumber(60, 70)
complex2.new_attribute = 80
complex2.displayComplex()
print((complex2.real_part, complex2.imag_part, complex2.new_attribute))

# But complex1 no posee valor en el parametro new_attribute
#complex1.new_attribute

print(complex1)
del complex1.real_part
del complex1

print(complex1)



