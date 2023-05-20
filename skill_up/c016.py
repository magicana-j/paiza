# coding: utf-8

s = 'BCDFHJKLMNOPQRTUVWXY'
my_list = list(s)


def leet(lst):
    rules = {
        'A': '4',
        'E': '3',
        'G': '6',
        'I': '1',
        'O': '0',
        'S': '5',
        'Z': '2'
    }

    result = []
    for i in range(len(lst)):
        found = rules.get(lst[i], -1)
        if found == -1:
            result.append(lst[i])
        else:
            result.append(found)
    return result


new_list = leet(my_list)
s = "".join(new_list)
print(new_list)
print(s)
