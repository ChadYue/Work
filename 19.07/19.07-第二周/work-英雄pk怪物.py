import random


class Sprite:

    def __init__(self, flood, strength):
        self.X = random.randint(0, 5)
        self.Y = random.randint(0, 5)
        self.flood = flood
        self.strength = strength

    def calc_health(self):
        return self.flood

    # def move(self):
    #     a = random.randint(1, 2)
    #     b = random.randint(-1, 1)
    #     print(b)
    #     if a == 1:
    #         if self.X + b > 5:
    #             self.X = 10 - (self.X + b)
    #         elif self.X - b < 0:
    #             self.X = b - self.X
    #         else:
    #             self.X += b
    #     elif a == 2:
    #         if a == 1:
    #             if self.Y + b > 10:
    #                 self.Y = 10 - (self.Y + b)
    #             elif self.Y - b < 0:
    #                 self.Y = b - self.Y
    #             else:
    #                 self.Y += b
    #     return self.X, self.Y

    def combat(self, attack_sprite):
        dmage = random.randint(attack_sprite.strength - 5, attack_sprite.strength + 5)
        self.flood -= dmage
        if self.flood <= 0:
            print(f'{self.name}你被{attack_sprite.name}杀死了.')
            return True
        else:
            print(f'{self.name}闪避不及,被{attack_sprite.name}攻击了,受到了{str(dmage)}点伤害!,还剩{str(self.flood)}滴血!')
            return False


class Hero(Sprite):
    def __init__(self, name, flood, strength):
        self.name = name
        super().__init__(flood, strength)


class Monster(Sprite):
    def __init__(self, name, flood, strength):
        self.name = name
        super().__init__(flood, strength)


# b = {1: ['史莱姆', 20, 10], 2: ['盗贼', 30, 30], 3: ['强盗', 80, 20]}
# place = {1: ['强盗头领', 100, 50]}
# monster = []
# x = 'n'
# y = 0
# z = 0
# hero = Hero('琦玉', 100, 50)
# for i in range(2, 11):
#     a = random.randint(1, 3)
#     place[i] = b[a]
# for key, value in place.items():
#     for n in value[:1]:
#         x = str(n)
#     for n in value[1:2]:
#         y = int(n)
#     for n in value[2:]:
#         z = int(n)
#     print(x, y, z)
#     key = Monster(x, y, z)
#     monster.append(key)
# i = 0
hero = Hero('琦玉', 100, 50)
monster = Monster('强盗头领', 100, 50)
while True:
    # for key in monster:
    #     key.move()
    #     print((key.X, key.Y))
    # hero.move()
    # print((hero.X, hero.Y))
    # for key in monster:
    #     if key.X == hero.X and key.Y == hero.Y:
    is_monster_died = monster.combat(hero)
    if is_monster_died:
        break
    is_hero_died = hero.combat(monster)
    if is_monster_died:
        # flog = False
        break
    # if i == 4:
    #     print(f'{hero.name} Win!')
    #     break