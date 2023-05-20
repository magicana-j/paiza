def digital_root(n):
    res = str(n)
    while len(res) > 1:
        l = list(map(int, res))
        res = str(sum(l))
    return int(res)


print(digital_root(16))
