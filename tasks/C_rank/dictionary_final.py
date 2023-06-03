# coding: utf-8

p, q, r = map(int, input().strip().split())
ninzuu = {"A": p, "B": q, "C": r}

inquire_query1 = []
for i in range(ninzuu["A"]):
    line = map(int, input().split())
    inquire_query1.append(list(line))
inquire_dic1 = dict(sorted(inquire_query1))

inquire_query2 = []
for i in range(ninzuu["B"]):
    line = map(int, input().split())
    inquire_query2.append(list(line))
inquire_dic2 = dict(inquire_query2)

# print(inquire_dic1)
# print(inquire_dic2)

for i in inquire_dic1.keys():
    print(i, inquire_dic2[inquire_dic1[i]])
