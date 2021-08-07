#manage user credentials
def readUserCrenditialFile():
    file = open("userCredentials.txt", "r")
    for i in file:
        user =i.split(" ")
    print(user)
      

def writeUserCrendentialsFile(username, password, account):
    file = open("registeredUsers.txt", "a")
    file.write(username+"|"+password+"|"+account+"\n")

#manage user 
def writeRegisterUserFile(username, password):
    file = open("registeredUsers.txt", "a")
    file.write(username+" "+password+"\n")

def readRegisteredUserFile():
    file = open("registeredUsers.txt", "r")
    for i in file:
        user =i.split("|")
        print(user[0])

