# coding: utf-8
# Your code here!

"""
# 入力される値
入力は以下のフォーマットで与えられます。

M
a_1
a_2
...
a_M
N
b_1
b_2
...
b_N
・1 行目に A のライブ日数を表す整数 M が与えられます。
・続く M 行のうちの i 行目 (1 ≦ i ≦ M) には、バンド A の i 番目のライブの日を表す整数 a_i (1 ≦ a_i ≦ 31) が与えられます。
・続く 1 行には B のライブ日数を表す整数 N が与えられます。
・続く N 行のうちの i 行目 (1 ≦ i ≦ N) には、バンド B の i 番目のライブの日を表す整数 b_i (1 ≦ b_i ≦ 31) が与えられます。
・入力は合計で M + 1 + N + 1 行となり、入力値最終行の末尾に改行が 1 つ入ります。


# 期待する出力
a_1
a_2
...
a_31
・期待する出力は 31 行からなります。
・ 行目 (1 ≦ i ≦ 31) にはそれぞれ今月の i 日目にバンド A とバンド B のいずれのライブに行くかを表す文字列を出力してください。
　・バンド A のライブに行く場合は、大文字アルファベットの "A" を出力してください。
　・バンド B のライブに行く場合は、大文字アルファベットの "B" を出力してください。
　・ライブがない場合小文字アルファベットの "x" を出力してください。
・ 出力最終行の末尾に改行を入れ、余計な文字、空行を含んではいけません。
"""


class Live:
    schedule_a = [0] * 31
    schedule_b = [0] * 31
    gone = "B"
    go_to_live = [""] * 31

    def __init__(self, a, b):
        for _ in a:
            self.schedule_a[_ - 1] = 1
        for _ in b:
            self.schedule_b[_ - 1] = 1

    def show_schedule(self):
        print(self.schedule_a)
        print(self.schedule_b)

    def which_live(self, i):
        if self.schedule_a[i] == 0 and self.schedule_b[i] == 0:
            return "x"
        elif self.schedule_a[i] == 1 and self.schedule_b[i] == 0:
            return "A"
        elif self.schedule_a[i] == 0 and self.schedule_b[i] == 1:
            return "B"
        else:
            if self.gone == "B":
                self.gone = "A"
                return "A"
            if self.gone == "A":
                self.gone = "B"
                return "B"

    def to_go(self):
        for i in range(31):
            self.go_to_live[i] = self.which_live(i)
        print(self.go_to_live)


def stdio():
    m = int(input())
    a = []
    for _ in range(m):
        a.append(int(input()))

    n = int(input())
    b = []
    for _ in range(n):
        b.append(int(input()))


# a = [12, 13, 14, 17, 27]
# b = [11, 12, 14, 17, 28]
a = [i for i in range(15)]
b = [i for i in range(15, 31)]

live = Live(a, b)
live.show_schedule()
# for i in range(31):
#    print(live.which_live(3))
live.to_go()
