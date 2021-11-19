#Write a program that will print the numbers 1 to 100 - DONE
#If the number is divisible by 3, print Fizz instead - DONE
#If the number is divisible by 5, print Buzz instead - DONE
#If the number is divisible by both, print FizzBuzz instead - DONE
#Start the game by asking the user to provide the "up to" number


user_input = input('Please provide a number you would like to play up to: ')
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
            start_game = False
else:
    print('Please enter a valid number')
