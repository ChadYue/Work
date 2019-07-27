money = 30000
count = 1
sum = 0
while count <= 10:
    money *= 1.06
    sum += money
    count += 1
print('该员工10年后的年薪为%d元，未来10年的总收入为%d元！'% (money,sum))