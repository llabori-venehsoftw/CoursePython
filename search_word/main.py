#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 13 22:21:12 2020

@author: llabori
"""

def read_file_bywords(f1):
    
    # Se le pasara a la funcion el nombre del archivo a trabajar 
    list_word = []
    ll = []
    name_file = f1
    
    archivo = open(name_file, "r")
    for line in archivo:
        ll += line.split()
    #print(ll)
    #print(len(ll))
    
    for i in range(0, len(ll)):
        temp  = []
        Band  = False
        temp += ll[i].split()
        #print(type(temp))
        #print(temp[0][0])
        #print(temp)
        if (  ( (ord(temp[0][0]) >= 65) and (ord(temp[0][0]) <= 90) )  or ( (ord(temp[0][0]) >= 97) and (ord(temp[0][0]) <= 122) ) ):
            Band = True
            if Band == True:
                list_word += temp
    
    archivo.close()
    #return
    return list_word

def search_words(f2,w):
    
    exist = False
    ver = read_file_bywords(f2)
    #print(ver)
    ver.sort()
    long = len(ver)
    
    if ord(w[0]) >= ord(ver[round(long/2)][0]):
        for i in range(round(long/2), long):
            if w == ver[i]:
                exist = True
                break
    else:
        for i in range(0, round(long/2)):
            if w == ver[i]:
                exist = True
                break
    return exist, ver

prueba = "words.txt"
prueba1 = "october"
fin, listorder = search_words(prueba, prueba1)
print(fin)
print(listorder)
#print(listorder[153])
#print(listorder[153][0])