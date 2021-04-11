#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  1 23:59:42 2021

@author: llabori
"""

# True or False
print(5 == 5)
print(5 > 5)

print("----------------------------")

# None
print(None == 0)
print(None == [])
print(None == None)
print(None == False)

print("----------------------------")
def a_void_function():
    a = 1
    b = 2
    c = a + b
    
x = a_void_function()
print(x)

print("----------------------------")
# And, Or, Not
print(True and False)
print(True or False)
print(False or False)
print(not False)

print("----------------------------")
# as
import math as Mymath
print(Mymath.cos(Mymath.pi))

print("----------------------------")
# assert
assert 5 > 4
assert 5 == 5

print("----------------------------")
# Break
for i in range(1,11):
    if i == 5:
        break
    print(i)

print("----------------------------")    
# Continue
for i in range(1,11):
    if i == 5:
        continue
    print(i)
    
print("----------------------------")
# class
class ExampleClass:
    def function1(parameters):
        print("function1 executing.....")
    
    def function2(parameters):
        print("function2 executing ....")
        
obj1 = ExampleClass()
obj1.function1()
obj1.function2()

print("----------------------------")
# def
def function_name(parameters):
    pass
function_name(20)

print("----------------------------")
#  del
a = 30
print(a)
del a
#print(a)

print("----------------------------")
# if...... elif....else
number = 2
if number == 1:
    print("one")
elif number == 2:
    print("two")
else:
    print("Something else")
    
print("----------------------------")
#tray .... raise.... catch.... finally
try:
    x = 9
    raise ZeroDivisionError
except ZeroDivisionError:
    print("Division cannot be performated")
finally:
    print("Execution Succesfully")
    
print("----------------------------")
# for
for i in range (1, 11, 2):
    print(i)
    
print("----------------------------")
# from ..... import
import math
from math import cos
print(cos(10))

print("----------------------------")
# global
globvar = 10
def read1():
    print(globvar)
def write1():
    global globvar
    globvar = 5
def write2():
    globvar = 15
read1()
write1()
read1()
write2()
read1()

    
    






