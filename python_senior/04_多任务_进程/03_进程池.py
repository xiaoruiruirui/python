from multiprocessing import Pool
import time,os,random

def work(msg):
    start_time = time.time()
    print('%d开始执行，进程号为%d'%(msg,os.getpid()))
    time.sleep(random.random()*2)
    stop_time = time.time()
    print('%d执行完毕，耗时%.2f'%(msg,stop_time - start_time))


def main():
    # 定义一个进程池，最大进程数为3
    po = Pool(3)
    for i in range(10):
        po.apply_async(work,(i,))

    print('---start---')
#     关闭进程池，关闭后，po不再接收其他请求
    po.close()

#     等待po中所有子进程执行完成，必须放在close后
    po.join()
    print('---end---')


if __name__ == '__main__':
    main()