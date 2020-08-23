# #第一种方法. 用for 循环得到fibonaci数列
# nums = list()
# a = 0
# b = 1
# i = 0
#
# while i < 10:
#     nums.append(a)
#     a,b = b,a+b
#
#     i +=1
# for num in nums:
#     print(num)

# 使用迭代器生成fibonacci数列创建的方法
import time
class Fibonacci(object):
    def __init__(self,all_num):
        self.all_num = all_num
        self.a = 0
        self.b = 1
        self.i = 0
    def __iter__(self):
        return self

    def __next__(self):
        while self.i < self.all_num:
            ret = self.a
            self.a,self.b = self.b,self.a+self.b
            self.i += 1
            return ret
        else:
            raise StopIteration

fibo = Fibonacci(10)

for num in fibo:
    print(num)
    time.sleep(1)