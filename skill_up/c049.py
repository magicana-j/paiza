# coding: utf-8

n = 3
a = [3, 1, 4]
a.insert(0, 1)

count = 0
for i in range(len(a)-1):
    count = count + abs(a[i+1]-a[i])
print(count)
