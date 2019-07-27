from company import Company
import time
import threading


index = 0


def day_of_neuedu(company: Company):
    global index
    if index % 7 == 0:
        student_num = len(company.income_money)
        total_income = sum(map(lambda x: x.income, company.income_money))

        print('-'*30 + f'周末休息'+'-'*30)
        print(f'\033[1;35m截止目前共有{student_num}名学员来到东软睿道学习,公司总营收收入{total_income}元\033')
        print('-'*30+f'周末休息'+'-'*30)
        time.sleep(3)

    print('-'*30+f'东软睿道美好的一天开始了,各部门员工紧张忙碌了起来'+'-'*30)

    print('市场部开始接待客户')
    student = company.get_student()
    if student:
        company.add_money(student)
        company.add_student_to_noclasslist(student)

    print(f'当前有{len(company.classes)}个班级在上课')

    class_removed = []

    if len(company.classes) > 0:
        print('实施部的大咖们开始给学员上课了')

    for c in company.classes:
        is_closed = c.stand_up()
        for student in c.students:
            student.study()
        if is_closed:
            class_removed.append(c)

    for c_del in class_removed:
        print(f'{c_del.class_name}学生毕业了,全部找到高薪工作,迎娶白富美,走上人生巅峰')
        company.classes.remove(c_del)

    global timer
    timer = threading.Timer(1, day_of_neuedu, [company])
    timer.start()


company = Company()
timer = threading.Timer(1, day_of_neuedu, [company])

timer.start()