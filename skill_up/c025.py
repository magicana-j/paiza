# coding: utf-8
def to_space_separated_str(l: list) -> str:
    return " ".join(map(str, l))


def join2str(s: list) -> str:
    return "".join(map(str, s))


def str_to_intList(s: str) -> list:
    return list(map(int, s.strip().split()))


def tousen_check(kuji: list, atari: list) -> list:
    result = []
    for i in range(len(atari)):
        cnt = 0
        for pos in range(len(kuji)):
            for pnt in range(len(kuji)):
                if kuji[pos] == atari[i][pnt]:
                    cnt += 1
        result.append(cnt)
    return result


kuji = "1 2 3 4 5 6"
n = 3
atari = ["1 5 4 2 3 6", "9 6 2 7 1 5", "32 9 87 33 41 60"]
kuji_list = str_to_intList(kuji)
atari_list = []
for i in range(n):
    atari_list.append(str_to_intList(atari[i]))
print(kuji_list)
print(atari_list)

print(tousen_check(kuji_list, atari_list))
