#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 13 21:18:28 2020

@author: llabori
"""

def read_file1(f):
    
    # Se le pasara un string contentivo del nombre que corresponde al archivo a leer
    list_word = []

    name_file = f
    file = open(name_file, "r")
    for linea in file:
        list_word += linea.split()
    file.close()
    return list_word


def read_file2(f):
    
    # Se le pasara un string contentivo del nombre que corresponde al archivo a leer
    list_word = []
    
    name_file = f
    file = open(name_file,"r")
    for linea in file:
        for word in linea.split():
            list_word.append(word)
    file.close()
    return list_word
    
archivo = "words.txt"
list1 = read_file1(archivo)
print(list1)
print(len(list1))
print("------------------------------------")
list2 = read_file2(archivo)
print(list2)
print(len(list2))