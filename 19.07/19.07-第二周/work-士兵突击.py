import time,random
class soldier:
    def __init__(self):
        self.name = '许三多'
        self.gun = None

    def fire(self):
        if self.gun == None:
            print('该士兵没有枪,无法射击!')
        else:
            print(f'{self.name}:冲啊!!!')
            self.gun.shoot()
            time.sleep(2)


class Gun:
    def __init__(self,model):
        self.model = model
        self.bullet_count = 0

    def add_bullet(self,count):
        self.bullet_count += count

    def shoot(self):
        if self.bullet_count > 0:
            self.bullet_count -= 1
            print(f'{self.model}突突突...剩余{self.bullet_count}颗子弹!')
        else:
            print(f'{self.model}里没有子弹了!')

Ak47 = Gun('Ak47')
Ak47.add_bullet(30)

xuesanduo = soldier()
xuesanduo.gun = Ak47
a = int(input('输入敌人数量:'))
n = int(input('背包内弹药数量:'))
a_hp = 100
Hp = 100
i = 0
while i <= a:
    c = float(format(random.random(),'.2f'))
    if c >= 0.3333333333:
        print('遇见敌人了!')
        time.sleep(2)
        a_hp = 100
        t = 1
        while a_hp > 0:
            if t == 1:
                if Ak47.bullet_count != 0:
                    xuesanduo.fire()
                    t = 2
                    b = float(format(random.random(),'.2f'))
                    if b >= 0.6:
                        print('打中敌人身体!')
                        time.sleep(2)
                        a_hp -= 40
                    elif b <= 0.2:
                        print('爆头!')
                        time.sleep(2)
                        a_hp -= 100
                    else:
                        print('打空了!')
                        time.sleep(2)
                else:
                    print('子弹打完了!')
                    x = input('是否装弹(Y/N):')
                    if x.lower() == 'y':
                        if n == 0:
                            print('game over!')
                            break
                        elif n <= 30:
                            Ak47.add_bullet(n)
                            n = 0
                        else:
                            Ak47.add_bullet(30)
                            n -= 30
                    else:
                        print('game over!')
                        break
            elif t == 2 and a_hp > 0:
                t = 1
                b = float(format(random.random(), '.2f'))
                if b >= 0.6:
                    print('敌人打中身体!')
                    Hp -= 20
                    time.sleep(2)
                elif b <= 0.1:
                    print('敌人爆头!')
                    Hp -= 50
                    time.sleep(2)
                else:
                    print('敌人打空了!')
                    time.sleep(2)
            if Hp <= 0:
                n = 0
                print('game over!')
                break
        if n == 0:
            break
        if i == a:
            print('Winner')
            break
        print('打倒敌人了!')
        time.sleep(2)
        i += 1
    elif c <= 0.33333333333:
        print('发现弹药了!')
        time.sleep(2)
        n += 50
    else:
        print('发现急救包!')
        time.sleep(2)
        Hp += 30