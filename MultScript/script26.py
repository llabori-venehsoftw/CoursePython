#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 10 21:02:42 2020

@author: llabori
"""
""" Ejemplo de lectura archivo Json """
import json

with open('note.json') as file:
    data=json.load(file)
    print(data)
    print(data['clientesA'])