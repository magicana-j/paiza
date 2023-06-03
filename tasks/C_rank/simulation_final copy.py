import random

# hp = random.randint(3, 100000000)
# print(hp)
hp = int(input())

paiza_damage = [1, 1]
enemy_damage = [1, 1]
damage_sum = 2

i = 1
while damage_sum < hp:
    i += 1
    # print(i + 1)
    d1 = paiza_damage[i - 1] + paiza_damage[i - 2]
    enemy_damage.append(d1)
    d2 = enemy_damage[i - 1] * 2 + enemy_damage[i - 2]
    paiza_damage.append(d2)
    # print("敵のダメージ: ", d1)
    # print("自分のダメージ: ", d2)
    damage_sum += d2
print(i + 1)
