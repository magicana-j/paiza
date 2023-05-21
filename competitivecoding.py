def list2str(l: list) -> str:
    return "".join(list(map(str, l)))


def str2strlist(s: str) -> list:
    return list(map(str, s))


def line2numlist(line: str) -> list:
    return list(map(int, line.strip().split()))


def del_duplication(l: list) -> list:
    return list(set(l))
