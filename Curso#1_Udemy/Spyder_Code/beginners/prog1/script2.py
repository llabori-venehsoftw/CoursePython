#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  3 14:25:54 2020

@author: llabori
"""

# Class My Complex Number 
class MyComplexNumber:
    # Constructor Methods
    def __init__(self, real = 0, img = 0):
        print("MyComplexNumber constructor executing...")
        self.real_part = real
        self.img_part = img
        
    def displayComplex(self):
        print("{0} + {1}j".format(self.real_part, self.img_part))
        
# Create a new object a partir de la clase MyComplexNumber
cmplx1 = MyComplexNumber(40, 23)

# Calling displayComplex wiht real = 40 and img = 23
# Output = 40 + 23j
cmplx1.displayComplex()

# Create another object against MyComplexNumber class
# and create a new attribute 'new_attribute'
cmplx2 = MyComplexNumber(60, 70)
cmplx2.new_attribute = 80

# Output {60, 70, 80}
print(cmplx2.real_part, cmplx2.img_part, cmplx2.new_attribute)

# Tratar de imprimir el new_attribute de cmplx1
# cmplx1.new_attribute

# Deleting object attribute and the object
print(cmplx1)
del cmplx1.real_part
del cmplx1
print(cmplx1)