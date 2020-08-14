# 数字  字符串  元组  是不可变的   其余都可以改变/数字、字符串、元组要用global
# 在一个函数中对全局变量进行修改时，到底要不要使用global进行说明，要看是否对全局变量的指向进行了修改。如果修改了指向，必须使用global,如果仅仅修改了指向空间的数据，此时不必须用global

import threading
import time


global_num = 10
def test_1():
    global global_num
    global_num += 10
    print('---%d---'%global_num)

def test_2():
    print('---%d---'%global_num)


def main():
    t1 = threading.Thread(target=test_1)
    t2 = threading.Thread(target=test_2)

    t1.start()
    time.sleep(1)

    t2.start()
    time.sleep(1)

    print('in main global_num = %s'%global_num)


if __name__ == '__main__':
    main()