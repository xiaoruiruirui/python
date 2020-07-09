#1. 写入文件
file = open('README','w',encoding='UTF-8')
file.write('12222222')
file.close()

# 2.按行读取文件内容
# readline方法
# 默认可读方式打开
file = open('README',encoding='UTF-8')
while True:
    text = file.readline()
    if not text:
        break
    print(text,end='')
file.close()

# 3. 复制小文件
# 1.打开
file_read = open('README',encoding='UTF-8')
file_write = open('README[副件]','w')

# 2.读写
text = file_read.read()
file_write.write(text)

# 3.关闭文件
file_read.close()
file_write.close()

# 4.复制大文件

file_read = open('README',encoding='UTF-8')
file_write = open('README[副件]','w')

while True:
    text = file_read.readline()
    if not text:
        break
    file_write.write(text)


file_read.close()
file_write.close()


#5. eval()函数  将字符串当成有效的表达式来求值 并返回计算结果
input_str = input('请输入算术题:')
print(eval(input_str))