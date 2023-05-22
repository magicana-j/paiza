kuku = [[0 for j in range(9)] for i in range(9)]
length_total = 2 * 9 + len(" | ") * 8
for dan in range(9):
    for i in range(9):
        kuku[dan][i] = (dan + 1) * (i + 1)
for i in range(9):
    for j in range(9):
        if j < 8:
            print("{:>2d}".format(kuku[i][j]), end="")
            print(" | ", end="")
        else:
            print("{:>2d}".format(kuku[i][j]))
    if i < 8:
        print("=" * length_total)
