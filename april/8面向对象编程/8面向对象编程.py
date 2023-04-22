import inspect


class Student(object):
    def __init__(self, name, age, sex=None, hobby=None):
        """
        :param name: 学生姓名
        :param age: 学生年龄
        :param sex: 学生性别，默认为 None
        :param hobby: 学生爱好，默认为 None
        """
        self.name = name
        self.age = age
        self.__sex = sex
        self._hobby = hobby

    @property
    def hobby(self):
        """
        获取学生的爱好
        """
        return self._hobby

    @hobby.setter
    def hobby(self, hobby):
        """
        设置学生的爱好
        :param hobby: 学生的爱好
        """
        self._hobby = hobby

    def study(self, course_name):
        """
        学生学习课程
        :param course_name: 课程名称
        """
        print(f'study:{self},course_name:{course_name}')


def student_test():
    student = Student('ssx', 19, '外星人')
    student.study("python")
    student.hobby = "看av"
    print(f'student.hobby:{student.hobby}')

    # 获取对象的所有成员变量和成员函数
    members = inspect.getmembers(student)
    for i in members:
        if not i[0].startswith('__'):
            print(f"data:{i}")


class Person(object):
    def __init__(self, name=None, age=1, person=None):
        # 判断是否已有 person 实例
        if person is not None:
            # 继承 person 的 name 和 _age 属性
            self.name = person.name
            self._age = person.age
        # 若没有 person 实例
        if person is None:
            # 初始化 name 和 _age 属性
            self.name = name
            self._age = age

    @property
    def age(self):
        # 返回 _age 属性值
        return self._age

    @age.setter
    def age(self, age):
        # 设置 _age 属性值
        self._age = age

    def init(self):
        # 返回 self 实例
        return self

    def out(self):
        # 输出 name 和 _age 属性值
        print(f'name:{self.name}')
        print(f'age:{self._age}')


class Ssx(Person):
    def __init__(self, sex, name='ssx', age=2, person=None):
        # 若有 person 实例，继承其 name 和 _age 属性
        if person is not None:
            super().__init__(person=person)
        # 若没有 person 实例，根据提供的 name 和 age 进行初始化
        if person is None:
            super().__init__(name, age)

        # 设置 sex 属性
        self.sex = sex

    def ssx_out(self):
        # 获取 Ssx 实例的所有属性，并输出
        members = inspect.getmembers(self)
        for i in members:
            if not i[0].startswith('__') and not str(i[1]).startswith('<'):
                print(f'{i[0]}:{i[1]}')


def person_test():
    p1 = Person('person', 19)
    p1.out()

    p2 = Person.init(p1)
    p2.age = 18
    print(f'p1 == p2:{p1 == p2}')

    print('--------------------')
    ssx = Ssx('nan', person=p2)
    ssx.out()


if __name__ == '__main__':
    person_test()
