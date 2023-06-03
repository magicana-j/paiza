import random


class Character:
    def __init__(self, hp, coef):
        self.hp = hp
        self.coef = [1, coef]
        self.damage = [0, 0]

    def attack(self):
        d = self.damage[1] * self.coef[1] + self.damage[0] * self.coef[0]
        if self.damage[0] * self.damage[1] == 0:
            print("条件満たさず")
            d = 1
        print("damage: ", d)
        return d

    def damaged(self, d):
        self.hp -= d
        self.damage[0] = self.damage[1]
        self.damage[1] = d

    def show_damage_history(self):
        return self.damage

    def hp_remains(self):
        return self.hp


hp = random.randint(3, 100)

paiza = Character(100, 1)
enemy = Character(999999999, 2)

turn = 0
while paiza.hp_remains() >= 0:
    turn += 1
    print("\nturn: ", turn)

    print(enemy.show_damage_history())
    enemy.damaged(paiza.attack())
    print("enemy HP: ", enemy.hp_remains())

    print(paiza.show_damage_history())
    paiza.damaged(enemy.attack())
    print("paiza HP: ", paiza.hp_remains())

print(turn)
