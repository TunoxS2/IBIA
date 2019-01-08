# LIBRARIES

# PANDAS
import pandas as pd
# TIME
import time
# DATETIME
from datetime import datetime
# ------------------------------------------------------------------------------
def Recolect_data():
    __username = raw_input("Username: ")
    __password = raw_input("Password: ")
    __email = raw_input("Email: ")
    __name = raw_input("Real name: ")
    __id = input("ID number: ")
    __cellphone = input("Cellphone number: ")
    __counter = 1
    __hour = time.strftime("%H:%M:%S")

    __list = [__username, __password, __email, __name, __id, __cellphone,
               __counter, __hour]
    return __list

# ------------------------------------------------------------------------------

def Columns_names():
    __list_names= ["USER","PASSWORD","EMAIL","NAME","ID","CELLPHONE","COUNTER",
               "HOUR 01","HOUR 02","AVERAGE 1","HOUR 03","HOUR 04","AVERAGE 2",
               "HOUR 05","HOUR 06","AVERAGE 3","HOUR 07","HOUR 08","AVERAGE 4",
               "HOUR 09","HOUR 10","AVERAGE 5","HOUR 11","HOUR 12","AVERAGE 6",
               "HOUR 13","HOUR 14","AVERAGE 7","HOUR 15","HOUR 16","AVERAGE 8",
              "HOUR 17","HOUR 18","AVERAGE 9","HOUR 19","HOUR 20","AVERAGE 10",
             "HOUR 21","HOUR 22","AVERAGE 11","HOUR 23","HOUR 24","AVERAGE 12",
             "HOUR 25","HOUR 26","AVERAGE 13","HOUR 27","HOUR 28","AVERAGE 14",
             "HOUR 29","HOUR 30","AVERAGE 15","HOUR 31","HOUR 32","AVERAGE 16",
             "HOUR 33","HOUR 34","AVERAGE 17","HOUR 35","HOUR 36","AVERAGE 18",
             "HOUR 37","HOUR 38","AVERAGE 19","HOUR 39","HOUR 40","AVERAGE 20",
             "AVERAGE","ANALYZE","MARKED",]
    return __list_names

# ------------------------------------------------------------------------------

def insert_user(__data):
    __list = []
    __list.append(__data)
    __dataset = pd.DataFrame(__list)
    __dataset.to_csv('dataset.csv', mode = 'a',
                                  index = False,
                                  header = False,
                                  sep=",")
    return

# ------------------------------------------------------------------------------

def Find_user(__ID):
    __list_names = Columns_names()
    __dataset =pd.read_csv('dataset.csv', header = None, names=__list_names)

    __zeus = __dataset["ID"]
    __zeus_1 = __zeus[__dataset["ID"] == __ID]
    __zeus_calvo = __zeus[__zeus == 2345654345432345422345]

    if __zeus_1.shape == __zeus_calvo.shape:
        return False
    else:
        return True
# ------------------------------------------------------------------------------

def Locate_user(__index, __ID):
    __dataset = pd.read_csv('dataset.csv', header = None, names=Columns_names())
    __user = __dataset.loc[__index, "ID"]

    if str(__user) == str(__ID):
        return True
    else:
        return False


# ------------------------------------------------------------------------------

def Review_counter(__index):
    __dataset =pd.read_csv('dataset.csv', header = None, names=Columns_names())
    return int(__dataset.loc[__index, "COUNTER"])

# ------------------------------------------------------------------------------

def Hour_diference(__hour_2, __hour_1):
    __Format = "%H:%M:%S"
    __previous_hour = datetime.strptime(str(__hour_1), __Format)
    __actual_hour = datetime.strptime(str(__hour_2), __Format)
    return str(__actual_hour - __previous_hour)

# ------------------------------------------------------------------------------

def Even_hour(__index, __column_var):
    # IMPORTAR DATASET Y LISTA DE COLUMNAS
    __dataset = pd.read_csv('dataset.csv', header = None, names=Columns_names())
    __list = Columns_names()
 # -------------------------------------------------------------------------- #
    if __dataset.loc[__index, "ANALYZE"] == 1:

        __dataset.iloc[__index, __column_var] =  time.strftime("%H:%M:%S")
        __dataset.loc[__index, "COUNTER"] = int(__dataset.loc[__index,"COUNTER"]) + 1

        __actual_h = __dataset.iloc[__index, __column_var]
        __previous_h = __dataset.iloc[__index, __column_var-1]
        __diff = Hour_diference(__actual_h, __previous_h)
        _test_hour = int(__diff[0:1])
        _test_min = int(__diff[3:4])

        __da_real_nigga_hours = _test_min + (_test_hour*60)

        if __da_real_nigga_hours <= 65:
            __dataset.loc[__index, "MARKED"] == 1
            __dataset.iloc[__index,__column_var +1] = __diff
            __dataset.to_csv('dataset.csv', index = False, header = False, sep=",")
            return
        else:
            __dataset.loc[__index, "COUNTER"] = int(__dataset.loc[__index,"COUNTER"]) + 1
            __dataset.to_csv('dataset.csv', index = False, header = False, sep=",")
            return
 # -------------------------------------------------------------------------- #
    __dataset.iloc[__index, __column_var] =  time.strftime("%H:%M:%S")
    __dataset.loc[__index, "COUNTER"] = int(__dataset.loc[__index,"COUNTER"]) + 1

    __actual_h = __dataset.iloc[__index, __column_var]
    __previous_h = __dataset.iloc[__index, __column_var-1]
    __diff = Hour_diference(__actual_h, __previous_h)
    _test_hour = int(__diff[0:1])
    _test_min = int(__diff[3:4])

    __da_real_nigga_hours = _test_min + (60 * _test_hour)

    if __da_real_nigga_hours <= 65:
        __dataset.loc[__index,"ANALYZE"] = 1
        __dataset.iloc[__index,__column_var +1] = __diff
        __dataset.to_csv('dataset.csv', index = False, header = False, sep=",")
    else:
        __dataset.to_csv('dataset.csv', index = False, header = False, sep=",")
    return

# ------------------------------------------------------------------------------

def Odd_hour(__index, __column_var):
    __dataset = pd.read_csv('dataset.csv', header = None, names=Columns_names())
    __list = Columns_names()
    __dataset.iloc[__index, __column_var] =  time.strftime("%H:%M:%S")
    __dataset.loc[__index, "COUNTER"] = int(__dataset.loc[__index,"COUNTER"]) + 1
    __dataset.to_csv('dataset.csv', index = False, header = False, sep=",")
    return

# ------------------------------------------------------------------------------

def Locate_hour(__index,__counter):
    __dataset = pd.read_csv('dataset.csv', header = None, names=Columns_names())
    __column_var = 7 + int(__counter)
    __list = Columns_names()
    while True:
        if __list[__column_var][0:4] == "HOUR":

            if __counter % 2 == 0:
                print(__list[__column_var])
                Odd_hour(__index, __column_var)
                print("impar")
                return
            else:
                print(__list[__column_var])
                Even_hour(__index, __column_var)
                print("par")
                return
        __column_var+=1

# INVESTIGAR PROBLEMA AL CARGAR EL 4 REGISTRO
# ------------------------------------------------------------------------------
