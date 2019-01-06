"""
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

list_names= ["USUARIO","PASSWORD","NOMBRE","CEDULA",
             "CELULAR","CONTADOR","HORA 1","HORA 2",
             "HORA 3","HORA 4","HORA 5","HORA 6","HORA 7",
             "HORA 8","HORA 9","HORA 10","HORA 11","HORA 12",
             "HORA 13","HORA 14","HORA 15","HORA 16","HORA 17",
             "HORA 18","HORA 19","HORA 20","HORA 21","HORA 22",
             "HORA 23","HORA 24","PROMEDIO","MARKED"]

def restar_hora(self,hora1,hora2):
        formato = "%H:%M:%S"
        h1 = datetime.strptime(hora1, formato)
        h2 = datetime.strptime(hora2, formato)
        resultado = h1 - h2
        return str(resultado)


def create_dataset():

    # OBTENER LOS DATOS DEL USUARIO

    usuario = raw_input("Ingrese nombre de usuario: ")
    password = raw_input("Ingrese password: ")

    nombre = raw_input("Ingrese el nombre real: ")
    cedula = input("Ingrese el numero de la cedula: ")
    celular = input("Ingrese el numero de celular: ")


    # BUSCAR LA CEDULA EN EL DATASET
    read_data = pd.read_csv('dataset.csv', header = None, names=list_names)
    __ced_buscar = read_data["CEDULA"]
    __ced_buscar_1 = __ced_buscar[__ced_buscar == cedula]

    # CREAR UN DATASET COMPARATIVO EN CASO DE NO ENCONTRAR LA CEDULA
    __ced_buscar_comp = __ced_buscar[__ced_buscar == 234565432345678876543]

    if __ced_buscar_1.shape == __ced_buscar_comp.shape:
        # SI ENTRA AQUI, NO SE ENCUENTRA EL USUARIO EN EL DATASET

        # INSERTAR EL CONTENIDO AL DATASET
        contador = 1
        data = []
        __hora = time.strftime("%H:%M:%S")
        lista = [usuario, password, nombre, cedula, celular, contador, __hora]
        data.append(lista)
        my_df = pd.DataFrame(data)
        my_df.to_csv('dataset.csv', mode = 'a', index = False, header = False,
                     sep=",")
    else:
        # SI ENTRA AQUI, EL USUARIO FUE ENCONTRADO EN EL DATASET

        # CREA UN SISTEMA PARA RECORRER EL DATASET POR FILAS
        __i = 0
        row_data = read_data.ix[__i:__i]
        while True:

            # CREA UN TRY/EXCEPT PARA CAPTURAR EL ERROR AL SUPERAR EL INDEX
            try:

                # BUSCA MEDIANTE UN IF EL USUARIO DESEADO
                __var = read_data.loc[__i, "CEDULA"]

                if str(__var) == str(cedula):

                    # ANALIZA SI EL CONTADOR DE REGISTROS ESTA ENTRE 1-4
                    if int(read_data.loc[__i, "CONTADOR"]) > 0 and int(read_data.loc[__i, "CONTADOR"]) < 5:


                        # INGRESA LA NUEVA HORA
                        print(str(read_data[read_data["CEDULA"] == 1004752250]))
                        # CONTADOR PARA SABER CUANTAS HORAS DEBE TENER
                        __counter_hours = int(read_data.loc[__i, "CONTADOR"])

                        read_data.iloc[__i, 6 + __counter_hours] =  time.strftime("%H:%M:%S")


                        # AUMENTA EN 1 EL CONTADOR DE REGISTROS
                        read_data.loc[__i, "CONTADOR"] = int(read_data.loc[__i, "CONTADOR"]) + 1

                        read_data.to_csv('dataset.csv', index = False, header = False,
                                     sep=",")
                        break
                    else:

                        # AQUI SE DEBE SACAR EL PROMEDIO ENTRE HORA DE REGISTROS

                        # SACA EL CONTADOR ACTUAL DE REGISTROS DEL USUARIO
                        __counter_hours = int(read_data.loc[__i, "CONTADOR"])

                        # LISTA DONDE SE ALMACENARAN LAS DIFERENCIAS ENTRE HORAS DE REGISTRO
                        __list_dif = []

                        # CALCULA EL PROMEDIO DE TIEMPO ENTRE REGISTROS

                        for __j in range(7, 7+__counter_hours):

                            # EVALUA SI LA HORA ACTUAL ES LA ULTIMA
                            if read_data.loc[__i,__j+1] == "nan":
                                break

                            __hour_actual = read_data.loc[__i,__j]
                            __hour_previous = read_data.loc[__i,__j-1]

                            __h_diference = restar_hora(__hour_actual, __hour_previous)

                            # FORMATO HORA <00:00:00>(HORA: 0-1)(MINUTOS: 3-4)(SEGUNDOS 6-7)

                            _test_hour = int(__h_diference[0:1])
                            _test_min = int(__h_diference[3:4])

                            #if _test_hour == 0 and _test_min <



                # ANALIZA SI ES PARAMETRO ACTUAL ES EL ULTIMO EN LAS FILAS
                # SI LO ES, SALTARA INDEXERROR
                __analizer_next = list(read_data.ix[__i+1:__i+1].ix[:,5])[0]

                __i+=1

            except IndexError:
                break




        # SI EL VALOR ES >4 , CALCULAR PROMEDIO HORAS Y DIAGNOSTICAR MARKED







# -----------------------------------------------------------------------------

def main():
    create_dataset()

if __name__ == '__main__':
    main()
