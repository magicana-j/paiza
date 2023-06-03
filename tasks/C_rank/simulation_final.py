import random

hp = random.randint(3, 100000000)

damage = [[0, 0]]
damage_sum = 0


def paiza_attack(k):
    if k == 1 or k == 2:
        return 1
    else:
        return damage[0][k - 1] + damage[0][k - 2]


def enemy_attack(k):
    if k == 1 or k == 2:
        return 1
    else:
        return damage[1][k - 1] * 2 + damage[1][k - 2]


def battle(k):
    damage_e = paiza_attack(k)
    damage_p = enemy_attack(k)
    damage.append([damage_p, damage_e])
    print(damage)


i = 1
while damage_sum < hp:
    battle(i)
    i += 1
print(i)
