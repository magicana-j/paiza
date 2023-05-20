# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！

for i in range(9):
    for j in range(9):
        if j == 8:
            print("{: >2}".format((i+1)*(j+1)))
            if i != 8:
                print("="*42)
        else:
            print("{: >2} | ".format( (i+1)*(j+1) ), end="")
        