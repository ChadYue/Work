high = int(input('请输入篮球落下高度：'))
count = 1
h = 0
while(count <= 10):
    count += 1
    h += high
    high /= 2
    h += high
print('篮球下落过程中一个经过了%s米！'% h)
print('篮球第十次落下的高度为%s米！'% high)