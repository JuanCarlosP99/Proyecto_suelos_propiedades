# -*- coding: utf-8 -*-
"""
Created on Wed Dec 25 11:13:57 2024

@author: pared
"""

import pandas as pd
import numpy as np

datos = pd.read_csv('dataset_soil.csv')
print(datos.info())
print(datos.head())

nuevo = pd.DataFrame(datos)
print(nuevo)
nuevo=nuevo.replace(np.nan, "0")
print("\n"*5)
print("***************Impresión son NaN*************")
print(nuevo.info())
print("\n"*5)
print("***************Estadisticas sin NaN***************")
print(nuevo.describe())
print("\n"*5)
print("*******Estadisticas solamente numeros*******")
print(nuevo.describe(include=[np.number]))
print("\n"*5)
## nuevo = nuevo.replace("N/A", "0")

## Convertir datos tipo texto a numero
## nuevo['nombre_de_columna'] = nuevo.nombre_de_columna.astype(int)
