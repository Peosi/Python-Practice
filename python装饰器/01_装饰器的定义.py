# def factory(func):
#     def inner():
#         print('###################')  # 装饰的新功能
#         return func()  # 调用原函数,实现原函数的功能
#
#     return inner
#
#
# def show():
#     print('我是show')
#
#
# show = factory(show)
# show()


def factory(func):
    def inner():
        print('###################')  # 装饰的新功能
        return func()  # 调用原函数,实现原函数的功能

    return inner


@factory
def show():
    print('我是show')


show()
