#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 15 00:22:42 2020

@author: llabori
"""

def read_file_bywords(file1):
    
    # Se le pasara a la funcion el nombre del archivo a trabajar 
    list_word = []
    ll = []
    name_file = file1
    
    archivo = open(name_file, "r")
    for line in archivo:
        ll += line.split()
        
    for i in range(0, len(ll)):
        Band  = False
        temp  = []
        temp += ll[i].split()
        if (  ( (ord(temp[0][0]) >= 65) and (ord(temp[0][0]) <= 90) )  or ( (ord(temp[0][0]) >= 97) and (ord(temp[0][0]) <= 122) ) ):
            Band = True
            if Band == True:
                list_word += temp
    
    archivo.close()
    num_words = len(list_word)
    
    return list_word, num_words

def search_reverse_pair(file2):
    
    # Se le pasara a la funcion el nombre del archivo a trabajar
    words_reverses = []
    
    lista, numero = read_file_bywords(file2)
    
    for i in range(0, numero):
        temp  = ""
        temp += lista[i]
        #print(temp)
        temp1 = ""
        temp1 += temp[::-1]
        #print(temp1)
        for j in range(i+1, numero):
            temp2  = ""
            temp2 += lista[j]
            #print(temp2)
            temp3  = ""
            temp3 += temp2[::-1]
            #print(temp3)
            if ( (temp == temp3) and (temp2 == temp1) ):
                inc  = []
                inc += [[temp, temp2]]
                words_reverses += inc
    
    return words_reverses
        
file_name = "words.txt"
words_r = search_reverse_pair(file_name)
print("Las palabras que reversan mutuamente son:")
print(words_r)