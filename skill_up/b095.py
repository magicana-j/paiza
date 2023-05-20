import os
dirname = os.path.dirname(__file__)

in_file = dirname + '/input.txt'
f = open(in_file, 'r', encoding='UTF-8')


def saiten(correct, person):
    length = len(correct_melody)
    point = 100
    for i in range(length):
        err = abs(person[i] - correct[i])
        if err <= 5:
            point = point
        elif err <= 10:
            point = point - 1
        elif err <= 20:
            point = point - 2
        elif err <= 30:
            point = point - 3
        else:
            point = point - 5
    return point


n, m = map(int, f.readline().strip().split())
correct_melody = []

for i in range(m):
    correct_melody.append(int(f.readline().strip()))
# print(correct_melody)

melody = [[0 for j in range(m)] for i in range(n)]
for i in range(n):
    for j in range(m):
        melody[i][j] = int(f.readline().strip())
# print(melody)
mx = 0
for i in range(n):
    p = saiten(correct_melody, melody[i])
    if p > mx:
        mx = p
print(mx)
