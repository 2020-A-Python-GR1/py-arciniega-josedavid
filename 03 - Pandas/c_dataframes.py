# -*- coding: utf-8 -*-
"""
Created on Sat Aug  1 03:39:05 2020

@author: Jose David
"""


# c_dataframes.py

import numpy as np
import pandas as pd

arr_pand = np.random.randint(0,10,6).reshape(2,3)

df1 = pd.DataFrame(arr_pand)

s1 = df1[0]

# operacion con la serie

s2 = df1[1]

s3 = df1[2]

df1[3] = s1

df1[4] = s1 * s2


datos_fisicos_uno = pd.DataFrame(
    arr_pand,
    columns = [
        'Estatura (cm)',
        'Peso (kg)',
        'Edad (anios)'])

datos_fisicos_dos = pd.DataFrame(
    arr_pand,
    columns = [
        'Estatura (cm)',
        'Peso (kg)',
        'Edad (anios)'],
    index = [
        'Adrian',
        'Vicente'])

serie_peso = datos_fisicos_dos['Peso (kg)']
datos_adrian = serie_peso['Adrian']
print(serie_peso)
print(datos_adrian)


df1.index = ['Adrian', 'Vicente']
df1.index = ['Wendy', 'Carolina']
df1.columns = ['A', 'B', 'C', 'D', 'E']
