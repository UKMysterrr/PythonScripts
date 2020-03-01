import random
import time

#Converts Money Into A Float For Decimals

money = 1
money = float(money)

play = 1

print("###################")
print("#    F r u i t    #")
print("#  M a c h i n e  #")
print("#                 #")
print("# M i t c h e l l #")
print("# D o c h e r t y #")
print("###################")
print("")
print("3x Bell = £2")
print("3x Cherry = £5")
print("3x Orange = £10")
print("3x Lemon = £25")
print("3x Star = £50")
print("2x The Same = Half Of 3x")
print("")
#Machine Takes Money To Roll, And Starts A While Loop
while play == 1:
    print("Rolling..")
    time.sleep(2)
    money = money - 0.2

    rollone = random.choice(["Bell","Bell","Bell","Bell","Bell","Cherry","Cherry","Cherry","Cherry","Lemon","Lemon","Lemon","Orange","Orange","Star","Skull","Skull"])
    rolltwo = random.choice(["Bell","Bell","Bell","Bell","Bell","Cherry","Cherry","Cherry","Cherry","Lemon","Lemon","Lemon","Orange","Orange","Star","Skull","Skull"])
    rollthr = random.choice(["Bell","Bell","Bell","Bell","Bell","Cherry","Cherry","Cherry","Cherry","Lemon","Lemon","Lemon","Orange","Orange","Star","Skull","Skull"])

#Rolls Then Prints The Rolls.

    print(rollone)
    time.sleep(2)
    print(rolltwo)
    time.sleep(2)
    print(rollthr)
    time.sleep(2)

#Checks For Similarities In Paytable

    if rollone == "Bell" and rolltwo == "Bell" and rollthr == "Bell":
        money = money + 2
        
    elif rollone == rolltwo == "Bell" or rolltwo == rollthr == "Bell" or rollone == rollthr == "Bell":
        money = money + 1
        
    if rollone == "Cherry" and rolltwo == "Cherry" and rollthr == "Cherry":
        money = money + 5
        
    elif rollone == rolltwo == "Cherry" or rolltwo == rollthr == "Cherry" or rollone == rollthr == "Cherry":
        money = money + 2.5
        
    if rollone == "Orange" and rolltwo == "Orange" and rollthr == "Orange":
        money = money + 10
        
    elif rollone == rolltwo == "Orange" or rolltwo == rollthr == "Orange" or rollone == rollthr == "Orange":
        money = money + 5
        
    if rollone == "Lemon" and rolltwo == "Lemon" and rollthr == "Lemon":
        money = money + 25
        
    elif rollone == rolltwo == "Lemon" or rolltwo == rollthr == "Lemon" or rollone == rollthr == "Lemon":
        money = money + 12.5
        
    if rollone == "Star" and rolltwo == "Star" and rollthr == "Star":
        money = money + 50
        
    elif rollone == rolltwo == "Star" or rolltwo == rollthr == "Star" or rollone == rollthr == "Star":
        money = money + 25
        
    if rollone == "Skull" and rolltwo == "Skull" and rollthr == "Skull":
        money = money - money

    elif rollone == rolltwo == "Skull" or rolltwo == rollthr == "Skull" or rollone == rollthr == "Skull":
        money = money - 5
    

#Prints Money And Checks If You Have Any Left.

    print("You Have £",round(money,2),"Left.")
    if money < 0.2:
        print("You Have Run Out Of Money. Thanks For Playing!")
        time.sleep(3)
        exit()
    play = int(input("If You Would Like To Play Again, Please Press 1...  "))
    if play != 1:
        print("Thanks For Playing!, You Left The Casino With £",money,"Left")
        time.sleep(3)
        exit()
    
