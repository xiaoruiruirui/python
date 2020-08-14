#列表不用加global  也可以代表全局变量，因为指向没有变

import threading
import time


def test_1(temp):
    temp.append(33)
    print('---%s---'%temp)

def test_2(temp):
    print('---%s---'%temp)


global_list = [11,22]

def main():
    t1 = threading.Thread(target=test_1,args=(global_list,))
    t2 = threading.Thread(target=test_2,args=(global_list,))

    t1.start()
    time.sleep(1)

    t2.start()
    time.sleep(1)

    print('in main global_list = %s'%global_list)

if __name__ == '__main__':
    main()