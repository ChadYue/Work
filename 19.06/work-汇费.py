money = int(input('请输入汇款金额：'))
if money < 100:
    money = 1
elif money < 5000:
    money *= 0.01
else:
    money = 50
print(f'您的汇费为{money}元！')