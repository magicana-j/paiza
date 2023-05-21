# coding: utf-8
def list2str(l: list) -> str:
    return "".join(list(map(str, l)))


def str2strlist(s: str) -> list:
    return list(map(str, s))


def line2numlist(line: str) -> list:
    return list(map(int, line.strip().split()))


def del_duplication(l: list) -> list:
    return list(set(l))


n = 5
g = "ai"
lst = ["pizza", "paiza", "aizu", "ai", "sai"]

ans = []
for i in lst:
    if g in i:
        ans.append(i)
if len(ans) > 0:
    for i in ans:
        print(i)
else:
    print("None")
