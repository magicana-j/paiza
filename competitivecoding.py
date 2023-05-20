def list2str(l: list) -> str:
    return "".join(list(map(str, l)))


def str2strlist(s: str) -> list:
    return list(map(str, s))


def line2numlist(line: str) -> list:
    return list(map(int, line.strip().split()))


def del_duplication(l: list) -> list:
    return list(set(l))


s = "print"
print(list2str(s))

t = "1 3 4 5"
print(line2numlist(t))

u = "1 2 2 3 4 4 4 5 6 6 7 8"
print(del_duplication(line2numlist(u)))
