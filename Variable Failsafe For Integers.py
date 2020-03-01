replaceableVariable = int()

while replaceableVariable==0:
    try:
        replaceableVariable = int(input("Please Add An Integer to not break the system"))
    except:
        print("Why Didn't You Put An Interger In Here?")
