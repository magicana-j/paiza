# coding: utf-8
def int_input():
    return int(input())


def multi_input():
    return map(str, input().strip().split())


def line_to_intlist():
    return list(map(int, input().strip().split()))


def line_to_strlist():
    return list(map(str, input().strip().split()))


def input_to_n_lists(n: int):
    result = []
    for _ in range(n):
        result.append(line_to_intlist())
    return result


def join_list_to_str(l: list):
    return " ".join(list(map(str, l)))


def print_each_element(l: list):
    for _ in len(l):
        print(l[_])


"""
int_input()             数値を一つ入力
multi_int_input()       数値を複数入力
line_to_intlist()       一行のスペース区切り整数データを一次元リストに格納
line_to_strlist()       一行のスペース区切りデータを一次元リストに格納
input_to_n_lists(n)     n行のスペース区切りデータを多次元リストに格納
join_list_to_str(l)     一次元数値リストlをスペース区切り文字列に変換
"""
import fileinput

if __name__ == "__main__":
    n = int(input())
    a1 = []
    b1 = []
    for line in fileinput.input():
        tokens = line.strip.split()
        a1.append(tokens[0])
        b1.append(tokens[1])

    m = int(input())
    a2 = []
    b2 = []
    for line in fileinput.input():
        tokens = line.strip.split()
        a2.append(tokens[0])
        b2.append(tokens[1])
