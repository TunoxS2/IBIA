# LIBRARIES

# PANDAS
import pandas as pd
# TIME
import time
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
                   "HOUR 1","HOUR 2","AVERAGE 1","HOUR 3","HOUR 4","AVERAGE 2",
                   "HOUR 5","HOUR 6","AVERAGE 3","HOUR 7","HOUR 8","AVERAGE 4",
                "HOUR 9","HOUR 10","AVERAGE 5","HOUR 11","HOUR 12","AVERAGE 6",
               "HOUR 13","HOUR 14","AVERAGE 7","HOUR 15","HOUR 16","AVERAGE 8",
              "HOUR 17","HOUR 18","AVERAGE 9","HOUR 19","HOUR 20","AVERAGE 10",
             "HOUR 21","HOUR 22","AVERAGE 11","HOUR 23","HOUR 24","AVERAGE 12",
             "HOUR 25","HOUR 26","AVERAGE 13","HOUR 27","HOUR 28","AVERAGE 14",
             "HOUR 29","HOUR 30","AVERAGE 15","HOUR 31","HOUR 32","AVERAGE 16",
             "HOUR 33","HOUR 34","AVERAGE 17","HOUR 35","HOUR 36","AVERAGE 18",
             "HOUR 37","HOUR 38","AVERAGE 19","HOUR 39","HOUR 40","AVERAGE 20",
             "AVERAGE","MARKED"]
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

def Hour_diference(self, __hour_1, __hour_2):
    __Format = "%H:%M:%S"
    __previous_hour = datetime.strptime(__hour_1, __Format)
    __actual_hour = datetime.strptime(__hour_2, __Format)
    return str(__actual_hour - __previous_hour)

# ------------------------------------------------------------------------------

def Add_checkin(__index):
    # NEW HOUR
    __dataset =pd.read_csv('dataset.csv', header = None, names=Columns_names())
    __counter_hour = int(__dataset.loc[__index, "COUNTER"])

    __column_var = 7+__counter_hour
    __Flag = True
    __list = Columns_names

    while __Flag:
        if "HOUR" in __list[__column_var]:
            __dataset.iloc[__index, __column_var] =  time.strftime("%H:%M:%S")
        else:
            __column_var+=1

    # INCREASE COUNTER
    __dataset.loc[__index, "COUNTER"] = int(__dataset.loc[__index,
                                                          "COUNTER"]) + 1
    __dataset.to_csv('dataset.csv', index = False, header = False, sep=",")
    return

# ------------------------------------------------------------------------------

def Check_mate():
    return

# ------------------------------------------------------------------------------
