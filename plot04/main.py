#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 11 01:36:21 2020

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

#sns.lmplot("gdpPercap", "lifeExp", df).set_axis_labels("GDP per capita", "Life Expectancy")
#ax = sns.scatterplot(x="gdpPercap",y="lifeExp",data=df)
#ax.set(xlabel="GDP per capita", ylabel="Life expectancy")

sns.scatterplot("gdpPercap","lifeExp",data=df)
plt.xlabel("GDP per capita", fontsize= 12)
plt.ylabel("Life expectancy", fontsize= 12)
plt.title("People live longer in richer countries")
plt.show()
#plt.savefig("GDPlife.png")
