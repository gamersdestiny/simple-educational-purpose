import random
import os
def guessing_game_single():
    print('you choosed single player game')
    global Toguess
    Toguess = input("choose Animals or Birds or Vehicles or Famous cities: ").lower()
    animals = ['Squirrel','Dog','Chimpanzee','Lion','Panda', 'Goat']
    birds = ['Crow', 'Peacock', 'Dove', 'Sparrow', 'Eagle', 'Ostrich', 'Pigeon',]
    vehicles = ['Motorbike', 'Scooter', 'Skateboard', 'Truck', 'Ambulance', 'Firetruck']
    famous_cities  = ['Paris', 'Newyork', 'France', 'Aagra', 'Egypt']
    if 'animal' in Toguess:
        print('You choosed Animals')
        findA = random.choice(animals)
        Toguess = findA        
    elif 'bird' in Toguess:
        print('You choosed Birds')
        findB = random.choice(birds)
        Toguess = findB
    elif 'vechicle' in Toguess:
        print('You choosed Vehicles')
        findC = random.choice(vehicles)        
        Toguess = findC        
    elif 'famous' in Toguess:
        print('You choosed Famous places')
        findD = random.choice(famous_cities)        
        Toguess = findD        
    else:
        print('Not a valid choice')
        return True
    Triedword = ""
    result = False
    Timesgussed = 0
    print('Try to find the word... :P You have 3 chances')
    midindex = int(len(Toguess)/2)
    while result == False and True:
        print(Toguess[0], '___', Toguess[midindex], '___', Toguess[-1:])
        Triedword = input('Guess the right word: ')
        Triedword = Triedword.capitalize()
        print('Attempt', Timesgussed+1)
        os.system('cls')
        Timesgussed += 1
        if Triedword == Toguess:
            print('That is the correct answer :D')
            result = True
            break
        if Toguess != Triedword:
            print('Wrong answer :( Try again')
        if Timesgussed == 3:
            print('You are out of chances')
            break

def guessing_game_dual():
    print('you choosed dual player game')
    Toguess = input("User 1 input the word of atleast 5 words to be guessed: ")
    os.system('cls')
    Triedword = ""
    result = False
    Timesgussed = 0
    print('User 2 find the word... :P You have 3 chances')
    midindex = int(len(Toguess)/2)
    print(midindex)
    while result == False:
        print(Toguess[0], '___', Toguess[midindex], '___', Toguess[-1:])
        Triedword = input('Guess the right word: ')
        print('Attempt', Timesgussed+1)
        os.system('cls')
        Timesgussed += 1
        if Triedword == Toguess:
            print('That is the correct answer :D')
            result = True
            break
        if Toguess != Triedword:
            print('Wrong answer :( Try again')
        if Timesgussed == 3:
            print('Sorry You are out of chances')
            print('The answer is', Toguess)
            break

def players_choice():
    playerchoice = (input("Select 1 player player 2 player mode: "))
    if 'single' or '1' in playerchoice:
        guessing_game_single()
    elif 'dua' or '1' in playerchoice:
        guessing_game_dual()
    else:
        print("This is not a valid choice")
players_choice()
