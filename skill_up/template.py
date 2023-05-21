# coding: utf-8
def int_input():
    """
    標準入力から整数を一つ取得する
    """
    return int(input())


def multi_int_input():
    """
    スペース区切りの整数入力を複数の変数に分割する
    """
    return map(int, input().strip().split())


def line_to_int_list():
    """
    スペース区切りの整数入力をリストに変換する
    """
    return list(map(int, input().strip().split()))


def input_to_n_lists(n: int):
    """
    n行のスペース区切り整数を多次元リストに格納する
    """
    result = []
    for _ in range(n):
        result.append(line_to_int_list(input()))
    return result


n = int_input()
x, y, z = multi_int_input()
a = line_to_int_list()
m = int_input()
q = input_to_n_lists(m)
