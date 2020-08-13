# 代码作为客户端发送数据，tcp/udp助手作为服务器接收数据
# 1.创建udp套接字 2.发送数据 3.关闭套接字

import socket
def main():
    # 1.创建套接字
    udp_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

    # 2.使用socket发送数据()对方的ip和端口
    udp_socket.sendto(b'1209838947930',('192.168.0.105',8080))

    # 关闭socket
    udp_socket.close()

if __name__ == '__main__':
    main()