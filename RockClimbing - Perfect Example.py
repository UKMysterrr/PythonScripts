## Rock Climbing Club Membership
import pickle, time, os

rockClimbingFile = ("members.p") #Gives filename to be checked

def syncdump(members):
    with open(rockClimbingFile,'wb') as wcf: #Syncs database
        pickle.dump(members,wcf) #Dumps new members

    with open(rockClimbingFile,'rb') as rcf: #Reloading database to be reread
        members = pickle.load(rcf)

if os.path.exists(rockClimbingFile): #Checks if filename exists
    with open(rockClimbingFile,'rb') as rcf: #if it does, its read, given the name 'rcf' and continues
        members = pickle.load(rcf)

else: #if not, it makes a new list
    members = []

    member = [] #Storage For Member Info To Be Appeneded Together
    userName = input("What is  your name?") #Requests Member name
    password = input("What Is Your Password?") #Rquests Time To Be Cooked
    member.append(userName) #Puts userName in member
    member.append(password) #Puts password in member
    members.append(member) #Puts member in members
    syncdump(members)

while True:  
    option = input("Are you here to 'register'? or to 'login'?")
    if option == 'register' or option == 'Register':
        member = [] #Storage For Member Info To Be Appeneded Together
        userName = input("What is  your name?") #Requests Member name
        password = input("What Is Your Password?") #Requests Password To Registered With
        member.append(userName) #Puts username in member
        member.append(password) #Puts password in member
        members.append(member) #Puts member in members
        syncdump(members)

    if option == 'login' or option == 'Login':
        userName = input("What Is Your Username?")
        password = input("What Is Your Password?")
    

    if option == '1tapgang': #if 1tapgang is inputted 'secret'
        members.sort() #sorts member list alphabetically
        print(members) #prints members

    if option == 'stop': #if input = stop
        sys.exit() #quit the program
