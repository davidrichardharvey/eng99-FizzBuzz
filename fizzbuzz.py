prompt_game = True
while prompt_game:
    input_range = input("Enter a number to play FizzBuzz\n")
    if input_range.isdigit():
        game_range = range(int(input_range) + 1)
        for n in game_range:
            if n % 3 == 0 and n % 5 == 0:
                n = "FizzBuzz"
            elif n % 3 == 0:
                n = "Fizz"
            elif n % 5 == 0:
                n = "Buzz"
            print(n)
            prompt_game = False
    else:
        print("Please enter a valid number")
