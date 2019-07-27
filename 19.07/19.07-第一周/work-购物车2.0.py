money = int(input('请输入您的预算(元):'))

goods = [
    {"num":1,"name": "电脑", "price": 8999},
    {"num":2,"name": "鼠标", "price": 1000},
    {"num":3,"name": "游艇", "price": 1560},
    {"num":4,"name": "手机", "price": 5998}
]
car_dict = {
    '电脑':{'price':8999, 'num':0},
    '鼠标':{'price':1000, 'num':0},
    '游艇':{'price':1560, 'num':0},
    '手机':{'price':5998, 'num':0}
}
print("*****商品列表*****")
for i in goods:
    for key in i:
        print(str(i[key]),end=" ")
    print()
good = 0
while good != 'q':
    expense = 0
    for key,value in car_dict.items():
        sum = value['price'] * value['num']
        expense += sum
    good = input('请选择商品(Q/q结算):')
    a = 'a'
    if good == 'q':
        print('您的购物车:')
        print('商品名称\t\t单价\t\t数量')
        for key, value in car_dict.items():
            if value['num'] != 0:
                print(key + ':'+'\t\t'+str(value['price'])+'\t'+str(value['num']))
        print(f'总消费{expense}元,剩余{money-expense}元!')
        print("购买成功!")
    else:
        for i in goods:
            if good in i['name'] or good in str(i['num']):
                a = i['name']
                for key, value in car_dict.items():
                    if a == key:
                        expense += value['price']
                        if expense < money:
                            if value['num'] == 0:
                                value['num'] += 1
                                print('该商品已添加!')
                                break
                            else:
                                print(f'您的购物车中已有{value["num"]}件该商品!')
                                x = str(input('是否继续购买？(Y/N):'))
                                if x == 'Y' or x == 'y':
                                    value['num'] += 1
                                    print('该商品已添加!')
                                    break
                                elif x == 'N' or x == 'n':
                                    print('该商品未添加!')
                                    break
                                else:
                                    print('输入无效字符!该商品未添加!')
                                    break
                        else:
                            print('已超出预算!该商品未添加!')

        if a == 'a':
            print('尚未出售该商品!')