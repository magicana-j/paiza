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


def inputs_to_lists(n: int):
    s = []
    for _ in range(n):
        s.append(input())
    return s


n = int_input()
strs = inputs_to_lists(n)
print(strs)
new_set = sorted(list(set(strs)))
for _ in range(len(new_set)):
    cnt = strs.count(new_set[_])
    print(new_set[_], cnt)
