 # 面向对象是更大的封装，在一个类class中封装多个方法，通过这个类创建出来的对象，就可以调用这些方法了
class Cat(object):
    def eat(self):
        # 哪一个对象调用的方法，self就是哪一个对象的引用
        print('%s 爱吃鱼' % self.name)
    def drink(self):
        print('%s 要喝水' % self.name)

# 创建猫对象
tom = Cat()
tom.name = 'Tom'
tom.eat()
tom.drink()
tom.name = 'Tom'
print(tom)
# 再创建一个猫对象
lazy_cat = Cat()
lazy_cat.name = '大懒猫'
lazy_cat.eat()
lazy_cat.drink()
print(lazy_cat)


# 类的属性的初始化
class Cat:
    def __init__(self):
        print('这是一个初始化方法')
# 使用类名（）创建对象的时候，会自动调用初始化方法__init__
tom = Cat()


# 在初始化方法内部定义属性
class Cat:
    def __init__(self):
        print('这是一个初始化方法')
#       self.属性名 = 属性的初始值
        self.name = 'Tom'
    def eat(self):
        print('%s 爱吃鱼'%self.name)
# 使用类名（）创建对象的时候，会自动调用初始化方法__init__
tom = Cat()
print(tom.name)

lazy_cat = Cat()
lazy_cat.eat()


# # 改造类
class Cat:
    def __init__(self,new_name):
        print('这是一个初始化方法')
#       self.属性名 = 属性的初始值
        self.name = new_name

    def eat(self):
        print('%s 爱吃鱼'%self.name)
# 使用类名（）创建对象的时候，会自动调用初始化方法__init__
tom = Cat('Tom')
print(tom.name)
lazy_cat = Cat('大懒猫')
lazy_cat.eat()





# 使用__del__方法,结束对象的生命周期
class Cat:
    def __init__(self,new_name):
        self.name = new_name
        print('%s 来了'% self.name)
    def __del__(self):
        print('%s我去了'%self.name)

tom = Cat('Tom')
print(tom.name)
# del关键字可以删除一个对象
del tom
#
print('-'*30)

# 使用__str__方法，必须有返回值,输出想要的字符串
class Cat:
    def __init__(self,new_name):
        self.name = new_name
        print('%s 来了'% self.name)
    def __del__(self):
        print('%s我去了'%self.name)
    def __str__(self):
#         必须返回一个字符串
        return '我是小猫[%s]'%self.name
tom = Cat('Tom')
print(tom)
