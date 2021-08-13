from app.manageFile import writeRegisterUserFile
from app.loginUser import login

login_func = login
write_register_func = writeRegisterUserFile
def registerUser(userName, password, repeatPassword):
    '''
    this function have a functionality to register user 
    '''
    if(password==repeatPassword):
        write_register_func(userName, password)
        print("\033c")
        actionsAfterRegister(userName, password)        
    elif(password != repeatPassword):
        print("passwords do not match")
    else:
        exit()
def actionsAfterRegister(user, password):
    '''
    this function have a functionality to handle user actions after register
    '''
    userChoise ='',
    userChoise = input("****CONGRATULATIONS!!"+" "+user+""+", Account Created Successfully******** \n"
                            "\t1: Login \n"
                            "\t2: Exit \n>>>")
    if userChoise =='1':
         login_func()
    elif userChoise =='2':
        exit()
    else:
        print("\033c")
        invalidChoice(user)

def loginAfterRegister():
    pass

def invalidChoice(user):
    '''
    this function have a functionality to handle invalid choice made by the user
    '''
    userChoise ='',
    userChoise = input("****SORRY!!"+" "+user+""+", Please Select A Valid Option******** \n"
                            "\t1: Login \n"
                            "\t2: Exit \n>>>")
    if userChoise =='1':
         pass
    elif userChoise =='2':
        exit()
    else:
        print("\033c")
        invalidChoice(user)

