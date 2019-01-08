import Users as u

def main():
    # ASK DATA
    __data_list = u.Recolect_data()
    __user_id = __data_list[4]
    __user_founded = u.Find_user(__user_id)
    if __user_founded:
        __index = 0

        while True:
            try:
                if u.Locate_user(__index, __user_id):
                    __counter = u.Review_counter(__index)
                    u.Locate_hour(__index, __counter)
                    break
                __index += 1

            except IndexError:
                break
    else:
        u.insert_user(__data_list)
    return 0

if __name__ == '__main__':
    main()

# ------------------------------------------------------------------------------

# PROGRAMA ESCRITO EN PYTHON 2.7.15
