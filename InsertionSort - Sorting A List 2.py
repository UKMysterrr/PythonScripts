#Insertion sort / Mitchell Docherty
import time

#List of Names to be sorted
namelist = ["John", "Dave", "Mary", "Peter", "Jane", "Adam", "Barry", "Amanda"]
#Make a Definition
def insertion(temp):
    for i in range(1, len(temp)): #Looks in the list
        while temp[i-1] > temp[i] and temp[i-1]: #If the value is on the wrong side,
            temp[i-1], temp[i] = temp[i], temp[i-1] #It switches
            print(temp) #Prints as it goes
            time.sleep(1) #Waits a second for show purposes


print (namelist) #Prints before command
print("")
insertion(namelist) #Runs "Insertion"
print (namelist) #Prints Aftermath
