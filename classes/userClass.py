
class IuserClassLogin:
    def __init__(self, userName, password):
        self.userName = userName
        self.password = password

class IuserRegister:
    def __init__(self, userName, password, passwordRepeat):
        self.userName = userName
        self.password = password
        self.asswordRepeat =passwordRepeat
        