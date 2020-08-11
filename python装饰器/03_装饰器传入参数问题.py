def factory(old):
    def new(*args, **kwargs):
        print('这里装修')
        return old(*args, **kwargs)

    return new


@factory
def show(name):
    print(name)


show('杜甫')


@factory
def show1(name, age):
    print(name, age)


show1('李白', 18)
