# -*- coding: utf-8 -*-
"""
Created on Sat Aug  1 03:32:34 2020

@author: Jose David
"""

importar  numpy  como  np
importar  pandas  como  pd

lista_numeros  = [ 1 , 2 , 3 , 4 ]
tupla_numeros  = ( 1 , 2 , 3 , 4 )
np_numeros  =  np . matriz (( 1 , 2 , 3 , 4 ))

series_a  =  pd . Serie (
    lista_numeros )

series_b  =  pd . Serie (
    tupla_numeros )

series_c  =  pd . Serie (
    np_numeros )

series_d  =  pd . Serie (
    [ Cierto ,
    falso ,
    12 ,
    12.12 ,
    "Adrian" ,
    Ninguno ,
    ( 1 )
    [ 2 ]
    { "nombre" : "Adrian" }
    ])

print ( series_d [ 3 ])

lista_ciudades   = [
    "Ambato" ,
    "Cuenca" ,
    "Loja" ,
    "Quito" ]

serie_ciudad  =  pd . Serie (
    lista_ciudades ,
    índice  = [
        "A" ,
        "C" ,
        "L" ,
        "Q" ])

print ( serie_ciudad [ 3 ])
print ( serie_ciudad [ "C" ])

valores_ciudad  = {
    "Ibarra" : 9500 ,
    "Guayaquil" : 10000 ,
    "Cuenca" : 7000 ,
    "Quito" : 8000 ,
    "Loja" : 3000
    }

serie_valor_ciudad  =  pd . Serie (
    valores_ciudad )


ciudades_menor_5k  =  serie_valor_ciudad  <  5000

print ( type ( serie_valor_ciudad )) # pandas.core.series.Series '
print ( type ( ciudades_menor_5k ))   # pandas.core.series.Series '
imprimir ( ciudades_menor_5k )


s5  =  serie_valor_ciudad [ ciudades_menor_5k ]

serie_valor_ciudad  =  serie_valor_ciudad  *  1.1

serie_valor_ciudad [ "Quito" ] =  serie_valor_ciudad [ "Quito" ] -  50

print ( "Lima"  en  serie_valor_ciudad )


svc_cuadrado  =  np . cuadrado ( serie_valor_ciudad )


ciudades_uno  =  pd . Serie ({
    "Montañita" : 300 ,
    "Guayaquil" : 10000 ,
    "Quito" : 2000 })

ciudades_dos  =  pd . Serie ({
    "Loja" : 300 ,
    "Guayaquil" : 10000 })

ciudades_uno [ "Loja" ] =  0

imprimir ( ciudades_uno  +  ciudades_dos )
print ( tipo ( ciudades_uno  +  ciudades_dos ))

ciudades_add  =  ciudades_uno . agregar ( ciudades_dos )
# sub ()
# mul ()
# div ()

ciud_concat  =  pd . concat ([
    ciudades_uno ,
    ciudades_dos ])

ciud_concat_verify  =  pd . concat ([
    ciudades_uno ,
    ciudades_dos ],
    verificar_integridad  =  Falso )

ciud_append_verify  =  ciudades_uno . agregar (
    ciudades_dos ,
    verificar_integridad  =  Falso )

print ( ciudades_uno . max ())
print ( pd . Series . max ( ciudades_uno ))
print ( np . max ( ciudades_uno ))

print ( ciudades_uno . min ())
print ( pd . Series . min ( ciudades_uno ))
print ( np . min ( ciudades_uno ))

print ( ciudades_uno . mean ())
print ( ciudades_uno . mediana ())
print ( np . average ( ciudades_uno ))

print ( ciudades_uno . cabeza ( 2 ))
print ( ciudades_uno . tail ( 2 ))


print ( ciudades_uno . sort_values (
    ascendente  =  falso ). cabeza ( 2 ))
print ( ciudades_uno . sort_values (). tail ( 2 ))

# 0 - 1000 5%
# 1001 - 5000 10%
# 5001 - 20000 15%

def  calcular ( valor_serie ):
    if ( valor_serie  <= 1000 ):
        return  valor_serie  *  1.05
    if ( valor_serie  >  1000  y  valor_serie  <=  5000 ):
        return  valor_serie  *  1.10
    if ( valor_serie  >  5000 ):
        return  valor_serie  *  1.15
    
ciudad_calculada  =  ciudades_uno . mapa ( calcular )

# si más
# Cuando NO CUMPLE condicion, aplica 

resultado  =  ciudades_uno . donde ( ciudades_uno  <  1000 ,
                               ciudades_uno  *  1.05 )

series_numeros  =  pd . Serie ([ '1.0' , '2' , - 3 ])

print ( pd . to_numeric ( series_numeros ))

# 'entero', 'firmado', 'sin signo', 'flotante'
imprimir ( pd . to_numeric ( series_numeros , abatidos  =  'entero' ))


series_numeros_err  =  pd . Serie ([ 'no tiene' , '1.0' , '2' , - 3 ])

# ignorar, coaccionar, elevar (predeterminado)
# print (pd.to_numeric (series_numeros_err))
print ( pd . to_numeric ( series_numeros_err , errors = 'ignore' ))
print ( pd . to_numeric ( series_numeros_err , errors = 'coerce' ))



