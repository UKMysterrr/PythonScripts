import pickle, time, os

recipesFileName = 'recipes.p' #Gives filename to be checked

if os.path.exists(recipesFileName): #Checks if filename exists
    with open(recipesFileName,'rb') as rfn: #if it does, its read, given the name 'rfn' and continues
        recipes = pickle.load(rfn)

else: #if not, it makes a new list
    recipes = []
    
cake = [] #Storage For Cake Names To Be Appeneded Together
cakeName = input("What is the name of your cake?") #Requests cake name
cookingTime = int(input("How Many Minutes Are You Cooking For?")) #Rquests Time To Be Cooked
cake.append(cakeName) #Puts cakeName in Cake
cake.append(cookingTime) #Puts cookingTime in Cake
recipes.append(cake) #Puts Cake in Recipes

with open(recipesFileName,'wb') as wfn: #Syncs database
    pickle.dump(recipes,wfn) #Dumps new cakes

with open(recipesFileName,'rb') as rfn: #Reloading database to be reread
    recipes = pickle.load(rfn)

print(recipes) #Prints Final list

sortRequest = input("How Would You Like It Sorted? say 'Name' or 'time'.")
if sortRequest == "Name" or sortRequest == "name":
    recipes.sort() #Sorts Recipes Alphabetically
    print(recipes)
    
elif sortRequest == "Time" or sortRequest == "time":
    recipes.sort(key=lambda x:x[1], reverse=False)
    print(recipes) #Prints New Sorted List By Time

