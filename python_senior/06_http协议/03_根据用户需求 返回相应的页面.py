"""此代码运行异常，由于html页面代码编写不完整，其他功能可以用"""


import socket
import re

def server_client(new_client_socket):
    # 6.收到客户端发送来的数据
    # 接收浏览器发送过来的请求，即http协议
    # GET / HTTP/1.1
    request = new_client_socket.recv(1024).decode('utf-8')
    # print(request)
    request_lines = request.splitlines()
    print('')
    print(request_lines)
    # GET是一种请求方式，还有其他的请求方式，POST,PUT,DEL
    # 浏览器发送过来的请求是GET /index.html HTTP/1.1

    # 如果ret不成立，那么没有file_name,下面不能用，所以，先定义一个空字符串
    file_name = ''
    ret = re.match(r'[^/]+(/[^ ]*)',request_lines[0])
    if ret:
        file_name = ret.group(1)
        if file_name == '/':
            file_name = '/index.html'

    # response += 'hahha'
    # 不要轻易打开一个文件，如果必须打开，最好用try
    try:
        f = open('./shangguigu' + file_name,'rb')

    except:
        response = 'HTTP/1.1 404 NOT FOUND\r\n'
        response += '\r\n'
        response += '---file not found---'
        new_client_socket.send(response.encode('utf-8'))

    else:
        html_content = f.read()
        f.close()
        # 7.给客户端回数据
        # 返回http格式的数据，给浏览器
        # header
        response = 'HTTP/1.1 \r\n'
        response += '\r\n'

        # body
        # 将response header发送给浏览器
        new_client_socket.send(response.encode('utf-8'))
        # 将response body发送给浏览器
        new_client_socket.send(html_content)

#     关闭套接字
    new_client_socket.close()

def main():
#     1.创建套接字
    tcp_server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#     设置当前服务器先close 即服务器4次挥手之后资源能够立即释放，这样就保证了，下次运行程序时，仍然可以为客户端服务，而不会显示端口被占用
    tcp_server.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)

# 2.绑定本地信息,默认本地ip，本机ip用127.0.0.1也可以表示
    tcp_server.bind(('',8080))

# # 3.输入对方信息
#     dest_ip = input('请输入目的ip：')
#     dest_port = int(input('请输入目的port:'))

# 4.监听套接字
    tcp_server.listen(128)

    while  True:
    # 5.等待客户端的到来
        new_client_socket,client_addr = tcp_server.accept()

    # 6.为客户端服务
        server_client(new_client_socket)

# 8.关闭套接字
    tcp_server.close()

if __name__ == '__main__':
    main()