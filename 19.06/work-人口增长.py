people = 13
count = 0
while people <= 26:
    people *= (1+0.8/100)
    count += 1
print('%d年后我国人口达到26亿！'% count)