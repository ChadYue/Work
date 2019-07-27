import random
class tortoise:
    def __init__(self):
        self.tortoise_X = random.randint(0,5)
        self.tortoise_Y = random.randint(0,5)
        self.power = 100
    def move(self):
        a = random.randint(1,4)
        b = random.randint(1,2)
        self.power -= 1
        if a == 1:
            if self.tortoise_X + b > 5:
                self.tortoise_X = 10 - (self.tortoise_X + b)
            else:
                self.tortoise_X += b
        elif a == 3:
            if self.tortoise_X - b < 0:
                self.tortoise_X = b - self.tortoise_X
            else:
                self.tortoise_X -= b
        elif a == 2:
            if self.tortoise_Y + b > 5:
                self.tortoise_Y = 10 - (self.tortoise_Y + b)
            else:
                self.tortoise_Y += b
        elif a == 4:
            if self.tortoise_Y - b < 0:
                self.tortoise_Y = b - self.tortoise_Y
            else:
                self.tortoise_Y -= b

        return self.tortoise_X,self.tortoise_Y
class fish:
    def __init__(self):
        self.fish_X = random.randint(0, 5)
        self.fish_Y = random.randint(0, 5)

    def Move(self):
        a = random.randint(1, 4)
        if a == 1:
            if self.fish_X == 5:
                self.fish_X -= 1
            else:
                self.fish_X += 1
        elif a == 3:
            if self.fish_X == 0:
                self.fish_X += 1
            else:
                self.fish_X -= 1
        elif a == 2:
            if self.fish_Y == 5:
                self.fish_Y -= 1
            else:
                self.fish_Y += 1
        elif a == 4:
            if self.fish_Y == 0:
                self.fish_Y += 1
            else:
                self.fish_Y -= 1

        return self.fish_Y, self.fish_Y
pond = []
n = 0
for i in range(10):
    i = fish()
    pond.append(i)
wugui = tortoise()
while wugui.power > 0:
    for key in pond:
        key.Move()
        print((key.fish_X,key.fish_Y),end=" ")
    wugui.move()
    print()
    print((wugui.tortoise_X,wugui.tortoise_Y))
    for key in pond:
        if key.fish_X == wugui.tortoise_X and key.fish_Y == wugui.tortoise_Y:
            pond.remove(key)
            wugui.power += 20
            print(f'乌龟吃掉了一条鱼,还剩{len(pond)}条鱼!')
    if len(pond) == 0:
        print('乌龟获胜,游戏结束!')
        break
    elif wugui.power == 0:
        print('乌龟死亡,游戏结束!')
        break