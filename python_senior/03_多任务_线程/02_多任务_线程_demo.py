#单核cpu执行多任务,是时间片轮转,假的多任务,并发
#多核cpu执行多任务,cpu数量可以满足程序数量,叫并行

import threading
import time

def sing():
    for i in range(5):
        print('---在唱歌---')
        time.sleep(1)

def dance():
    for i in range(5):
        print('---在跳舞---')
        time.sleep(1)


def main():

    t1 = threading.Thread(target=sing)
    t2 = threading.Thread(target=dance)
    t1.start()
    t2.start()


if __name__ == '__main__':
    main()