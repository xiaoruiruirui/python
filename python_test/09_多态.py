# 多态  不同的子类对象调用相同的父类方法 产生不同的执行结果
class Dog(object):
    def __init__(self,name):
        self.name = name

    def game(self):
        print('%s蹦蹦跳跳玩'%self.name)

class XiaoTianQuan(Dog):
    def game(self):
        print('%s飞到天上'%self.name)

class Person(object):
    def __init__(self,name):
        self.name = name

    def game_with_dog(self,dog):
        print('%s 和 %s快乐的玩'%(self.name,dog.name))

        # 让狗玩耍
        dog.game()

# 1.创建一个狗对象
# dog = Dog('狗狗')
xiaotianquan = XiaoTianQuan('哮天犬')
# 2.创建一个小明对象
xiaoming = Person('小明')
# 3.让小明和狗玩
xiaoming.game_with_dog(xiaotianquan)