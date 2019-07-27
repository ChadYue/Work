sum = 1
for i in range(1,101):
    if i%3 == 0:
        sum +=i
print('1到100之间所有能被3整除的整数的和为%d'% sum)


sum = 1
i = 1
while i <= 100:
    if i%3 == 0:
        sum += i
    i += 1
print('1到100之间所有能被3整除的整数的和为%d'% sum)