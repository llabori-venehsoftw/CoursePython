#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 11 00:44:36 2020

@author: llabori
"""
# Se importan las librerias a utilizar
import requests
import seaborn as sns
import pandas as pd
from matplotlib import pyplot as plt
import numpy as np

# Este es la dirección del archivo CVS desde donde se extraera la información a manipular
data_url="https://raw.githubusercontent.com/holtzy/data_to_viz/master/Example_dataset/4_ThreeNum.csv"
# Se obtiene la data
r = requests.get(data_url)
# Escribimos la información en un archivo .txt
with open("gdp-life.txt", "w") as f:
    f.write(r.text)
# Leemos los datos del archivo txt (Que tiene campo separado spor coma)
# empleando pandas
df = pd.read_csv("gdp-life.txt")
print(df.head())

print("---")
print("The correlation is:", np.corrcoef(df["gdpPercap"], df["lifeExp"])[0,1])
print("---")

sns.lmplot("gdpPercap", "lifeExp", df, hue="continent").set(xlabel="GDP per capita", ylabel="Life Expectancy")
plt.title("People live longer in richer countries")
plt.tight_layout()
#plt.show()
plt.savefig("GDPlife.png")
