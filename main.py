from app import loginUser, registerUser
from classes.userClass import IuserClassLogin

user = IuserClassLogin
login_func= loginUser.login
register_func= registerUser.registerUser
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
            loginPassword=input("Enter Your Account Password \n >> ")
            user(username, loginPassword)
            login_func()
        #logic if user chose Create Account
        elif userOptions=='2':
            print("\033c")
            print("Welcome, you are one step from managing your password \n"
                "******************************************************")
            userName=input("Enter Your Username \n >> ")
            password=input("Enter Password \n >> ")
            repeatPassWord=input("Repeat Password \n >> ")
            register_func(userName, password, repeatPassWord)
    
        #logic if user opted to exit
        else:
            exit("Exit Successful")

userPrompt()
