class BigNumber:
    def __init__(self):
        self.n = 0
    def __init__(self, a:int)->int:
        self.n = a
    def print_number(self):
        print(self.n)

n = 12345678901234567890
my_num = BigNumber(n)
my_num.print_number()
