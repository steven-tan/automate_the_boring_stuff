while True:
    print('Please give me some input... 1, 2, or anything else.  (Or exit if needed.)')
    spam = input()
    if spam == '1':
        print('Hello')
    elif spam == '2':
        print('Howdy')
    elif spam == 'exit':
        print('Exiting')
        break
    else:
        print('Greetings!')
