# coding: utf-8

def read_line(s):
    f = open(s, 'r', encoding='UTF-8')
    datalist = f.readlines()
    arguments = []
    arguments[0] = list(map(int, datalist[0].split()))
    return result
