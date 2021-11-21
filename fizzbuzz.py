# - Write a program that will print the numbers 1 to 100
# - If the number is divisible by 3, print Fizz instead
# - If the number is divisible by 5, print Buzz instead
# - If the number is divisible by both, print FizzBuzz instead
# - Start the game by asking the user to provide the "up to" number



# age = 0
# while True:
#     age = input("What is your age in years \n")
#     if age.isdigit():
#         age = int(age)
#         if age <= 118:
#             break
#         else:
#             print("Big doubt")
#     print("Please provide your age in digits")
#
# print(age, type(age))
# x = range(1, 101)
# for i in x:
#     if i % 3 == 0:
#         print("Fizz")
#     elif i % 5 == 0:
#         print("Buzz")
#         print(i)
num = 1
while num <= 100:
    num += 1
    if num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
        print(num)


# for number in number:
#     square = number ** 2
#     print(square)
# print(range(5))