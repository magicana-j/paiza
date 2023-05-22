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


"""
int_input()             数値を一つ入力
multi_int_input()       数値を複数入力
line_to_int_list()      一行のスペース区切りデータをリストに格納
input_to_n_lists(n)     n行のスペース区切りデータを多次元リストに格納
join_list_to_str(l)     数値リストをスペース区切り文字列に変換
"""


n = int_input()
x, y, z = multi_int_input()
a = line_to_int_list()
m = int_input()
q = input_to_n_lists(m)
