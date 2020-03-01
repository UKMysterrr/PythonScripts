#Classification - Mitchell Docherty

#Intro

print("###################")
print("# C l a s s i f - #")
print("# i c a t i o n . #")
print("#       B y       #")
print("# M i t c h e l l #")
print("# D o c h e r t y #")
print("###################")
print("")
print("Simply Enter *y* to say yes, and anything else for no.")

#List Of Animals

animals = ["Horse", "Cow", "Sheep", "Pig", "Dog", "Cat", "Lion",
           "Tiger", "Whale", "Dolphin", "Seal", "Penguin", "Ostrich",
           "Sparrow", "Spider", "Ant", "Bee", "Wasp", "Termite", "Octopus", "Squid"]

#Removal Variables

legsno = [8, 9, 10, 11, 12, 13]

#Asks Questions, And Removes Irrelevant Animals

legs = input("Does Your Animal Have 4 Or More Legs?")
if legs == "y":
             animals.remove("Whale")
             animals.remove("Dolphin")
             animals.remove("Seal")
             animals.remove("Penguin")
             animals.remove("Ostrich")
             animals.remove("Sparrow")
else:
    animals.remove("Horse")
    animals.remove("Cow")
    animals.remove("Sheep")
    animals.remove("Pig")
    animals.remove("Dog")
    animals.remove("Cat")
    animals.remove("Lion")
    animals.remove("Tiger")
    animals.remove("Spider")
    animals.remove("Ant")
    animals.remove("Bee")
    animals.remove("Wasp")
    animals.remove("Termite")
    animals.remove("Octopus")
    animals.remove("Squid")

print(animals)
    
