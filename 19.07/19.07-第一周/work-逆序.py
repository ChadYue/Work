import random
def nx(k):
    list = []
    for i in range(0,30):
        list.append(random.randint(1,100))
    list.sort()
    if k < 30:
        print(list[:k][::-1]+list[k:][::-1])
    else:
        print('error key')
k = int(input('请输入key值:'))
nx(k)