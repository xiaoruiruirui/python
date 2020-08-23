import multiprocessing
import time

def test_1():
    while True:
        print('---1---')
        time.sleep(1)

def test_2():
    while True:
        print('---2---')
        time.sleep(1)

def main():

    p1 = multiprocessing.Process(target=test_1)
    p2 = multiprocessing.Process(target=test_2)

    p1.start()
    p2.start()


if __name__ == '__main__':
    main()