import multiprocessing
import os

def copy(file_name,old_folder_file,new_folder_file):
    """
    完成复制功能
    """
    old = open(old_folder_file + '/' +file_name,'rb')
    old_file = old.read()
    old.close()

    new = open(new_folder_file +'/' +file_name,'wb')
    new.write(old_file)
    new.close()

def main():
#     获取想要copy的文件夹名字
    old_folder_file = input('请输入想要copy的文件夹名字')

# 新建一个新的文件夹
    try:
        new_folder_file = old_folder_file + '[新]'
        os.mkdir(new_folder_file)
    except:
        pass

# 获取想要copy的文件夹的文件名字
    file_names = os.listdir(old_folder_file)

# 创建进程池
    po = multiprocessing.Pool(5)

    # 向进程池中添加copy的任务
    for file_name in file_names:
        po.apply_async(copy,(file_name,old_folder_file,new_folder_file))

    po.close()
    po.join()

if __name__ == '__main__':
    main()