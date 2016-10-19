while True:
    print('Who are you?')
    name = input()
    if name != 'Joe':
        continue
    print('Hello, Joe. What is the password?')
    print('hint: It is a big fish that lives in the sea')
    password = input()
    if password == 'swordfish':
        break
    else:
        print('Nope, wrong password. Starting over.')
print('Access granted.')
