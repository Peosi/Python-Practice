"""
继承的语法:
    子类会自动继承父类的方法与属性
    子类的实例可以直接使用父类的方法
    子类也可以添加自己的新的方法
    私有属性不会被子类继承
"""


class People(object):  # 这是父类
    def say(self):
        print("我是父类")


class Man(People):  # 子类,继承父类的say方法
    def speak(self):
        print("我是子类男人")


class Women(People):  # 子类,重写父类的方法
    def say(self):
        print("我是子类女人")


man = Man()
man.speak()
man.say()
woman = Women()
woman.say()

"""
单继承:只是继承了父类的方法与属性

多层继承: 多个父类也呈现从属关系

当出现多个父类继承如:
语法: class 类名(父类1,父类2,..):

通过 类名.__mro__  可以查看各个类的优先级,前面的优先
"""


class Animal(object):
    def eat(self):
        print('进食')


class People(Animal):
    def say(self):
        print('我是父类')

    def run(self):
        print('父类运动')


class Student(People):
    def study(self):
        print('我是子类学习')

    def play(self):
        print('我是学生子类玩')


class Teacher(People):
    def teach(self):
        print('我是子类老师')

    def play(self):
        print('我是老师子类玩')


class Tutor(Teacher, Student):
    def homework(self):
        print('帮你做作业')


stu = Student()
tu = Tutor()
print(Tutor.__mro__)
tu.play()

