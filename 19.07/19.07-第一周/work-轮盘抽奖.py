import random,collections
def lp(n):
    y = []
    for i in range(0,n):
        x = float(format(random.random(),'.2f'))
        if x < 0.08:
            y.append(1)
        elif x < 0.3:
            y.append(2)
        else:
            y.append(3)
    print(f'一等奖: {y.count(1)}')
    print(f'二等奖: {y.count(2)}')
    print(f'三等奖: {y.count(3)}')
lp(1000)