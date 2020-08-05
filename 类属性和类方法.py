"""
实例属性
"""


# 定义一个people类
class People(object):
    def __init__(self):
        # 通过self绑定实例属性
        self.name = "张飞"


peo = People()
# 通过对象绑定实例属性
peo.age = 18
print(dir(peo))

"""
类属性
"""


class Man(object):
    sex = '男'


Man.sex = '女'
man = Man()
print(man.sex)
man.sex = '中'  # 修改时,对象属性不能修改类属性
print(man.sex)

man2 = Man()
print(man2.sex)
print(Man.sex)

"""
类方法
"""


class Women(object):
    @classmethod
    def age(cls):
        print("我是类方法")


# 直接通过类调用方法
Women.age()

# 通过创建实例调用方法
women = Women()
women.age()
