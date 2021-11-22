"""
BRIEF:
Write a program that will print the numbers 1 to 100
If the number is divisible by 3, print Fizz instead
If the number is divisible by 5, print Buzz instead
If the number is divisible by both, print FizzBuzz instead
Start the game by asking the user to provide the "up to" number
"""


class Fizzbuzz_Game:
    def __repr__(self):
        return "A class for playing the game Fizzbuzz"
    def __init__(self):
        pass

    def fizzbuzz(self, max_num):
        """
        Game that prints from 1 to a given number.
        If the number is divisible by 3, print Fizz instead
        If the number is divisible by 5, print Buzz instead
        If the number is divisible by both, print FizzBuzz instead
        max_num is the upper limit for the game:
        """
        for i in range(1, max_num + 1):
            output = ''
            if i % 3 == 0:
                output += "Fizz"
            if i % 5 == 0:
                output += "Buzz"
            if len(output) == 0:
                output = i
            print(output)

    def get_upper_limit(self):
        """
        Gets the user to enter a number to act as the upper limit in the Fizzbuzz game
        Checks if it is valid
        if valid, returns the number
        if not, loops again
        Returns the maximum number for the game
        """
        while True:
            max_num = input("For the FizzBuzz game, please enter an upper limit that is great than one: ")
            # Ensures user enters an integer
            try:
                max_num = int(max_num)
            except ValueError:
                print("Please enter an integer")
                continue
            # Ensuring user enters an integer 1 or larger
            if max_num <= 0:
                print("Please enter a number greater than 0")
                continue
            break
        return max_num

    def play_again(self):
        '''
        Asks the user if they want to play again
        if not, then the code returns false, otherwise no return is necessary
        '''
        play_again = input("Do you wish to play again? y/n ")
        play_again.lower()
        # if first conditional is false, second isn't checked, so second cannot generate an empty list error if the
        # length is indeed 0
        if len(play_again) > 0 and play_again[0] == "n":
            print("Thank you for playing, the game has now ended")
            return False


# Gets user input, runs game, checks if user wants to play again (if the answer isn't a no, then it runs again)
while True:
    # Running game
    game = Fizzbuzz_Game()
    # Gets the upper limit for the user's game
    max_num = game.get_upper_limit()
    # Executes fizzbuzz portion of game
    game.fizzbuzz(max_num)
    # Does the user want to replay?
    # if not, game ends, other responses starts a new game
    play_again = game.play_again()
    if play_again == False:
        break
