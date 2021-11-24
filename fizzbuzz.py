
print('Welcome to FizzBuzz!\n')

def fizzbuzz(user_input):
    if user_input.isdigit():
        for i in range(1, (int(user_input) + 1)):
            if i % 3 == 0 and i % 5 == 0:
                print('FizzBuzz')
            elif i % 3 == 0:
                print('Fizz')
            elif i % 5 == 0:
                print('Buzz')
            else:
                print(i)
    else:
        print('Please enter a valid number')

print(fizzbuzz(input('Please provide a number you would like to play up to: ')))