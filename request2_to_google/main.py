#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 10 22:22:27 2020

@author: llabori
"""

import requests
from bs4 import BeautifulSoup

r = requests.get("https://www.google.com").text
soup = BeautifulSoup(r, "html.parser")
print([x.get("title") for x in soup.findAll("input") if x.get("title")])

"""
Con este script se ejecuta un scrat de la pagina de google se hace la busqueda 
de un boton y se imprime por consola el texto de dicho boton
"""