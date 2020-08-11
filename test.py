def getLi():
    li = []
    for i in range(1, 4):
        def inner(j=i):
            print(i)
            return j**2
        li.append(inner)
    return li


f1, f2, f3 = getLi()
print(f1(), f2(), f3())
print(f1.__closure__) 