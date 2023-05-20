import os
dirname = os.path.dirname(__file__)

in_file = dirname + '/input.txt'
f = open(in_file, 'r', encoding='UTF-8')

explanation = f.readline().strip()


def print_list(my_list):
    print(" ".join(map(str, my_list)))


a = list(explanation.split("+"))
numbers = []
for i in a:
    ten = i.count('<') * 10
    one = i.count('/')
    number = ten + one
    numbers.append(number)
print(sum(numbers))
