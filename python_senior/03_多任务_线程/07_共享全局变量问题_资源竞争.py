import threading
import time

global_num = 0

def test_1(num):
    global global_num
    for i in range(num):
        global_num += 1
    print('---in test_1 global_num = %d'%global_num)

def test_2(num):
    global global_num
    for i in range(num):
        global_num += 1
    print('---in test_2 global_num = %d'%global_num)

def main():

    t1 = threading.Thread(target=test_1,args=(1000000,))
    t2 = threading.Thread(target=test_2,args=(1000000,))

    t1.start()
    t2.start()

    time.sleep(1)
    print('---in main global_num = %s'%global_num)


if __name__ == '__main__':
    main()