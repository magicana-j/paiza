# C123:節分ロボットの問題


def solve(y, qu):
    # y: 参加者の年齢リスト
    # qu: クエリリスト
    length = len(qu)
    result = [0 for i in range(len(y))]
    for i in range(length):
        start = qu[i][0] - 1
        end = qu[i][1]
        mame = qu[i][2]
        for j in range(start, end):
            if mame + result[j] <= y[j]:
                result[j] += mame
            else:
                result[j] = y[j]

    return result


n = 5

# n = int(input())
y = [10, 20, 30, 40, 50]
# y=[]
# for i in range(n):
#    y.append(int(input()))
# m = int(input())
m = 2
# qu = []
qu = [[2, 4, 10], [1, 3, 15]]
# for i in range(m):
#    qu.append(list(map(int,input().split())))


ans = solve(y, qu)
for i in range(len(ans)):
    print(ans[i])
