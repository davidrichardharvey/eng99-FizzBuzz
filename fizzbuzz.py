# Write a program that will print the numbers 1 to 100
# If the number is divisible by 3, print Fizz instead
# If the number is divisible by 5, print Buzz instead
# If the number is divisible by both, print FizzBuzz instead
# Start the game by asking the user to provide the "up to" number


fizzbuzz_game = True

while fizzbuzz_game <100:
    fizzbuzz_game = input("Enter a number from 1 up to 100\n")
    if fizzbuzz_game.isdigit():
        fizzbuzz_game = int(fizzbuzz_game)
        if fizzbuzz_game == 100:
            break
        elif fizzbuzz_game == 0:
            print("Please enter a different number")
        elif int(fizzbuzz_game) % 3 == 0 and int(fizzbuzz_game) % 5 == 0:
            print("FizzBuzz")
        elif int(fizzbuzz_game) % 3 ==0:
            print("Fizz")
        elif int(fizzbuzz_game) % 5 ==0:
            print("Buzz")
        else:
            print("keep guessing")