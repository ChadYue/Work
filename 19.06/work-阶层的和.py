n = int(input('若想求1-n的阶层的和，请输入n的值：'))
a = 1
sum = 0
for i in range(1,n+1):
    a *= i
    sum += a
print(f'1-{n}的阶层的和为：{sum}')