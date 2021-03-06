from app.test.userCredentialsTest import isCredentialsNotBlank
credentialsTest = isCredentialsNotBlank
#manage user credentials
def readUserCrenditialFile():
    '''
    this function have a functionality to read userCredential.txt file
    '''
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
    '''
    this function have a functionality to write userCredential.txt file
    '''
    file = open("userCredentials.txt", "a")
    file.write(username+"|"+account+"|"+password+"\n")

def removeAccount(password):
    '''
    this function handles a functionality of removing credentials from userCredential.txt
    it takes in password as a param 
    '''
    with open("userCredentials.txt",'r') as file:
        lines = file.readlines()

    with open("userCredentials.txt",'w') as file:
        for line in lines:
        # find() returns -1 if no match is found
            if line.find(password) != -1:
                print("No Matching account")
            else:
                file.write(line)
                print("Deleted")
#manage user 
def writeRegisterUserFile(username, password):
    '''
    this function handles writing writerRegisterUserFile.txt
    it takes in username and password
    '''
    file = open("registeredUsers.txt", "a")
    file.write(username+" "+password+"\n")

def readRegisteredUserFile():
    '''
    this function handles reading writerRegisterUserFile.txt
    '''
    file = open("registeredUsers.txt", "r")
    for i in file:
        user =i.split("|")
        print(user[0])

