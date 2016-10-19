variableName=()
while not variableName:
    print('Enter a value, any value')
    variableName = input()
    if variableName:
        print('You entered ' + str(variableName))
        break
    print('You didn\'t enter anything!  Try again...')
