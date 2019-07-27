# 编写装饰器，为多个函数加上认证的功能(用户的账号密码)，
# 要求登录成功一次，后续的函数都无需再输入用户名和密码
user_dic = {"username": 'admin', "password": '123'}
status = False  # 用户登录状态
i = 0


# 登录认证
def login(func):
    def inner():
        global status
        global i
        i += 1
        if not status:
            while i <= 3:
                user_name = input('user_name:')
                user_password = input('user_password:')
                if user_name != user_dic['username'] or user_password != user_dic['password']:
                    print('用户名&密码错误!')
                else:
                    status = True
                    break
                i += 1
        if not status and i <= 4:
            print('-----登录失败!-----')
        elif status:
            print('-----登录成功!-----')
            func()
        return status
    return inner


@login
def home():
    print('-----HOME-----')


@login
def bbs():
    print('-----BBS-----')
    print('-----畅所欲言-----')


home()
bbs()