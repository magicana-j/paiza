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
spr = " | "
length1 = 1 + 1 + len(str(a)) + len(str(b)) + len(", ")
length_total = length1 * w + len(spr) * (w - 1)
for i in range(h):
    for j in range(w):
        if j < w - 1:
            print("({0:d}, {1:d})".format(a, b), end="")
            print(spr, end="")
        else:
            print("({0:d}, {1:d})".format(a, b))
    if i < h - 1:
        print("=" * length_total)
