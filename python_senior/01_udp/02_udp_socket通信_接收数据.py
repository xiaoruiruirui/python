#本代码作为服务器接收数据，tcp/udp助手作为客户端发送数据

# 1. 创建套接字
# 2. 绑定自己的ip和端口号
# 3. 接收数据并打印出来
# 4. 关闭套接字

import socket
def main():
    # 1. 创建套接字
    udp_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

    # 2. 绑定自己的ip和端口号
    udp_socket.bind(('',8080))

    # 3. 接收数据并打印出来
    recv_data = udp_socket.recvfrom(1024)
    recv_msg = recv_data[0]
    send_addr = recv_data[1]

    msg = '%s:%s'%(str(send_addr),recv_msg.decode('utf-8'))
    print(msg)

    #4. 关闭套接字
    udp_socket.close()

if __name__ == '__main__':
    main()

