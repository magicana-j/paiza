# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！
n = int(input()) # 人数
balls = []  # 持っているボールの数
for i in range(n):
    balls.append(int(input()))
m = int(input())    # パスクエリの行数
qry = []
for i in range(m):
    qry.append(list(map(int, input().split())))
#print(balls)
#print(qry)

def passing(person, qry):
    result = person
    from_person = qry[0]-1
    to_person = qry[1]-1
    ball = qry[2]

    #print(result)
    #print("from: ", from_person)
    #print("to: ", to_person)

    if ball > person[from_person]:
        #print("number of balls: ", ball, person[from_person])

        result[to_person] += person[from_person]
        result[from_person] = 0
    else:
        #print("number of balls: ", ball)

        result[from_person] -= ball
        result[to_person] += ball
    return result

t = balls
for i in range(m):
    t = passing(t, qry[i])
for i in t:
    print(i)
