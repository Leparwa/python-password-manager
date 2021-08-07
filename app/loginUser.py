from classes.userClass import IuserClassLogin
from app.manageFile import readRegisteredUserFile
userInfo =IuserClassLogin
userCrenditials = readRegisteredUserFile

def login():
    if(userInfo.user):
        actionsAfterLogin()
    else:
        print("user does not exist")


def viewAll():
    userCrenditials()

def actionsAfterLogin():
    viewAll()
    print("--------------------------")
