class HouseItem:
    def __init__(self,name,area):
        self.name = name
        self.area = area

    def __str__(self):
        return ' %s | 占地:%.2f'%(self.name,self.area)

class House:
    def __init__(self,style,area):
        self.style = style
        self.free_area=area
        self.area = area
        self.item_list =[]
    def add_item(self,item):
        if self.free_area - 40 > item.area:
            self.item_list.append(item.name)
            self.free_area -= item.area
            print('家具已添加!')
        else:
            print('房屋面积不够')
    def __str__(self):
        return (' 户型:%s | 总面积:%.2f \n 家具清单:%s \n 剩余面积:%.2f')%(
            self.style,self.area,self.item_list,self.free_area)

house_style = input('请输入房屋户型:')
house_area = int(input('请输入房屋面积:'))
my_house = House(house_style,house_area)
item = {'席梦思':4,'衣柜':2,'餐桌':1.5,'电视柜':1.5,'浴缸':3,'沙发':3,'电脑桌':1,'茶几':2}
flag = True
print('请添加家具!')
while flag != False:
    print(' 家具名称 | 占地面积 ')
    for key in item:
        print(' '+key+' | '+str(item[key]))
    item_name = input('请输入想添加的家具名称:')
    item_area = item[item_name]
    my_item = HouseItem(item_name,item_area)
    my_house.add_item(my_item)
    a = input('是否继续添加家具(y/n):')
    if a.lower() == 'y':
        flag = True
    else:
        flag = False
print(my_house)