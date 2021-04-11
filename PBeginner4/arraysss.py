#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  1 22:52:34 2021

@author: llabori
"""

# Defining and declaring ans array
arr = [34, 56, 6, 78, 90, 45]
print(arr)

# Accesing Array Elements
print(arr[0])
print(arr[1])
print(arr[2])
print(arr[-1])
print(arr[-2])

brands = ["apple", "toyota", "pepsi", "ford", "colgate", "lenovo"]
print(brands)

# Finding the Lenght of array
number_brands = len(brands)
print(number_brands)

" Adding one element to array with append() "
brands.append("intel")
print(brands)
print(len(brands))

# Removing elements from a array
colors = ["blue", "yellow", "green", "black", "white", "purple", "red"]
del colors[4]
print(colors)

colors.remove("blue")
colors.pop(3)
print(colors)
print(len(colors))

# Modifying elements of an array using indexing
fruits = ["orange", "apple", "lemon", "strawberry", "pear", "tomato", "banana"]
print(fruits)
fruits[4] = "onion"
fruits[5] = "melon"
print(fruits)

# Concatening two array using + operator
comp  = [1, 2, 6, 8]
comp += [23, 56, 89]
print(comp)

" Repeating elements in an array "
repeat = ["z"]
print("first repeat")
repeat = repeat * 5
print(repeat)
repeat = ["z"]
print("second repeat")
repeat *= 5
print(repeat)

" Slicing an array "
fruits = ["orange", "apple", "lemon", "strawberry", "pear", "tomato", "banana"]
print("Primera seccion")
print(fruits[:4])
print("Segunda seccion")
print(fruits[1:5])
print("Tercera seccion")
print(fruits[3:])
print("Cuarta seccion")
print(fruits[:-1])

# Declaring and defining multidimensional Array
multi = [ [1, 4], [34, 67], [23, 89], [2, 6]]
print(multi)
print(multi[1])
print(multi[1][1])
print(multi[0][1])

