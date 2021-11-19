num = None
while True:
    num = input("Please enter a valid number: ")
    if num.isdigit():
        num = 1000 if int(num) > 1000 else int(num)
        break


for i in range(1, num + 1):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 5 == 0:
        print("Buzz")
    elif i % 3 == 0:
        print("Fizz")
    else:
        print(i)