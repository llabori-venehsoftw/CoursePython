#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 10 20:45:51 2020

@author: llabori
"""
""" Ejemplo de lectura/escritura archivos """
from xml.dom.minidom import parse,Node

xmltree = parse("note.xml")
for nodo in xmltree.getElementsByTagName('pro'):
    for nodo_hijo in nodo.childNodes:
        if nodo_hijo.nodeType==Node.TEXT_NODE:
            print(nodo_hijo.data)