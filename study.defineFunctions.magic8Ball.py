#magic8Ball.py

import random
import sys
def getAnswer(answerNumber):
    if answerNumber == 1:
        return 'It is certain'
    elif answerNumber == 2:
        return 'It is decidedly so'
    elif answerNumber == 3:
        return 'Yes'
    elif answerNumber == 4:
        return 'Reply hazy, try again'
    elif answerNumber == 5:
        return 'Ask again later'
    elif answerNumber == 6:
        return 'Concentrate and ask again'
    elif answerNumber == 7:
        return 'My reply is no'
    elif answerNumber == 8:
        return 'Outlook not so good'
    elif answerNumber == 9:
        return 'Very doubtful'

userinput=()
while not userinput:
    print('Please think of a yes or no question, then press enter.  Or type "exit" to end program.')
    userinput = input()
    if not userinput:
        r = random.randint(1, 9)
        fortune = getAnswer(r)
        print(fortune)
        print()
    elif userinput == 'exit':
        print('Exiting program, thanks for playing.')
        sys.exit()
    else:
        userinput = ()
        print('Huh?  Only enter or exit work.')
        print()
        continue
