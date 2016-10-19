#Number guesser

#Some import statements here to generate randomness and exit out of program
import random
import sys

#compareNumbers function contains all the logic
def compareNumbers():
    global guessCounter
    print('Take a guess.')
    inputNumber = input()
    try:
        int(inputNumber)
    except ValueError:
        print('That is not an integer number at all!')
        return
    if int(inputNumber) > 20 or int(inputNumber) < 1:
        print('That is not a number between 1 and 20')
    elif int(inputNumber) < randomNumber:
        print('Your guess is too low.')
        guessCounter = guessCounter + 1
    elif int(inputNumber) > randomNumber:
        print('Your guess is too high.')
        guessCounter = guessCounter + 1
    elif int(inputNumber) == randomNumber:
        print('Good job!  You guessed my number in ',end='')
        print(str(guessCounter) + ' guesses!')
        sys.exit()
    if guessCounter > 6:
        print('Nope, the number I was thinking of was '+str(randomNumber))
        sys.exit()

#set the random number, and start the guessing counter
randomNumber = random.randint(1,20)
print('I am thinking of a number between 1 and 20')
guessCounter = 1

#call the main compareNumbers() function in a continuous loop
while True:
    compareNumbers()
