import random
strCountrys = "科特迪瓦，阿根廷，澳大利亚，塞尔维亚，荷兰，尼日利亚，日本，美国，中国，新西兰，巴西，比利时，韩国，喀麦隆，洪都拉斯，意大利"
Countrys = strCountrys.split('，')
zb = {}
group = ['第一组','第二组','第三组','第四组']
for key in group:
    y = []
    for j in range(1,5):
        a = random.randint(0, len(Countrys)-1)
        y.append(Countrys.pop(a))
    zb[key] = y
for key in zb:
    print(key)
    print(zb[key])