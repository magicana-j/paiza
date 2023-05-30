# coding: utf-8
def int_input():
    return int(input())


def multi_int_input():
    return map(int, input().strip().split())


def line_to_int_list():
    return list(map(int, input().strip().split()))


def input_to_n_lists(n: int):
    result = []
    for _ in range(n):
        result.append(line_to_int_list())
    return result


def join_list_to_str(l: list):
    return " ".join(list(map(str, l)))


def print_each_element(l: list):
    for _ in len(l):
        print(l[_])


"""
int_input()             数値を一つ入力
multi_int_input()       数値を複数入力
line_to_int_list()      一行のスペース区切りデータを一次元リストに格納
input_to_n_lists(n)     n行のスペース区切りデータを多次元リストに格納
join_list_to_str(l)     一次元数値リストlをスペース区切り文字列に変換
"""

"""
xc yc r_1 r_2
n
x_1 y_1
x_2 y_2
...
x_n y_n

1 から n 番目の人まで順に、暴風域にいれば "yes"、そうでなければ "no" を、それぞれ一行に出力してください。
最後は改行し、余計な文字、空行を含んではいけません。
"""

import math


def boufuuken(x, y, xc, yc, r1, r2):
    cond = (x - xc) ** 2 + (y - yc) ** 2
    if r1**2 <= cond and r2**2 >= cond:
        return True
    else:
        return False


xc, yc, r_1, r_2 = map(int, input().strip().split())
n = int(input())

for i in range(n):
    x, y = map(int, input().strip().split())
    if boufuuken(x, y, xc, yc, r_1, r_2):
        print("yes")
    else:
        print("no")
