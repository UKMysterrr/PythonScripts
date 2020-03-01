#Rock Paper Scissors / Mitchell Docherty
"""Pseudo Code..
name = input('What is Your Name? ')
output ("Welcome to Rock Paper Scissors! Go Against The Machine And See Who Wins!")
botList = [1, 2, 3]
wins = 0
botWins = 0

while guess <> '':
    botGuess = random.choice(botList)
    guess = ("Please Press... 1 For Rock, 2 For Paper, Or 3 For Scissors!")
    if guess = botGuess:
        output ("Broken Even! Try Again!")
    elif guess = 1 and botGuess = 2 or guess = 2 and botGuess = 3 or guess = 3 and botGuess = 1:
        output ("Ouch, You Lost!")
        botWins = botWins + 1
    elif guess = 1 and botguess = 3 or guess = 2 and botguess = 1 or guess = 3 and botGuess = 2:
        output ("Well done! you beat me!")
        wins = wins + 1
endwhile
"""

import random, time, pickle

botList = [1, 2, 3]
wins = 0
botWins = 0

name = input('What is Your Name? ')
print ("Welcome to Rock Paper Scissors! Go Against The Machine And See Who Wins!")
guess = input("Please Press... 1 For Rock, 2 For Paper, Or 3 For Scissors!")

while guess != "":
    botGuess = random.choice(botList)

    if guess == botGuess:
        print ("Broken Even! Try Again!")

    elif (guess == 1 and botGuess == 2) or (guess == 2 and botGuess == 3) or (guess == 3 and botGuess == 1):
        print ("Ouch, You Lost!")
        botWins = botWins + 1

    if (guess == 1 and botguess == 3) or (guess == 2 and botguess == 1) or (guess == 3 and botGuess == 2):
        print ("Well done! you beat me!")
        wins = wins + 1

    guess = input("Please Press... 1 For Rock, 2 For Paper, Or 3 For Scissors!")
