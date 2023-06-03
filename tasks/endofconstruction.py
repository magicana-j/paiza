# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！
import fileinput


def strToTime(s):
    h, m = map(str, s.split(":"))
    return int(h), int(m)


def timeToStr(h, m):
    hh = str(h).zfill(2)
    mm = str(m).zfill(2)
    return hh + ":" + mm


def addTime(h1, m1, h2, m2):
    h = h1 + h2
    m = m1 + m2
    if m >= 60:
        h += 1
        m -= 60
    if h >= 24:
        h -= 24
    return h, m


def endOfConstruction(t: str, h: int, m: int):
    h1, m1 = strToTime(t)
    hh, mm = addTime(h1, m1, h, m)
    return timeToStr(hh, mm)


n = int(input())
for _ in range(n):
    t, h, m = map(str, input().split())
    h = int(h)
    m = int(m)
    print(endOfConstruction(t, h, m))
