import sys

def printList():
    print('Here is your list:')
    for i in listVariable:
        print(i)


listVariable = []

print('Please enter items you\'d like added to the list.  To finish the list, just press enter.')

while True:
    print('? ',end='')
    inputVariable = input()
    if inputVariable == '':
        print()
        printList()
        sys.exit()
    print('Okay, I\'ve added ' + inputVariable)
    listVariable = listVariable + [inputVariable]


##An alternate version which is a bit simpler:
##
##catNameList = []
##print('Now enter the name of a cat.  Or just press enter to end the list.')
##while True:
##    print('Cat Name: ',end='')
##    catInput = input()
##    if not catInput:
##        break
##    catNameList = catNameList + [catInput]
##print('Thanks, that\'s all the cats!  Here is the list:')
##for i in catNameList:
##    print('   ' + i)
