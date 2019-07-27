q = 'hello world god is allways busy'
b = 'a'
for i in ''.join(sorted(list(''.join(q.split())))):
    if i != b:
        print(f'{b}:{q.count(b)}',end=" ")
        b = i
# a = 0
# while a != -1:
#     a = q.find(' ')
#     if a != -1:
#         b = a+1
#         q = q[:a]+q[b: ]
# x = list(q)
# x.sort()
# c = 1
# b = 1
# for a in range(c,len(x)):
#     if x[a-1] == x[a]:
#         b = b+1
#     else:
#         print(f'{x[a-1]}:{b}',end=" ")
#         c = a
#         b = 1
# x = list(say)
# x.sort()
# b = x.index('a')
# b = int(b)
# del x[:b]
# print(x)