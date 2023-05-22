# coding: utf-8
def int_input():
    return int(input())


def multi_input():
    return map(int, input().strip().split())


def to_space_separated_str(l: list):
    return " ".join(list(map(str, l)))


def str2strlist(s: str):
    return list(map(str, s))


def line_to_numlist(line: str):
    return list(map(int, line.strip().split()))


h, w, a, b = multi_input()
