"""
闭包的定义:
    1.内部函数定义在外部函数内部
    2.内部函数有使用外部函数的局部变量
    3.内部函数作为外部函数的返回值
"""


# 定义一个外部函数
def father():
    name = '我是外部函数'

    # 定义一个内部函数
    def son(var):
        print('{}传递{}给内部函数'.format(name, var))

    return son


res = father()
res('变量')

"""
闭包可以替代简单的类,可以减少内存的开销
"""


# 原版
class Animal(object):
    def __init__(self, name):
        self.name = name

    def say(self, voice):
        print('{}的叫声是{}'.format(self.name, voice))


dog = Animal('狗')
dog.say('汪')


# 闭包改良后
def ani(name):
    def voi(vo):
        print('{}的叫声是{}'.format(name, vo))

    return voi


cat = ani("猫")
cat('喵')
