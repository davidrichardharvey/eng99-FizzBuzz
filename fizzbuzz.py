# Write a program that will print the numbers 1 to 100
# If the number is divisible by 3, print Fizz instead
# If the number is divisible by 5, print Buzz instead
# If the number is divisible by both, print FizzBuzz instead
# Start the game by asking the user to provide the "up to" number

class FizzBuzz_Game:

    for user_input in range(1, 100):
        user_input = int(input("Enter a number from 1 up to 100\n"))
        user = int(user_input)
        if user_input >= 100:
            print("Enter a digit between 1-100")
        elif int(user_input) % 3 == 0 and int(user_input) % 5 == 0:
            print("FizzBuzz")
        elif int(user_input) % 3 == 0:
            print("Fizz")
        elif int(user_input) % 5 == 0:
            print("Buzz")
        else:
            print("keep going")
    else:
        print("Please, enter a digit")
