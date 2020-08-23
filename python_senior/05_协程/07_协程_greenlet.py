from greenlet import greenlet
import time

def test_1():
    while True:
        print('---1---')
        t2.switch()
        time.sleep(1)

def test_2():
    while True:
        print('---2---')
        t1.switch()
        time.sleep(1)

t1 = greenlet(test_1)
t2 = greenlet(test_2)

# 切换到t1中运行
t1.switch()
