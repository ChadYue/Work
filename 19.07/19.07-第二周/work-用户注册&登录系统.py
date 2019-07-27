# 使用python代码实现如下功能:
#     一、用户注册功能
#         需求:实现用户注册功能，并将用户注册信息保存到磁盘文件中，用户注册时给定:用户名和密码，用户名不能重复
#     二、用户登录功能
#         需求:根据系统提示，用户输入用户名和密码，当用户名和密码给定正确的时候，显示登录成功，
#             否则登录失败;


def sign_in_name(id_name, id_dict):
    for key in id_dict:
        if id_name == key:
            print('该用户名已注册!')
            return True
        else:
            return False


def sign_in_password(id_name, id_dict):
    id_password1 = input('请输入密码:')
    id_password2 = input('请再次输入密码:')
    while id_password1 != id_password2:
        print('两次密码不一致请再次输入密码1')
        id_password1 = input('请输入密码:')
        id_password2 = input('请再次输入密码:')
    id_dict[id_name] = id_password1
    print(f'用户{id_name}注册成功!请牢记您的用户名及密码')


def log_in(id_dict):
    id_name = input('请输入用户名:')
    if id_name in id_dict.keys():
        i = 0
        while i < 3:
            id_password = input('请输入密码:')
            if id_dict[id_name] == id_password:
                print('登陆成功')
                break
            elif i < 2:
                i += 1
                print('用户名&密码不正确,请重新输入(输入次数%d/3)!' % i)
            else:
                print('用户名&密码不正确,请重新输入(输入次数3/3)!')
                print('登录失败!')
                i += 1
    else:
        print('该用户未注册,请重新注册!')


id_dict = {}
with open('a.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()
    for line in lines:
        line = str(line).strip()
        if line[:7] == 'id_name':
            key = line[8:]
        elif line[:11] == 'id_password':
            id_dict[key] = line[12:]
print(id_dict)
print('欢迎登录***系统'+'\n'+'1: 登录 ; 2: 注册')
a = input('登录 or 注册:')
if a == '2':
    id_name = str(input('请输入用户名:'))
    while sign_in_name(id_name, id_dict):
        id_name = input('请输入用户名:')
    sign_in_password(id_name, id_dict)
elif a == '1':
    log_in(id_dict)
with open('a.txt', 'w', encoding='utf_8') as f:
    for key, value in id_dict.items():
        f.write('id_name:' + key + '\n')
        f.write('id_password:' + id_dict[key] + '\n')
        f.write('-' * 30 + '\n')