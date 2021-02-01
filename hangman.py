import random
from words import words
questionWord = random.choice(words)
dashes = (' _ '*len(questionWord))
questionWordset = set(questionWord)
print(dashes)
def playagain():
    Pagain = input('Do you wanna play again Yes or No: ').lower()
    if 'y' or 'yes' in Pagain:
        find()
def find():
    limit = 6
    chances = 0
    lenth = 6
    dashesAsset = set()
    userAnswer = set()
    while chances<limit:
        userInput = input('\nEnter a character: ').lower()
        if userInput in questionWord:
            if userInput in userAnswer:
                print('You have already entered the word')
            if userInput in questionWord:
                if userInput in dashesAsset:
                    continue
                userAnswer.add(userInput)
            for letter in questionWord:
                if letter in userAnswer:
                    print(letter, end=' ')
                else:
                    print(' _ ',end='')
            if questionWordset == userAnswer:
                print('\nYou got the right answer')
                break
        elif userInput not in questionWord:
            chances += 1
            lenth -=1
            print(f'Wrong character Try again chances left {lenth}')
    else:
        print(f'You are out of chances. The answer is {questionWord}')

find()
