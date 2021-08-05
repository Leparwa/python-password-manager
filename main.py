userOptions=""
while userOptions != '1' or userOptions != '2':
    userOptions= input("WELCOME TO YOUR PASSWORD MANAGER PORTAL !! \n"
                        "*****************************************"
                        "\n1: Login\n-------------------"
                        "\n2: Create Account\n-------------------"
                        "\n3:  Exit \n-------------------\n>>> ")
    if userOptions =='1':
        print("\033c")
        print("Welcome To Your Account")
        userName=input("Enter Your Account Username")
        passWord=input("Enter Your Account Password")

    elif userOptions=='2':
        print("\033c")
        print("Welcome, you are one step from managing your password \n"
            "******************************************************")
        userName=input("Enter Your Username")
        passWord=input("Enter Password")
        repeatPassWord=input("Repeat Password")
    else:
        exit("Exit Success")


