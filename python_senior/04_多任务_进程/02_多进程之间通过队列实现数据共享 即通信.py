import multiprocessing


def download_data(q):
    list1 = [11,22,33,44]
    for temp in list1:
        q.put(temp)
    print('下载完毕')

def analiy_data(q):
    list2 = []
    while True:
        list2.append(q.get())
        if q.empty():
            break
    print(list2)

def main():
#     创建一个队列，用于数据的放入和取出
    q = multiprocessing.Queue()

# 创建进程
    p1 = multiprocessing.Process(target=download_data,args=(q,))
    p2 = multiprocessing.Process(target=analiy_data,args=(q,))

    p1.start()
    p2.start()


if __name__ == '__main__':
    main()