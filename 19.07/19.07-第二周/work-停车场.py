class Park(object):
    def __init__(self, price):
        self.price = price

    def money(self, time):
        money = self.price * time
        return money


class Coach(Park):
    def __init__(self, name,price):
        self.name = name
        self.time = 0
        super().__init__(price)

    def time(self, hour):
        self.time = hour


class Truck(Park):
    def __init__(self, name, price):
        self.name = name
        self.time = 0
        super().__init__(price)

    def time(self, hour):
        self.time = hour


class Limousine(Park):
    def __init__(self, name, price):
        self.name = name
        self.time = 0
        super().__init__(price)

    def time(self, hour):
        self.time = hour


guangqi = Coach('广汽', 6)
futian = Truck('福田', 8)
bujiadi = Limousine('布加迪', 5)

Price_List = {'客车': guangqi.price, '货车': futian.price, '轿车': bujiadi.price}
print('**********价目表**********')
for key in Price_List:
    print(key+' | '+str(Price_List[key]))

a = input('车辆种类为:')
b = float(input('车辆停放时间(小时):'))
if a == '客车':
    print(guangqi.money(b))
elif a == '货车':
    print(futian.money(b))
elif a == '轿车':
    print(bujiadi.money(b))
