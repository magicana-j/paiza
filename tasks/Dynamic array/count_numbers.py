def count_numbers(arry):
    l = len(arry)
    result = [0] * 10
    s = "".join(arry)
    for i in range(10):
        cnt = s.count(str(i))
        result[i] = cnt
    return result


s = "5"
c = list(map(str, "1 2 3 4 5".split()))
counts = count_numbers(c)
print(" ".join(map(str, counts)))
