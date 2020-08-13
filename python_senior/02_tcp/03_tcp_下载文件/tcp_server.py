# 1.创建套接字
# 2.绑定自己信息
# 3.状态变为监听状态
# 4.等待客户端的连接
# 5.为客户端服务
# 6.关闭套接字

import socket

def send_file_to_client(new_client_socket,client_addr):
    # 收到客户端发送来的要下载的文件的名字
    file_name = new_client_socket.recv(1024).decode('utf-8')
    print('客户端%s要下载的文件名是%s'%(str(client_addr),file_name))

    file_content = None

    try:
        f = open(file_name,'rb')
        file_content = f.read()
        f.close()
    except Exception as ret:
        print('没有要下载的文件%s'%file_name)

    if file_content:
        new_client_socket.send(file_content)


def main():
    # 1.创建套接字
    tcp_server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    # 2.绑定自己信息
    tcp_server_socket.bind(('',7000))

    # 3.状态变为监听状态
    tcp_server_socket.listen(128)

    # 4.等待客户端的连接
    while True:
        new_client_socket,client_addr = tcp_server_socket.accept()

        # 5.为客户端服务
        send_file_to_client(new_client_socket,client_addr)

        new_client_socket.close()
    # 6.关闭套接字
    tcp_server_socket.close()

if __name__ == '__main__':
    main()