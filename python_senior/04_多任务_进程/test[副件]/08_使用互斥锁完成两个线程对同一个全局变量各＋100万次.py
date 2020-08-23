import threading
import time

# 定义一个全局变量
gl_num = 0

def test_1(num):
    global gl_num
    for i in range(num):
        # 上锁
        mutex.acquire()
        gl_num += 1
        # 解锁
        mutex.release()

    print('-----in test1 gl_num = %d-----' %gl_num)

def test2(num):
    global gl_num
    for i in range(num):
        # 上锁
        mutex.acquire()
        gl_num += 1
        # 解锁
        mutex.release()

    print('-----in test2 gl_num = %d-----' % gl_num)



# 定义一个互斥锁，默认是未上锁状态
mutex = threading.Lock()

def main():
    t1 = threading.Thread(target=test_1,args=(1000000,))
    t2 = threading.Thread(target=test2,args=(1000000,))

    t1.start()
    t2.start()

    # 等待上面两个线程执行完毕
    time.sleep(3)
    print('----in main g_nums = %d----' % gl_num)

if __name__ == '__main__':
    main()