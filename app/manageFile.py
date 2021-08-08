from app.test.userCredentialsTest import isCredentialsNotBlank
credentialsTest = isCredentialsNotBlank
#manage user credentials
def readUserCrenditialFile():
    file = open("userCredentials.txt", "r")
    print("\tUser Name\tAccount\t\tPassword")
    print("\t----------------------------------------")
    for i in file:
        user =i.split("|")
        if user:
            print("\t"+user[0]+"\t\t"+user[1]+"\t\t"+user[2])
            
        else:
            print("it is blank")

    print("\t______________________________________________")
def writeUserCrendentialsFile(username, password, account):
    file = open("userCredentials.txt", "a")
    file.write(username+"|"+account+"|"+password+"\n")

#manage user 
def writeRegisterUserFile(username, password):
    file = open("registeredUsers.txt", "a")
    file.write(username+" "+password+"\n")

def readRegisteredUserFile():
    file = open("registeredUsers.txt", "r")
    for i in file:
        user =i.split("|")
        print(user[0])

