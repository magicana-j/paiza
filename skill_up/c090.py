import os
dirname = os.path.dirname(__file__)

in_file = dirname + '/c090_input.txt'
f = open(in_file, 'r', encoding='UTF-8')


def print_list(my_list):
    print(" ".join(map(str, my_list)))


phone = [12, 3, 4, 5, 6, 7, 8, 9, 10, 11]
s = list(map(str, f.readline().strip()))
# print(s)
number = list(map(int, [i for i in s if i != '-']))
# print(number)
length = len(number)
kyori = 0
for i in range(length):
    kyori += phone[number[i]]
print(kyori*2)
