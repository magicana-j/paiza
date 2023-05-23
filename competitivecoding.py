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
        print(l[i])


"""
int_input()             数値を一つ入力
multi_int_input()       数値を複数入力
line_to_int_list()      一行のスペース区切りデータを一次元リストに格納
input_to_n_lists(n)     n行のスペース区切りデータを多次元リストに格納
join_list_to_str(l)     一次元数値リストlをスペース区切り文字列に変換
"""

if __name__ == "__main__":
    # code here
    records = [["chi", 20.0], ["beta", 50.0], ["alpha", 50.0]]
    records.sort()
    score_list = []
    for i in range(len(records)):
        score_list.append(records[i][1])
    sorted_score = sorted(list(set(score_list)))
    for i in range(len(records)):
        if records[i][1] == list(sorted_score)[1]:
            print(records[i][0])
