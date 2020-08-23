def fibonacci(n):
    a = 0
    b = 1
    num = 0
    while num < n:
        # yield没有返回值，f是yield执行完的结论。当send开始启动生成器的时候，send的参数就是yield执行完的结论。fi.send（）的结果是a。
        f = yield a
        print('>>>f>>>', f)

        a,b = b , a+b
        num += 1
    return '---ok---'

fi = fibonacci(10)

f = next(fi)
print(f)

f = fi.send('wi')
print(f)

f = fi.send('wi')
print(f)

f = fi.send('wi')
print(f)