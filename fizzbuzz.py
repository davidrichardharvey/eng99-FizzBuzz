number = int(input('Please enter a maximum number: '))
counter = 1

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









