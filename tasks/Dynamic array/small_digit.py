class SmallDigit:
    def __init__(self):
        self.d = 0.0
    def __init__(self, f:float)->float:
        self.d = f
    def print_digit(self):
        print(self.d)

f = 1.234567891234567891234
my_digit = SmallDigit(f)
my_digit.print_digit()
