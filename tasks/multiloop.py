# coding: utf-8

import fileinput

m = int(input())
c = []
for line in range(m):
    token = input()
    c.append(token)

n = int(input())
s = []
for line in range(n):
    token = input()
    s.append(token)


for i in range(m):
    for j in range(n):
        if c[i] in s[j]:
            print("YES")
        else:
            print("NO")
