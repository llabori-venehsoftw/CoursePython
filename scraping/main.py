# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#import requests

#url = "https://www.bbc.com/news"

#response = requests.get(url)
#print(response.text[:1000])

#importamos las libreria a utilizar
import requests
from bs4 import BeautifulSoup

#direccion url a analizar
url = "https://www.bbc.com/news"

#obtenemos los datos desde l url
response = requests.get(url)
html = response.text

#ejecutamos el parseo de la informacion
soup = BeautifulSoup(html, "html.parser")
links = soup.findAll("a")

#for link in links:
#    print(link.get("href"))

#obtenemos solo los link internos no los externos
for link in links:
    href = link.get("href")
    if href.startswith("/news") and href[-1].isdigit():
        print(href)