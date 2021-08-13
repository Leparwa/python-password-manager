from app.manageFile import readRegisteredUserFile
registered_func = readRegisteredUserFile
class IuserClassLogin:
    "User login Class"

    '''
     
    the class takes in username, password
    '''
    def __init__(self, userName, password):
        
        self.userName = userName
        self.password = password

    def user(self):
        isRegistered = readRegisteredUserFile(self.password)
        if(isRegistered):
           return True
        else:
          return  print("user do not exist")
  
 

