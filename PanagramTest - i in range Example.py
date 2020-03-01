#Pangrams
alphabet = 'abcdefghijklmnopqrstuvwxyz' #List Alphabet
sentence = input('ok: ').lower() #Input Sentence To Be Checked, Forces It In Lower Case
while sentence != 'stop': #saying stop quits instantly, while saying stop will close it instantly
    characters = [] #creating a list for the letters to be held
    for i in range(len(sentence)): #reads the sentence
        currentLetter = sentence[i] #readability
        if currentLetter in alphabet and currentLetter not in characters: #add a character to the list, if not in list and in alphabet
            characters.append(currentLetter) #add it to the list
    characters.sort() #sort
    characters = ''.join([characters[i] for i in range(len(characters))]) #join characters together, should form alphabetically
    print('Yeet!' if characters == alphabet else 'Nope!') #print yes or no
    sentence = input('ok: ').lower() #reiterates input that loops
