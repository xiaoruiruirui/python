# 单核cpu执行多任务是时间片轮转，即假的多任务，也叫并发。多核cpu，cpu数量可以满足程序数量要求，执行多任务，叫并行。

import time
import threading

def sing():
    for i in range(5):
        print('---正在唱：一个人---')
        time.sleep(1)


def dance():
    for i in range(5):
        print('---正在跳舞---')
        time.sleep(1)


def main():
    t1 = threading.Thread(target=sing)
    t2 = threading.Thread(target=dance)
    t1.start()
    t2.start()

if __name__ == '__main__':
    main()