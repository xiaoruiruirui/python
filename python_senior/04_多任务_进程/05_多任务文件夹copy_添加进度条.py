import multiprocessing
import os


def work_copy(queue,file_name,old_folder_file,new_folder_file):
    old = open(old_folder_file + '/' +file_name,'rb')
    old_file = old.read()
    old.close()

    new = open(new_folder_file + '/' +file_name,'wb')
    new_file = new.write(old_file)
    new.close()

    #     如果拷贝完了文件,那么就像队列添加完成信息
    queue.put(file_name)


def main():
#     获取要copy的文件夹名字
    old_folder_file = input('请输入想要copy的文件夹名字')

#     新建一个新的文件夹
    try:
        new_folder_file = old_folder_file + '[副件]'
        os.mkdir(new_folder_file)
    except:
        pass

#   获取文件夹中的文件名字
    file_names = os.listdir(old_folder_file)

#   创建进程池
    po = multiprocessing.Pool(5)

#   创建一个队列
    queue = multiprocessing.Manager().Queue()

#   将copy任务放入进程池
    for file_name in file_names:
        po.apply_async(work_copy,(queue,file_name,old_folder_file,new_folder_file))

    po.close()

    all_file = len(file_names)
    num = 0
    while True:
        file_name = queue.get()
        num += 1
        print('\r拷贝进度为%.2f%%'%(num * 100 / all_file),end=' ')

        if all_file == num:
            break

if __name__ == '__main__':
    main()