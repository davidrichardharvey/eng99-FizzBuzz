# - Write a program that will print the numbers 1 to 100
# - If the number is divisible by 3, print Fizz instead
# - If the number is divisible by 5, print Buzz instead
# - If the number is divisible by both, print FizzBuzz instead
# - Start the game by asking the user to provide the "up to" number


def fizz_buzz(limit):
    num = 0
    while num <= limit - 1:
        num += 1
        if num % 3 == 0 and num % 5 == 0:
            print("FizzBuzz")
        elif num % 3 == 0:
            print("Fizz")
        elif num % 5 == 0:
            print("Buzz")
        else:
            print(num)

print(fizz_buzz(int(input("Enter maximum boundary \n"))))