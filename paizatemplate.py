# coding: utf-8

import fileinput

m = int(input())
a1 = []
b1 = []
for line in fileinput.input():
    tokens = line.strip.split()
    a1.append(tokens[0])
    b1.append(tokens[1])

n = int(input())
a2 = []
b2 = []
for line in fileinput.input():
    tokens = line.strip.split()
    a2.append(tokens[0])
    b2.append(tokens[1])
