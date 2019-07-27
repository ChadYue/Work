num = 200
while num >= 200:
    for i in range(2,num):
        if num %i == 0:
            num += 1
            break
    else:
        print('%d是大于200的最小质数!'% num)
        break