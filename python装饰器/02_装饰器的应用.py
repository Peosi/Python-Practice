def parma_int(old):
    def new(num1, num2):
        if not (isinstance(num1, int) and isinstance(num2, int)):
            print('参数必须为整数')
        else:
            return old(num1, num2)  # 注意,原函数的执行结果,我们必须返回

    return new


@parma_int
def my_sum(num1, num2):
    return num1 + num2


@parma_int
def my_mul(num1, num2):
    return num1 * num2


print(my_sum(1, '李白'))
print(my_mul(3, 5))
