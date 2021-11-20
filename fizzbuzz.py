play = True
print('Welcome to FizzBuzz!')
while play:
    counter = 1
    number = (input('Please enter a number (1-100): '))

    if int(number) in range(1,101):
        while (counter < int(number)):
            if counter % 3 == 0 & counter % 5 == 0:
                print('FizzBuzz')
            elif counter % 3 == 0:
                print(('Fizz'))
            elif counter % 5 == 0:
                print('Buzz')
            else:
                print(counter)
            counter += 1
    else:
        print('Please enter correct value')

    counter = 1
    replay = str(input('Do you want to play again? (Y/N)'))
    if replay == 'N' or replay == 'n':
        play = False
print('Thanks for playing!')










