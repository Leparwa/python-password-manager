def userPrompt():
    userOptions=""
    while userOptions != '1' or userOptions != '2':
        userOptions= input("WELCOME TO YOUR PASSWORD MANAGER PORTAL !! \n"
                            "*****************************************"
                            "\n1: Login\n-------------------"
                            "\n2: Create Account\n-------------------"
                            "\n3:  Exit \n-------------------\n>>> ")
        if userOptions =='1':
            print("\033c")
            userName=input("Enter Your Account Username \n >> ")
            passWord=input("Enter Your Account Password \n >> ")

        elif userOptions=='2':
            print("\033c")
            print("Welcome, you are one step from managing your password \n"
                "******************************************************")
            userName=input("Enter Your Username \n >> ")
            passWord=input("Enter Password \n >> ")
            repeatPassWord=input("Repeat Password \n >> ")
            createAction()

        else:
            exit("Exit Successful")

def createAction():
    print("successfull creating Account")

def loginUser():
    print("login success")

def manageUserActivities():
    print("")
userPrompt()    
