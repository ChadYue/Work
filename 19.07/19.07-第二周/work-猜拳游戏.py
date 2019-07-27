import random


def person():
    type = int(input("请出拳（1.剪刀 2.石头 3.布）："))
    if type == 1:
        print('玩家:剪刀')
    elif type == 2:
        print('玩家:石头')
    elif type == 3:
        print('玩家:布')
    else:
        print('输入有误')
    return type


def computer():
    type = random.randint(1,3)
    if type == 1:
        print('电脑:剪刀')
    elif type == 2:
        print('电脑:石头')
    elif type == 3:
        print('电脑:布')
    return type


def game(user):
    a = {'胜': 0, '平': 0, '负': 0}
    while True:
        flag = input("是否现在开始（y/n）:")
        if flag.lower() == 'y':
            player = person()
            com = computer()
            if player == com:
                a['平'] += 1
                print("平局")
            elif (player == 1 and com == 3) or (player == 2 and com == 1)or (player == 3 and com == 2):
                a['胜'] += 1
                print(user+"胜利")
            else:
                a['负'] += 1
                print("电脑胜利")
        elif flag.lower() == 'n':
            print('游戏结束')
            break
    print(a)
    return a


x = {}
y = {}
with open('a.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()
    for line in lines:
        if line in lines[::3]:
            key = line.strip()
        elif line in lines[1::3]:
            x[key] = line.strip()
print("----------------欢迎来到猜拳游戏---------------")
while True:
    username = input("请输入用户名：")
    if username in lines:
        with open('a.txt', 'r', encoding='utf-8') as f:
            lines = f.readlines()
            for dict in lines[1::3]:
                dict = dict.strip()
                s = ' '.join(dict.split(':'))
                a = s.split()[::2]
                b = s.split()[1::2]
                i = 0
            while a:
                y[a.pop(i)] = int(b.pop(i))
    else:
        break
print(x)
a = game(username)
if y:
    for key in a:
        a[key] += y[key]
x[username] = str(a)
with open('a.txt', 'w', encoding='utf-8') as f:
    for key, vslue in x.items():
        f.write(key+'\n'+x[key]+'\n')
        f.write('-'*30+'\n')