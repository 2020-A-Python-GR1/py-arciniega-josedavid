# -*- coding: utf-8 -*-
"""
Created on Sat Aug  1 03:44:10 2020

@author: Jose David
"""


# d_lectura_csv.py

# 03_pandas
# d_lectura_csv.py
# datos
# artworw.csv

importar  pandas  como  pd
importar  os

ruta  =  "/ inicio / dev-11 / Documentos / Github / py-eguez-sarzosa-vicente-adrian / 03 - Pandas / data / artwork_data.csv"

# "C: // Usuarios // USRBET // Documentos // GitHub // py-eg"
# "./data/artwork_data.csv"

df1  =  pd . read_csv (
    ruta ,
    nrows = 10 )

columnas  = [ 'id' , 'artist' , 'title' ,
            'medio' , 'año' ,
            'adquisiciónYear' , 'height' ,
            'ancho' , 'unidades' ]

df2  =  pd . read_csv (
    ruta ,
    nrows = 10 ,
    usecols  =  columnas )

df3  =  pd . read_csv (
    ruta ,
    usecols  =  columnas ,
    index_col  =  'id' )



path_guardado  =  "/ home / dev-11 / Documentos / Github / py-eguez-sarzosa-vicente-adrian / 03 - Pandas / data / artwork_data.pickle"
# artwork_data.pickle

df3 . to_pickle ( path_guardado )

df4  =  pd . read_pickle ( path_guardado )



