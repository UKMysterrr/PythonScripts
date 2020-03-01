#Morse Code By: Mitchell Docherty

#Infinite Loop

goagain = 1
while goagain == 1:

#   Asks For Message And Adds A New Message For The Morse

    message = input("What would you like to encrypt?")
    new_message = ""

    letters = {"a": ".- ",
    "b": "-... ",
    "c": "-.-. ",
    "d": "-.. ",
    "e": ". ",
    "f": "..-. ",
    "g": "--. ",
    "h": ".... ",
    "i": ".. ",
    "j": ".--- ",
    "k": "-.- ",
    "l": ".-.. ",
    "m": "-- ",
    "n": "-. ",
    "o": "--- ",
    "p": ".--. ",
    "q": "--.- ",
    "r": ".-. ",
    "s": "... ",
    "t": "- ",
    "u": "..- ",
    "v": "...- ",
    "w": ".-- ",
    "x": "-..-",
    "y": "-.--",
    "z": "--.."}

    for let in message:
        if let in letters:
            new_message += letters[let]
    print(new_message)


