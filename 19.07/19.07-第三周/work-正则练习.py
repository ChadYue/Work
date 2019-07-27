import re
# # 1、 匹配一段文本中的每行的时间字符串，比如：‘1990-07-12’；
# time = 'asfasf1990-07-12asdfAAAbbbb434241'
# o = re.findall(r'\d{4}-\d{2}-\d{2}', time)
# print(o)
#
# # 2、匹配一段文本中所有的身份证数字。
# a = 'sfafsf,34234234234,1231313132,154785625475896587,sdefgr54184785ds85,4864465asf86845'
# s = re.findall(r'\d{14}\w{4}', a)
# print(s)
#
# # 3、匹配qq号。(腾讯QQ号从10000开始)  [1-9][0-9]{4,}
# q = '3344,88888,7778957,10000,99999,414,4,867287672'
# q = re.sub(r'\D', " ", q)
# t = re.findall(r'[1-9][0-9]{4,}', q)
# print(t)
#
# # 4、匹配一个浮点数
# s = '-1,-2.5,8.8,1,0'
# f = re.findall(r'-*\d[.]\d', s)
# print(f)
#
# # 5、写一个正则表达式，使其能同时识别下面所有的字符串：'bat','bit', 'but', 'hat', 'hit', 'hut'
# s = "bat,bit,but,hit,hut"
# F = re.findall(r'[bh][aiu]t', s)
# print(F)
#
# # 6、匹配以“www”起始且以“.com”结尾的简单Web域名:例如,http://www.yahoo.com ，也支持其他域名，如.edu .net等
# s = "http://www.yahoo.com   www.foothill.edu"
# S = re.findall(r'[w]{3}.\w{1,}.(?:com|edu|net)', s)
# print(S)
#
# # 7、匹配一段文本中的每行的邮箱
# y = '123@qq.comaaa@163.combbb@126.comasdfasfs33333@adfcom'
# S = re.findall(r'\w+@(?:qq|163|126).com', y)
# print(S)

# 1.把a1b23c4d非字符内容拼成一个字符串  2.把一个字符串中的所有字母找出并拼成一个字符串
s = 'a1b23c4d'
n = re.findall(r'\d', s)
S = re.findall(r'\D', s)
print(''.join(n))
print(''.join(S))

# 3.统计一个字符串中单词的数量
s = "hello world he-llo china"
w = re.findall(r'[a-zA-Z]{1,}', s)
print(len(w))

# 4.统计一个文件中单词的数量
with open('Demo01·19.07.26.py', 'r+', encoding='utf-8') as f:
    lines = f.readlines()
print(lines)
p = re.findall(r'[a-zA-Z]{1,}', str(lines))
print(p)
print(len(p))

# 5.编写匹配ip的正则表达式
s = '254.16.23.189'
ip = re.findall(r'', s)
print(ip)