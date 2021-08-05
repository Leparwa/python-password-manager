from app.loginUser import login
from app import loginUser, registerUser

login_func = loginUser.login
register_func = registerUser.registerUser

class IuserClassLogin:
    def __init__(self, userName, password):
        self.userName = userName
        self.password = password

class IuserRegister:
    def __init__(self, userName, password, passwordRepeat):
        self.userName = userName
        self.password = password
        self.asswordRepeat =passwordRepeat
