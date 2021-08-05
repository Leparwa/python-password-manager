from app import  loginUser, registerUser

#functions in the app folder declaration
register_func = registerUser
login_func=loginUser.login


def userPrompt():
    userOptions=""
    while userOptions != '1' or userOptions != '2':
        userOptions= input("WELCOME TO YOUR PASSWORD MANAGER PORTAL !! \n"
                            "*****************************************"
                            "\n1: Login\n-------------------"
                            "\n2: Create Account\n-------------------"
                            "\n3:  Exit \n-------------------\n>>> ")
        #logic if user chose login
        if userOptions =='1':
            print("\033c")
            username=input("Enter Your Account Username \n >> ")
            passWord=input("Enter Your Account Password \n >> ")
            login_func(username, passWord)

        #logic if user chose Create Account
        elif userOptions=='2':
            print("\033c")
            print("Welcome, you are one step from managing your password \n"
                "******************************************************")
            userName=input("Enter Your Username \n >> ")
            passWord=input("Enter Password \n >> ")
            repeatPassWord=input("Repeat Password \n >> ")
    
        #logic if user opted to exit
        else:
            exit("Exit Successful")

userPrompt()
