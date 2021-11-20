play = True

while play:
    counter = 1
    number = int(input('Please enter a maximum number: '))


    while (counter < number):
        if counter % 3 == 0 & counter % 5 == 0:
            print('FizzBuzz')
        elif counter % 3 == 0:
            print(('Fizz'))
        elif counter % 5 == 0:
            print('Buzz')
        else:
            print(counter)
        counter += 1

    counter = 1
    replay = str(input('Do you want to play again? (Y/N)'))
    if replay == 'N':
        play = False










