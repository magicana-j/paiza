# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！

import os
dirname = os.path.dirname(__file__)

in_file = dirname + '/input.txt'
f = open(in_file, 'r', encoding='UTF-8')

old_str = f.readline().strip()
p = list(map(int, f.readline().strip().split()))
for i in p:
    i = i-1
    
n = len(old_str)
m = len(p)
print(p)
print("second hole:", p[1])


def decode(str, qs):
    if len(str) <= 2:
        return str
    else:
        length = len(qs)
        left_str = str[:length]
        result = str[length:]
        counter = 0
        while (left_str != []):
            print("tmp=", left_str)
            print("res=", result)
            # print(result, l2)
            result.insert(qs[counter], left_str.pop(0))
            counter = counter + 1
        return decode(result, qs)


new_list = decode(list(old_str), p)
new_str = "".join(new_list)
print(new_str)
