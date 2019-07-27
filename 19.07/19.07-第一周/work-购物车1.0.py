phone = [['Apple',7588],['SAMSUNG',5999],['HUAWEI',3999],['Xiaomi',2999],['vivo',1493]]
shopping = []
n = []
user = 'a'
while user != 'q':
    print("******商品列表******")
    for index,i in enumerate(phone):
        index += 1
        print(f'{index}. {i[0]}| {i[1]}')
    user = input('请输入您想购买的商品的编号：')
    if user.isdigit():
        user = int(user)
        if user <= len(phone):
            user -= 1
            n = phone[user]
            b = shopping.count(n)
            if b > 0:
                print(f'您的购物车中已有{b}件该商品!')
                c = str(input('是否继续添加？(Y/N):'))
                if c == 'Y' or c == 'y':
                    shopping.append(n)
                    n = []
                    print(f'已经将商品{phone[user]}加入购物车！')
                elif c == 'N' or c == 'n':
                    print(f'未将商品{phone[user]}加入购物车!')
                    n = []
                else:
                    print(f'输入无效字符!未将商品{phone[user]}加入购物车!')
                    n = []
            else:
                shopping.append(n)
                n = []
                print(f'已经将商品{phone[user]}加入购物车!')
        else:
            print('本店未出售该商品!')
    else:
        user = str(user)
        if len(shopping) != 0:
            print('您的购物车中有以下商品:')
            shopping.sort()
            for index,a in enumerate(shopping):
                print(f'{index+1}. {a[0]}| {a[1]}')
        else:
            print('您的购物车中没有商品!')