# 为什么要用迭代器：for循环列表，是首先将列表的值都存储好之后再一个一个读出来，占用存储空间。而迭代器是一种生成列表数据的方法，占用空间极少。
from collections import Iterable
from collections import Iterator
import time
class Classmate(object):
    def __init__(self):
        self.names = list()

    def add(self,name):
        self.names.append(name)

    def __iter__(self):
        # 如果想让一个对象成为一个可以迭代的对象，即可以使用for，那么必须实现__iter__方法
        return ClassIterator(self)

class ClassIterator(object):
    def __init__(self,obj):
        self.obj = obj
        self.num = 0

    def __iter__(self):
        pass

    def __next__(self):
        if self.num < len(self.obj.names):
            ret = self.obj.names[self.num]
            self.num += 1
            return ret
        else:
            raise StopIteration

xiaoming = Classmate()
xiaoming.add('小明')
xiaoming.add('小李')

# xiaoming_iterator = iter(xiaoming)
# print(isinstance(xiaoming,Iterable))
# print(isinstance(xiaoming_iterator,Iterator))
# print(next(xiaoming_iterator))

for i in xiaoming:
    print(i)
    time.sleep(1)
