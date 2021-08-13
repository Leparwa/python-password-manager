import random
import string
from classes.userClass import IuserClassLogin
from app.manageFile import removeAccount, readUserCrenditialFile, writeUserCrendentialsFile
userInfo =IuserClassLogin
userCrenditials = readUserCrenditialFile
writeCredentials = writeUserCrendentialsFile
deleteAcc = removeAccount

isContinueAddMoreAccounts = False

def login():
    '''
    this function handles login functionality 
    '''
    print("\033c")
    if(userInfo.user):
        print(userInfo.user)
        actionsAfterLogin()
    else:
        print("user does not exist")


def viewAll():
    userCrenditials()

def actionsAfterLogin():
    '''
    this function handles user actions after login
    '''
    print("\033c")
    print("*********LIST OF CREDENTIALS MANAGED***********\n")
    viewAll()
    loginAction =input("\t********MANAGE YOUR ACCOUNT***********\n"
          "\t1: add new account\n"
           "\t2: view managed account's credentials\n"
           "\t3: delete Account\n"
           "\t4: Logout \n>>>")
    if loginAction =='1':
        print("\033c")
        addNewAcount()
        actionAfterAddNewAccount()
    elif loginAction=='2':
        print("\033c")
        viewAll()
        actionAfterViewAll()
    elif loginAction=='3':
        deleteAccount()

    else:
        exit("Logout Successfully")

def addNewAcount():
    ''' 
    this function handles user action adding new account credentials
    '''
    password = ""
    userName=input("Enter Account Username  \n >>")
    account=input("Enter Account company \n >> ")
    isgeneratePassword =input("\t1: generate password?"
                              "\t2: enter your password\n"
                                "\t >>>")
    if isgeneratePassword=='1':
        password_length = input("enter the length of the password \n >>")
        password = generate_pass(int(password_length))
    elif isgeneratePassword =='2':
        password=input("Enter Account Password \n >> ")


    writeCredentials(userName, password, account)

def actionAfterViewAll():
    '''
    this function handles user actions after they view all of the saved credentials
    '''
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
    '''
    this function handles user actions after login
    '''
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

def deleteAccount():
    '''This function deletes user account'''

    password = input("Enter The Password Of Account You Want To Delete\n>>>")
    deleteAcc(password)
    login()

def generate_pass(length):
    "Takes length of the password desired by user"

    '''
    it automatically generates the password
    and the function return the password
    '''
    letters = string.ascii_lowercase
    random_password = ''.join(random.choice(letters) for i in range(length))
    return random_password
