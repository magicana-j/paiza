# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！

#n, x0 = map(int, input().split())
n = 5
x = [0 for i in range(n)]
x0 = 7
x[0] = x0
#declaration = list(map(int, input().split()))
declaration = [9, 10, 6, 7, 6]
x[1] = declaration[0] - x[0]
if n>2:
    for i in range(2, n-1):
        x[i] = declaration[i-1] - x[i-2] - x[i-1]
    x[n-1] = declaration[n-1] - x[n-2]
    print(" ".join(map(str,x)))
else:
    print(" ".join(map(str,x)))
