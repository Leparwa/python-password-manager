#manage user credentials
def readUserCrenditialFile():
    file = open("userCredentials.txt", "a")
    for i in file:
        user =i.split("''")
        return user


def writeUserCrendentialsFile(username, password, account):
    file = open("registeredUsers.txt", "a")
    file.write(username+" "+password+" "+account+"\n")

#manage user 
def writeRegisterUserFile(username, password):
    file = open("registeredUsers.txt", "a")
    file.write(username+" "+password+"\n")
def readRegisteredUserFile(password):
    file = open("registeredUsers.txt", "a")
    for i in file:
        user =i.split("''")
        return user[i]==str(password)
