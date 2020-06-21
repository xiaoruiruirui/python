# # 继承
# class Animal:
#
#     def eat(self):
#         print('吃')
#     def drink(self):
#         print('喝')
#     def run(self):
#         print('跑')
#     def sleep(self):
#         print('睡-')
#
# class Dog(Animal):
#     # 子类拥有父类的所有属性和方法
#     def bark(self):
#         print('汪汪叫')
#
# # 子类的子类
# class XiaoTianQuan(Dog):
#     def fly(self):
#         print('我会飞')
#     def bark(self):
# #         1.针对子类特有的需求，编写代码
#         print('叫的像神一样')
# # 2.使用super().调用原本在父类中封装的方法
#         super().bark()
# #         3.增加其他子类的方法
#         print('$$%%')
# # class Cat(Animal):
# #     def catch(self):
# #         print('抓老鼠')
# # 创建一个对象 狗对象
# wangcai = XiaoTianQuan()
# wangcai.eat()
# wangcai.drink()
# wangcai.run()
# wangcai.sleep()
# # 如果子类中重写了父类的方法，在使用子类对象调用方法时，会调用子类中重写的方法
# wangcai.bark()
# wangcai.fly()






# # 子类对象不能在自己的方法内部 直接访问父类的私有属性或私有方法，子类对象可以通过父类的公有方法间接访问到私有属性或私有方法
# class A:
#     def __init__(self):
#         self.num1 = 100
#         self.__num2 = 200
#
#     def __test(self):
#         print('私有方法%d %d'%(self.num1,self.__num2))
#
#     def test(self):
#         print('父类的公有方法%d %d' % (self.num1, self.__num2))
#         self.__test()
#
# class B(A):
#     def demo(self):
#         print('访问父类的公有属性 %d'%self.num1)
#         self.test()
#
#
# b = B()
# print(b)
# # print(b.__test)
# b.demo()






# 多继承
# 子类可以拥有多个父亲,并且具有所有父亲的属性和方法
class A:
    # 父类内方法不要重复
    def test(self):
        print('testa方法')

    def demo(self):
        print('demoa方法')

class B:
    def test(self):
        print('testb方法')
    def demo(self):
        print('demob方法')

class C(B,A):
    # 多继承可以让子类对象同时具有多个父类的属性和方法
    print('c类方法')

c = C()
c.test()
c.demo()
# 确定C类对象调用方法的顺序
print(C.mro())

class A():
    pass

a = A()
# dir()可以查看对象的内置的属性和方法
print(dir(a))