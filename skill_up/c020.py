# coding: utf-8

m = 1   # 仕入れ量
p = 80  # 生で売れた量
q = 40  # 加工して売れた量

urenokori1 = round(m * (1 - (p/100)), 4)
urenokori2 = round(urenokori1 * (1 - (q/100)), 4)

print(urenokori2)
