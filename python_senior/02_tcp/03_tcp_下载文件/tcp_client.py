#1. 创建socket套接字
# 2. 连接服务器
# 3. 输入要下载的文件名
# 4.将要下载的文件名发送给服务器
# 5. 接收服务器发送回来的数据,写入一个文件中
# 6.关闭套接字

import socket
def main():
    # 1.创建套接字
    tcp_client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    # 2.连接服务器
    dest_ip = input('请输入服务器ip:')
    dest_port = int(input('请输入服务器端口号:'))
    dest_addr = (dest_ip,dest_port)

    tcp_client_socket.connect(dest_addr)

    # 3.输入要下载的文件名
    download_file_name = input('请输入要下载的文件名:')

    # 4.将要下载的文件名发送给服务器
    tcp_client_socket.send(download_file_name.encode('utf-8'))

    # 5.接收服务器发送回来的数据
    recv_data = tcp_client_socket.recv(1024)

    if recv_data:
        with open('[new]'+download_file_name,'wb') as f:
            f.write(recv_data)

    # 6.关闭套接字
    tcp_client_socket.close()

if __name__ == '__main__':
    main()


