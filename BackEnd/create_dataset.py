# MACRO ALGORITMO

"""
HACER UN PROGRAMA QUE:

    1. PIDA LA CANTIDAD DE CASOS DE PRUEBA (OMITIR ESTA PASO)

    2. POR CADA CASO DE PRUEBA, PIDA EL NOMBRE, LA CEDULA, EL CELULAR

    3. BUSQUE LA CEDULA EN EL ARCHIVO CSV

    4. SI NO LA ENCUENTRA, CREAR UN EXAMPLE:
            * NOMBRE
            * CEDULA
            * CELULAR
            * CONTADOR DE REGISTROS
            * HORA DEL PRIMER REGISTRO

    5. SI LA ENCUENTRA, REVISE EL CONTADOR DE REGISTROS:

        5.1 SI CONTADOR ESTA ENTRE 1 Y 4, AUMENTE EN 1 EL CONTADOR E INGRESE LA
            HORA DEL REGISTRO EN UNA NUEVA COLUMNA

        5.2 SI CONTADOR ES MAYOR A 4, COMPARE EL VALOR DE LA HORA DEL REGISTRO
            ACTUAL AL ULTIMO REGISTRO, SI HAY UNA DIFERENCIA MENOR A MEDIA HORA,
            ASIGNAR UN VALOR 1 A UNA CARACTERISTICA LLAMADA MARKED

                5.2.1 PARA CALCULAR EL PROMEDIO:
                            * GENERAR DOS VARIABLES (PROMEDIO Y DIFERENCIA)
                            * HACER UN CICLO QUE RECORRA TODA LA FILA
                            * GENERE LA DIFERENCIA DE HORAS E IR CREANDO UNA
                              SUMATORIA
                            * UNA VEZ TERMINADA SE DIVIDE SOBRE EL LARGO
                              DE LA FILA


    6. CREE UN NUEVO ARCHIVO CSV QUE TENGA SOLO:
        * LA CEDULA
        * EL PROMEDIO DE TIEMPO ENTRE REGISTROS
        * EL VALOR DE MARKED (0-1)

    7. RETORNE EL NUEVO ARCHIVO CSV LISTO PARA INGRESAR A CECI
"""

import time
import pandas as pd
import calendar
import csv

def create_dataset():

    # OBTENER LOS DATOS DEL USUARIO

    usuario = raw_input("Ingrese nombre de usuario: ")
    password = raw_input("Ingrese password: ")

    nombre = raw_input("Ingrese el nombre real: ")
    cedula = input("Ingrese el numero de la cedula: ")
    celular = input("Ingrese el numero de celular: ")


    # BUSCAR LA CEDULA EN EL DATASET
    read_data = pd.read_csv('dataset.csv', header = 0)
    __ced_buscar = read_data["CEDULA"]
    __ced_buscar_1 = __ced_buscar[__ced_buscar == cedula]

    # CREAR UN DATASET COMPARATIVO EN CASO DE NO ENCONTRAR LA CEDULA
    __ced_buscar_comp = __ced_buscar[__ced_buscar == 234565432345678876543]

    if __ced_buscar_1.shape == __ced_buscar_comp.shape:
        # SI ENTRA AQUI, NO SE ENCUENTRA EL USUARIO EN EL DATASET

        # INSERTAR EL CONTENIDO AL DATASET
        data = []
        contador = 1
        __hora = time.strftime("%H:%M:%S")
        lista = [usuario, password, nombre, cedula, celular, contador, __hora]
        data.append(lista)
        my_df = pd.DataFrame(data)
        my_df.to_csv('dataset.csv', mode = 'a', index = False, header = False,
                     sep=",")
    else:
        # SI ENTRA AQUI, EL USUARIO FUE ENCONTRADO EN EL DATASET

        # EVALUAR EL VALOR DEL CONTADOR DEL USUARIO
        __i = 0
        row_data = read_data.ix[__i:__i]
        while True:
            row_data = read_data.ix[__i:__i]
            row_contador = row_data.ix[:,5]
            try:
                #print("la fila ", __i, " tiene contador: ", list(row_contador)[0])
                # SI EL VALOR ESTA ENTRE 1-4, CONTADOR+=1 Y NUEVA HORA
                __counter = int(list(row_contador)[0])
                if __counter > 0 and __counter < 5:
                    __counter+=1
                    

                __i+=1
            except IndexError as e:
                break






        # SI EL VALOR ES >4 , CALCULAR PROMEDIO HORAS Y DIAGNOSTICAR MARKED







# -----------------------------------------------------------------------------

def main():
    create_dataset()

if __name__ == '__main__':
    main()
