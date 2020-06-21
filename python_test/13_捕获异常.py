# 捕获异常  try() except()
try:
    # 不能确定正确执行的代码
    # input函数输入的是字符串，浮点数类型的字符串是不能用int转换为整型的，只有整数类型的字符串才能用int转换为整型。
    num = int(input('请输入整数：'))

except:
    # 错误的代码处理
    print('请输入正确的整数')

print('-'*50)

# 多种错误类型捕获

try:
    # 提示用户输入一个整数
    num = int(input('输入一个整数：'))
    # 使用8除以用户输入的整数并且输出
    # 真实值
    # print(a/b)
    # 地板除法
    # print(a//b)
    # 取余
    # print(a%b)

    result = 8 / num
    print(result)
except ZeroDivisionError:
    print('除0错误')
except ValueError:
    print('请输入正确的整数')

# 捕获未知错误
try:
    # 提示用户输入一个整数
    num = int(input('输入一个整数：'))
    # 使用8除以用户输入的整数并且输出
    result = 8 / num
    print(result)
except ValueError:
    print('请输入正确的整数')

# 假如没有预判到输入分母为0 的错误
except Exception as result:
    # result是在except下定义的变量 不一定非用result   Exception是一个异常的类
    print('未知错误%s'%result)

# 异常捕获的完整语法

try:
    # 提示用户输入一个整数
    num = int(input('输入一个整数：'))
    # 使用8除以用户输入的整数并且输出
    result = 8 / num

    print(result)
except ValueError:
    print('请输入正确的整数')

# 假如没有预判到输入分母为0 的错误
except Exception as result:
    # result是在except下定义的变量 不一定非用result   Exception是一个异常的类
    print('未知错误%s'%result)

else:
    print('尝试成功')
finally:
    print('无论是否出现错误都会执行的代码')

print('-'*50)

# 异常的传递:当函数/方法执行出现异常，会将异常传递给函数/方法的调用一方。如果传递到主程序   仍然没有异常处理 程序才会被终止

def demo1():
    return int(input('输入整数：'))

def demo2():
    return demo1()

# 利用异常的传递性，在主程序捕获异常
try:
    print(demo2())
except Exception as result:
    print('未知错误 %s'%result)

# 抛出raise异常

def input_password():

#     1.提示用户输入密码
    pwd = input('请输入密码：')
# 2.判断密码长度 >= 8,返回用户输入的密码
    if len(pwd) >= 8:
        return pwd
# 3.如果密码<8 主动抛出异常
    print('主动抛出异常')
#     1.创建异常对象--可以使用错误信息字符串作为参数
    ex = Exception('密码长度不够')
# 2.主动抛出异常
    raise ex

# 提示用户输入密码
try:
    print(input_password())
except Exception as result:
    print(result)