# Fizzbuzz 1-100

n = 100
i = 1

print("Fizzbuzz 1 to 100")
print("----START----")
while i <= n:
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
    i += 1

print("----END----\n")


# Fizzbuzz 1 up to x

prompt_for_number = True
x = None
while prompt_for_number:
    tempx = input("What number would you like the FizzBuzz to go up to: ")
    if tempx.isdigit():
        prompt_for_number = False
        x = int(tempx)
    else:
        print("please enter number  in digits")


counter = 1

print("Starting FizzBuss \n-----------------")
while counter <= x:
    if counter % 3 == 0 and counter % 5 == 0:
        print("FizzBuzz")
    elif counter % 3 == 0:
        print("Fizz")
    elif counter % 5 == 0:
        print("Buzz")
    else:
        print(counter)
    counter += 1
print("----------------- \nFizzBuzz Ended")
