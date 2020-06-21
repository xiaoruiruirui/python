# 私有属性
class Women:

    def __init__(self,name):
        self.name = name
        self.__age = 18

    def __secret(self):
        # 在对象的方法内部是可以访问对象的私有属性的
        print('%s的年龄是%d'%(self.name,self.__age))

xiaofang = Women('小芳')
# 私有属性，在外界不能够直接被访问
# 改造后可以访问，使用_class名
print(xiaofang._Women__age)
# 私有方法同样不允许在外界直接访问
xiaofang._Women__secret()