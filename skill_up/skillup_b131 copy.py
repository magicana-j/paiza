# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！

old_str = "acbed"
p = [0, 2]
n = len(old_str)
m = len(p)
print(p)
print("second hole:", p[1])


def decode1(l1, l2):
    result = l2
    temp = l1
    counter = 0
    while (counter < m):
        # print(result, l2)
        if len(temp) == 0:
            break
        result.insert(p[counter], temp[counter])
        counter = counter + 1
    return result


s1 = "be"
s2 = "d"

print(decode1(list(s1), list(s2)))
