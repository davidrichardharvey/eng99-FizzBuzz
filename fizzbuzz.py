# Viggy's Fizz Buzz Game

prompt_if_game_over = True
while prompt_if_game_over:
    prompt_if_number = True

    while prompt_if_number:
        Number_Limit = input("Enter the number up to which you would like to play the FIZZBUZZ Game\n")
        if Number_Limit.isdigit():
            prompt_if_number = False
        else:
            print("Error: Kindly  entered a valid number (eg 100)")
    print("The Numbers will start print:")
    for number in range(1, int(Number_Limit) + 1):
        if number % 3 == 0 and number % 5 == 0:
            print("FizzBuzz")
        elif number % 3 == 0:
            print("Fizz")
        elif number % 5 == 0:
            print("Buzz")
        else:
            print(number)
    play_again = input("1) Enter 'y' if you want to play the game again\n2)Enter any other character to exit\n").upper()
    if play_again != "Y":
        prompt_if_game_over = False


print("Hope you had a wonderfull experience see you back soon, bye")
