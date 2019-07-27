class operation:
    def __init__(self,):
        self.money = 0
    def deposit(self,m):
        self.money += m
        print('存钱成功,当前余额:%.2f'% self.money)
    def withdrawal(self,d):
        if self.money >= d:
            self.money -= d
            print('取钱成功,当前余额:%.2f' % self.money)
        else:
            print('余额不足,请重新输入!')


print('欢迎来到本银行')
do = 3
op = operation()
while do != 0:
    print('您需要办理什么业务?')
    print('\n1.存款  2.取款  0.退出\n')
    do = int(input('请选择你需要办理的业务:'))
    if do == 1:
        savemoney = int(input('请输入存款金额:'))
        op.deposit(savemoney)
    elif do == 2:
        delmoney = int(input('请输入取款金额:'))
        op.withdrawal(delmoney)
    elif do == 0:
        print('谢谢使用!')
    else:
        print('暂无该业务,请重新选择!')