num = input('请输入一个数字：')
x = list(num)
d = len(x)
print('这是一个%d位数字！'% d)
for i in range(0,d):
    a = i+1
    print('这个数字的第%d位为:%s'% (a,x[i]))