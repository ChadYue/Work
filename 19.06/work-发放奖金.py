profit = int(input('请输入企业当月利润(万)：'))
bouns = 0
if profit <= 10:
    bonus = profit * 0.1
elif profit <= 20:
    bonus = 10 * 0.1 + (profit - 10) * 0.075
elif profit <= 40:
    bonus = 10 * 0.175 + (profit - 20) * 0.05
elif profit <= 60:
    bonus = 10 * 0.275 + (profit - 40) * 0.03
elif profit <= 100:
    bonus = 10 * 0.335 + (profit - 60) * 0.015
else:
    bonus = 10 * 0.395 + (profit - 100) * 0.01
print(f'应发放{bonus}万奖金！')