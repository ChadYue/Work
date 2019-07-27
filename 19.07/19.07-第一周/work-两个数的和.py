num = [2,7,11,15,1,8,7]
y = []
for a in range(len(num)):
    for b in range(len(num)):
        if a != b and num[a]+num[b] == 19:
            if num[a] < num[b]:
                x = (num[a],num[b])
                if y.count(x) == 0:
                    y.append(x)
            else:
                x = (num[b], num[a])
                if y.count(x) == 0:
                    y.append(x)

print(y)