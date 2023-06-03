# coding: utf-8

# 名前辞書の作成とダメージ初期化
# 一時リストを作成した後にまとめて辞書型に変換する
num_of_names = int(input())
list_dic = []
for line in range(num_of_names):
    name = input()
    temp_list = [name, 0]
    list_dic.append(temp_list)
damage_dict = dict(list_dic)

# print(damage_dict)

# 各ターンの対象およびダメージ入力と、合計ダメージ更新
num_of_turns = int(input())
for line in range(num_of_turns):
    target, damage = input().split()
    damage = int(damage)
    damage_dict[target] += damage

# print(damage_dict)

# 検索対象者の合計ダメージ表示
person = input()
print(damage_dict[person])
