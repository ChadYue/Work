from datetime import datetime
from time import time
from random import randint
import threading


class Student:
    def __init__(self):
        self.name = ''
        self.point = 0
        self.hard_degree = 0
        self.smart_degree = 0
        self.is_enter_class = False

    def pay_money(self):
        return 20000

    def study(self):
        if self.is_enter_class:
            a = 10 * (self.hard_degree + self.smart_degree)
            self.point += a
            print(f'{self.name}的经验增长了{a},达到了{self.point}')


class Course:
    def __init__(self, course_name, course_time):
        self.course_name = course_name
        self.course_time = course_time

    def __str__(self):
        return self.course_name


class CourseTable:
    def __init__(self):
        self.tables = []
        self.tables.append(Course('Python', 5))
        self.tables.append(Course('mysql', 3))
        self.tables.append(Course('flask', 5))
        self.tables.append(Course('django', 3))
        self.tables.append(Course('tensorflow', 5))


class Class:
    class_num = 1

    def __init__(self,):
        self.class_name = ''
        self.start_date = datetime.now()
        self.students = []
        self.course_table = CourseTable()

    def stand_up(self):
        is_closed = False
        c = self.course_table.tables.pop()
        print(f'{self.class_name}正在上{c.course_name}课,该课还剩余{c.course_time}个课时!')
        course_time = c.course_time - 1
        if course_time > 0:
            c.course_time = course_time
            self.course_table.tables.append(c)
        if len(self.course_table.tables) == 0:
            is_closed = True

        return is_closed


class IncomeMoney:
    def __init__(self):
        self.income = 0
        self.log = ''


class Company:
    def __init__(self):
        self.classes = []
        self.courses = []
        self.income = 0
        self.income_money = []
        self.inschool_students = []
        self.noclass_students = []
        self.num = 5

    def add_money(self, student: Student):
        print(f'财务部收款{student.pay_money()}元')
        self.income += student.pay_money()
        ir = IncomeMoney()
        ir.income = student.pay_money()
        ir.log = f'收到{student.name}学费{student.pay_money()}元'
        self.income_money.append(ir)

    def add_student_to_noclasslist(self, student: Student):
        self.noclass_students.append(student)
        size = len(self.noclass_students)
        print(f'当前招生人数{size}')
        if size >= self.num:
            c = Class()
            c.class_name = f'{Class.class_num}班'
            Class.class_num += 1
            self.classes.append(c)
            print(f'{c.start_date}:{c.class_name}开班了')
            for stud in self.noclass_students:
                stud.is_enter_class = True
                c.students.append(stud)

            self.noclass_students.clear()

    def get_student(self):
        n = randint(1, 10)
        if n <= 7:
            stu = Student()
            stu.name = '张'+str(time())
            stu.point = n*10
            stu.hard_degree = randint(1, 10)
            stu.smart_degree = randint(1, 10)
            stu.is_enter_class = False
            print(f'学员{stu.name}加入东软睿道学习,等待新班')
            return stu
        else:
            print(f'很遗憾,本次招生未成功')
            return None