# coding: utf-8
# Your code here!
import fileinput


class Solution:
    a = []
    b = []

    def __init__(self, a, b):
        self.a = a
        self.b = b


if __name__ == "__main__":
    n = int(input())
    for line in fileinput.input():
        tokens = line.strip().split()
        a, b = int(tokens[0]), int(tokens[1])
        print("%d %d" % (a, b))
