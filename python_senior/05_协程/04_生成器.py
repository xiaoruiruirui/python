# 生成器是特殊的迭代器
# 创建生成器方法1.
# 将[]改为()，就将列表变为了生成器。列表和生成器都能for循环。区别在于：列表循环是事先将列表数据存储起来，占用空间，而生成器是一种生成列表数据的方式，占用空间小。

# li = (i * 2 for i in range(10))
# print(li)
#
# for num in li:
#     print(num)


# # 创建生成器方法2.
# 写函数，将函数中的return 改为yield
# 例如：fibonacci函数
def fibonacci(n):
    a = 0
    b = 1
    num = 0
    while num < n:
        # 如果一个函数有yield语句，那么这就不再是一个函数，而是一个生成器的模板,可以理解成与类同级
        yield a
        a,b = b , a+b
        num += 1
    return '---ok---'
# 如果在调用fibonacci时，其中有yield,那么不是在调用函数，而是在创建生成器对象
# 可以生成多个生成器，相互之间没有交叉。

obj = fibonacci(10)
obj2 = fibonacci(8)

ob = next(obj)
print(ob)

ob = next(obj)
print(ob)

input()
ob2 = next(obj2)
print(ob2)

ob2 = next(obj2)
print(ob2)

ob = next(obj)
print(ob)


# 如果参数值小，在多次使用next方法后，会没有数值可取 就会报错，所以用try方法捕获异常
ob = fibonacci(50)

while True:
    try:
        d = next(ob)
        print(d)
    except Exception as r:
        print(r.value)
        break
