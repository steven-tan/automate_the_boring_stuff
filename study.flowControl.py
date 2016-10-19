#This program imports sys module, then uses various flow control methods
#in a while loop, including continue, break, sys.exit, as well as
#standard if elif else logic and a for loop

import sys

while True:
    print('Type exit to exit.  Also try "again" and "breakloop"')
    response = input()
    if not response:
        print('Please give me some input, not just carriage returns.')
        continue
    elif response == 'exit':
        print('Exiting program')
        sys.exit()
    elif response == 'again':
        print('Okay, repeating while loop.')
        continue
    elif response == 'breakloop':
        print('Okay, continuing with rest of program.')
        break
    else:
        print(('Random input received, you entered: ') + str(response))
        print('starting over...')
        print()

for i in range(3):
    print()

print('This is now the remainder of the program.')
print('blah blah blah')
