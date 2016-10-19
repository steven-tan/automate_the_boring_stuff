# The Collatz Sequence

# getInput() tests for errors, then returns a positive integer
def getInput():
    inputValue = ''
    print('Please enter a positive number....')
    while True:
        try:
            inputValue=int(input())
        except:
            print('That is not an integer! Try again...')
            continue
        if inputValue <= 0:
            print('The number must be positive! Try again...')
            continue
        else:
            print('Thank you!')
            return inputValue

# collatz() performs the needful calcs and prints collatz output                        
def collatz(number):
    if number % 2 == 0:
        print(number // 2)
        return number // 2
    else:
        print(3 * number + 1)
        return 3 * number + 1

n = getInput()

count = 0

while n != 1:
    n = collatz(n)
    count = count + 1

print('Sequence completed in ' + str(count) + ' steps.')

