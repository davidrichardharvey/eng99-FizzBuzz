class FizzBuzz:
    def __init__(self, default=1000, is_valid=False):
        self._default = default
        self._is_valid = is_valid

    def is_valid_number(self, num):
        if num.isdigit() and num != int(num) > 0:
            self._is_valid = True

    def fizz_buzz(self):
        num = None
        while not self._is_valid:
            num = input("Please enter a valid number: ")
            self.is_valid_number(num)

        num = self._default if int(num) > self._default else int(num)

        for i in range(1, num + 1):
            if i % 3 == 0 and i % 5 == 0:
                print("FizzBuzz")
            elif i % 5 == 0:
                print("Buzz")
            elif i % 3 == 0:
                print("Fizz")
            else:
                print(i)
