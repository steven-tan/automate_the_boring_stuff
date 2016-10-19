catNameList = []
print('Now enter the name of a cat.  Or just press enter to end the list.')
while True:
    print('Cat Name: ',end='')
    catInput = input()
    if not catInput:
        break
    catNameList = catNameList + [catInput]
print('Thanks, that\'s all the cats!  Here is the list:')
for i in catNameList:
    print('   ' + i)
