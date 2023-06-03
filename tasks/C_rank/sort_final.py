# coding: utf-8

import fileinput

n = int(input())
# n,m,k = map(int(input().split()))
a = []
for line in fileinput.input():
    au, ag = map(int, line.strip().split())
    # data = map(str, line.strip().split())
    lst = [au, ag]
    a.append(lst)
    # a.append(int(line))

# print(a)
new_a = sorted(a, key=lambda x: (x[1], x[0]), reverse=True)

# print(new_a)

for data in new_a:
    print(" ".join(map(str, data)))
