# coding: utf-8

import fileinput

n, m, k = map(int, input().split())
lines = []
for line in fileinput.input():
    lines.append(line)

a = []
for i in range(len(lines)):
    data = map(int, lines[i].split())
    a.append(list(data))

"""
print(a)
print("people: ", len(a))
print("m: ", len(a[0]))
"""
cnt = [0] * n
for person in range(n):
    for i in range(m):
        if a[person][i] == k:
            cnt[person] += 1
for _ in cnt:
    print(_)
