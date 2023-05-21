def solve(days, cond_min, cond_max, prices):
    rieki = 0
    mochikabu = 0
    for d in range(days):
        if d == days - 1:
            rieki += prices[d] * mochikabu
            mochikabu = 0
        else:
            if prices[d] <= cond1:
                mochikabu += 1
                rieki -= prices[d]
            elif prices[d] >= cond2 and mochikabu != 0:
                rieki += prices[d] * mochikabu
                mochikabu = 0
    return rieki


# days, cond1, cond2 = list(map(int, input().stlip()))
# prices = []
# for i in range(days):
#    prices.append(int(input()))
days = 5
cond1 = 110
cond2 = 120
prices = [110, 100, 120, 130, 105]
# 110
# 100
# 120
# 130
# 105

print(solve(days, cond1, cond2, prices))
