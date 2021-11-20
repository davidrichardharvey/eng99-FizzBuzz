start_game = True

while start_game:
    up_to_number = input("Pick a number you want to count up to?\n")

    if int(up_to_number) in range(1, 101):
        for i in range(1, int(up_to_number)):
            if i % 3 == 0 and i % 5 == 0:
                print("BuzzFizz")
            elif i % 3 == 0:
                print("Buzz")
            elif i % 5 == 0:
                print("Fizz")
            else:
                print(i)
    else:
        print("Enter a valid number that is between 1 - 100")

    start_over = input("Thank you for playing, type Y if you want to play again or any other key to stop\n")
    start_over = start_over.upper()

    if start_over == "Y":
        start_game = True
    else:
        print("Thank you for playing!")
        break
