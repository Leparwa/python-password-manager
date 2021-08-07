from classes.userClass import IuserClassLogin
from app.manageFile import readRegisteredUserFile, writeUserCrendentialsFile
userInfo =IuserClassLogin
userCrenditials = readRegisteredUserFile
writeCredentials = writeUserCrendentialsFile

isContinueAddMoreAccounts = False

def login():
    print("\033c")
    if(userInfo.user):
        actionsAfterLogin()
    else:
        print("user does not exist")


def viewAll():
    userCrenditials()

def actionsAfterLogin():
    print("\033c")
    print("*********LIST OF CREDENTIALS MANAGED***********\n")
    viewAll()
    loginAction =input("********MANAGE YOUR ACCOUNT***********\n"
          "\t1: add new account\n"
           "\t2: view managed account's credentials\n>>> ")
    if loginAction =='1':
        print("\033c")
        addNewAcount()
        actionAfterAddNewAccount()
    elif loginAction=='2':
        print("\033c")
        viewAll()
        actionAfterViewAll()

    else:
        pass

def addNewAcount():
    userName=input("Enter Account Username  \n >> ")
    password=input("Enter Account Password \n >> ")
    account=input("Enter Account company \n >> ")
    writeCredentials(userName, password, account)

def actionAfterViewAll():
    userChoise =input("************Choose Action********** \n"
                        "\t1: Go back \n"
                        "\t2: Add new account\n"
                        "\t3: Logout\n>>> ")
    if userChoise =='1':
        actionsAfterLogin()
    elif userChoise =='2':
        addNewAcount()
        actionAfterViewAll()
    else:
        exit("Logout Successfully")

def actionAfterAddNewAccount():
    userChoise=''
    userChoise =input("************Choose Action********** \n"
                "\t1: Go back \n"
                "\t2: Add another account\n"
                "\t3: View all managed account's credential\n"
                "\t4: Logout\n>>> ")
    if userChoise =='1':
        actionsAfterLogin()

    elif userChoise =='2':
        print("\033c")        
        addNewAcount()
        while True:
            actionAfterAddNewAccount()

    elif userChoise=='3':
        print("\033c")
        viewAll()
        actionAfterViewAll()

    else:
        exit("Logout Successfully")
