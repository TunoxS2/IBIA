import Users as u

def main():
    __data_list = u.Recolect_data()
    __user_founded = u.Find_user(__data_list[4])

    if __user_founded:
        __index = 0

        while True:
            try:

                if u.Locate_user(__index, __data_list[4]):
                    __counter = u.Review_counter(__index)

                    if __counter == 1:
                        u.Add_checkin(__index)
                        return 0
                    else:


            __index+=1
            except IndexError:
                break
    else:
        u.insert_user(__data_list)
    return 0

if __name__ == '__main__':
    main()

# ------------------------------------------------------------------------------

# PROGRAMA ESCRITO EN PYTHON 2.7.15
