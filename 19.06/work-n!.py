n = int(input('若想求n的阶层，请输入n的值：'))
a = 1
b = 1
while a <= n:
    b *= a
    a += 1
print(f'{n}!={b}')