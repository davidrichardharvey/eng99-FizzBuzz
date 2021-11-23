class FizzBuzz:
    def __init__(self, default = 1000, is_valid = False):
        self.default = default
        self.is_valid = is_valid


    def is_valid_number(self, num):
        if num.isdigit() and num != "0":
            num = self.default if int(num) > self.default else int(num)
            self.is_valid = True

    def fizz_buzz(self):
        num = None
        while not self.is_valid:
            num = input("Please enter a valid number: ")
            self.is_valid_number(num)

        num = int(num) if int(num) < self.default else self.default

        for i in range(1, num + 1):
            if i % 3 == 0 and i % 5 == 0:
                print("FizzBuzz")
            elif i % 5 == 0:
                print("Buzz")
            elif i % 3 == 0:
                print("Fizz")
            else:
                print(i)