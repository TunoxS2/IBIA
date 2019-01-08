def F_user(Email, Password):
    email_dt = pd.read_csv("dataset.csv", usecols=[2],header=0)
    pass_dt = pd.read_csv("dataset.csv", usecols=[3],header=0)

    if len(email_dt["EMAIL"]==Email) > 0 and len(pass_dt["PASSWORD"]) >0:
        return "verde"
    else:
        return "rojo"

# ------------------------------------------------------------------------------
