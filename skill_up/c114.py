import os
dirname = os.path.dirname(__file__)

in_file = dirname + '/input.txt'
f = open(in_file, 'r', encoding='UTF-8')


def print_list(my_list):
    print(" ".join(map(str, my_list)))


n = int(f.readline())
words = []
for i in range(n):
    words.append(f.readline().strip())
bad_case = []
for i in range(n-1):
    end_letter = words[i][-1]
    start_letter = words[i+1][0]
    if end_letter != start_letter:
        bad_case.append([end_letter, start_letter])
if bad_case == []:
    print("Yes")
else:
    print_list(bad_case[0])
