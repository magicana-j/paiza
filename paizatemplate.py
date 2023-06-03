# coding: utf-8

import fileinput

m = int(input())
# n,m,k = map(int(input().split()))
a = []
for line in fileinput.input():
    data = map(int, line.strip().split())
    # data = map(str, line.strip().split())
    a.append(list(data))
    # a.append(int(line))
