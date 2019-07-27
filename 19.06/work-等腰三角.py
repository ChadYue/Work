# 单循环
for a in range(1,9):
    c = 2*a-1
    d = '* '*c
    f = '  '*(8-a)
    print(f'{f}{d}')

# 嵌套循环
for x in range(1,9):
    y = 2*x-1
    for z in range(1,9-x):
        print('  ',end='')
    print('* '*y)
