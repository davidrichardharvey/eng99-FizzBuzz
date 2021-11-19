'''
Write a program that will print the numbers 1 to 100
If the number is divisible by 3, print Fizz instead
If the number is divisible by 5, print Buzz instead
If the number is divisible by both, print FizzBuzz instead
Start the game by asking the user to provide the "up to" number
'''



def fizzbuzz_game(max_num):
    '''

    :param max_num:
    :return:
    '''
    for i in range(1,max_num+1):
        output = ''
        if i % 3 == 0:
            output += "Fizz"
        if i % 5 == 0:
            output += "Buzz"
        if len(output) == 0:
            output = i
        print(output)

fizzbuzz_game(100)