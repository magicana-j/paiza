# coding: utf-8

s = "Torvalds"
l = list(s)
vowels = list("aiueoAIUEO")
print(l)
print(vowels)


def my_index(l, x, default=False):
    if x in l:
        return l.index(x)
    else:
        return default


new_s = []
for idx in range(len(l)):
    found = my_index(vowels, l[idx], -1)
    if found == -1:
        new_s.append(l[idx])

print("".join(new_s))
