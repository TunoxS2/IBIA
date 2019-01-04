# MACRO ALGORITMO

"""
HACER UN PROGRAMA QUE:

    1. PIDA LA CANTIDAD DE CASOS DE PRUEBA

    2. POR CADA CASO DE PRUEBA, PIDA EL NOMBRE, LA CEDULA, EL CELULAR

    3. BUSQUE LA CEDULA EN EL ARCHIVO CSV

    4. SI NO LA ENCUENTRA, CREAR UN EXAMPLE:
            * NOMBRE
            * CEDULA
            * CELULAR
            * CONTADOR DE REGISTROS
            * HORA DEL PRIMER REGISTRO

    5. SI LA ENCUENTRA, REVISE EL CONTADOR DE REGISTROS:

        5.1 SI CONTADOR ESTÁ ENTRE 1 Y 4, AUMENTE EN 1 EL CONTADOR E INGRESE LA
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

from datetime import datetime, date, time, timedelta
import calendar
import csv

def create_dataset():

    a = int(input("ingrese la cantidad de casos de prueba: "))
    for i in range(a):

        #nombre = input("Ingrese el nombre del usuario: ")
        #cedula = input("Ingrese el numero de la cedula: ")
        #   celular = input("Ingrese el numero de celular: ")

"""
        dt = open("dataset_1.csv", "w")
        dt_csv_w = csv.writer(dt)
        data = [["Santiago", 1004752259]]
        dt_csv_w.writerows(data)
        dt.close()
"""


"""
        with open('dataset_1.csv', 'w') as csvfile:
            fieldnames = []
"""

create_dataset()
