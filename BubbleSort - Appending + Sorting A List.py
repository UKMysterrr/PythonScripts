#Bubble sort / Mitchell Docherty
import time

#List of Names to be sorted

name1 = input("Input No.1")
name2 = input("input No.2")
namelist = []
namelist.append(name1)
namelist.append(name2)

#Make a Definition

def bubble(temp):
    length = len(temp) - 1
    sorted = False

    while not sorted:
        sorted = True
        print (temp)
        time.sleep(1)
        for i in range(length):
            if temp[i] > temp[i+1]:
                sorted = False
                temp[i], temp[i+1] = temp[i+1], temp[i]

#Genuine Code.

print (namelist)
print("")
bubble(namelist)
print (namelist)
