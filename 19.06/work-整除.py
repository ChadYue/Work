import random
n = int(input('请输入随机整数的最大值：'))
a = random.randint(1,n)
if a%5 == 0 and a%6 == 0:
    print(f'{a}能被5和6整除！')
elif a%5 == 0:
    print(f'{a}能被5整除！')
elif a%6 == 0:
    print(f'{a}能被6整除！')
else:
    print(f'{a}不能被5或6整除！')