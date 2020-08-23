import threading
import time

def test_1():
    for i in range(5):
        print('-------%d------'%i)
        time.sleep(1)
#     如果创建Thread时执行的函数，运行结束  意味着这个子线程结束了

def test_2():
    for i in range(10):
        print('---------%d----'%i)
        time.sleep(1)

def main():
    t1 = threading.Thread(target=test_1)
    t2 = threading.Thread(target=test_2)

    t1.start()
    t2.start()

    while True:
        print(threading.enumerate())
        if len(threading.enumerate())<=1:
            break
        time.sleep(1)

if __name__ == '__main__':
    main()