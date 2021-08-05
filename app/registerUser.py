from app.manageFile import writeRegisterUserFile
write_register_func = writeRegisterUserFile
def registerUser(userName, password, repeatPassword):
    if(password==repeatPassword):
        write_register_func(userName, password)
        print("register successfull")
        
    elif(password != repeatPassword):
        print("passwords do not match")
    else:
        exit()
