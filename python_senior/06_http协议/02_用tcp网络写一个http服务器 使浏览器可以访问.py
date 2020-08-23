import socket

def server_client(new_client_socket):
    # 6.收到客户端发送来的数据
    # GET / HTTP/1.1
    request = new_client_socket.recv(1024).decode('utf-8')
    print(request)

    # 7.给客户端回数据
    # header   body
    # 浏览器区分header和body是根据，header和body中间有一行空格

    response = 'HTTP/1.1 \r\n'
    response += '\r\n'
    response += 'hahha'
    new_client_socket.send(response.encode('utf-8'))

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