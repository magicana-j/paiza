import random


class Game:
    def __init__(self, n, a, b):
        self.n = n
        self.a = a
        self.b = b
        self.temochi = [1, 1]
        self.kaisuu = [0, 0]

    def one_deal(self):
        self.temochi[1] += self.temochi[0] * self.a
        self.kaisuu[0] += 1
        self.temochi[0] += self.temochi[1] % self.b
        self.kaisuu[1] += 1

        return self.kaisuu[0]

    def num_of_deal(self):
        while self.temochi[1] <= self.n:
            self.one_deal()

        return self.kaisuu[0]


# n = random.randint(2, 10001)
# a = random.randint(1, 11)
# b = random.randint(1, 11)
n = int(input())
a, b = map(int, input().split())

game = Game(n, a, b)
print(game.num_of_deal())
