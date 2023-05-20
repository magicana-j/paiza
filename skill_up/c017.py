import os
dirname = os.path.dirname(__file__)

in_file = dirname + '/input.txt'
f = open(in_file, 'r', encoding='UTF-8')


def game(a, b):
    result = ""
    if a[0] == b[0]:
        if a[1] < b[1]:
            result = "High"
        else:
            result = "Low"
    elif a[0] > b[0]:
        result = "High"
    else:
        result = "Low"

    return result


oya = list(map(int, f.readline().strip().split()))
n = int(f.readline().strip())
ko = []
for i in range(n):
    ko.append(list(map(int, f.readline().strip().split())))
# print(oya)
# print(ko)
for i in range(n):
    print(game(oya, ko[i]))
