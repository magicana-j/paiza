import os
dirname = os.path.dirname(__file__)

in_file = dirname + '/input.txt'
f = open(in_file, 'r', encoding='UTF-8')


def print_list(my_list):
    print(" ".join(map(str, my_list)))


n = int(f.readline())
a = list(map(int, f.readline().split()))

print(n)
print_list(a)
