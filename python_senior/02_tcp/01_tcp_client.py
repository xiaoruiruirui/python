#tcp和udp的区别
# 1.udp不安全、不稳定  可能会丢失数据
# 2.udp就如写信 不能知道对方有没有获取到  tcp就如打电话 能知道对方有没有收到 所以要提前建立好连接
# 3.udp接收方不会告诉发送方是否收到数据 tcp接收方会告诉发送方是否收到数据

# 1.创建套接字
# 2.连接服务器
# 3.发送数据
# 4.关闭套接字

import socket
def main():
    # 1.创建套接字
    tcp_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    # 2.连接服务器
    server_ip = input('请输入服务器ip')
    server_port = int(input('请输入服务器port'))
    server_addr = (server_ip,server_port)
    tcp_socket.connect(server_addr)

    # 3.发送数据
    send_data = input('请输入要发送的数据')
    tcp_socket.send(send_data.encode('utf-8'))

    # 4.关闭套接字
    tcp_socket.close()

if __name__ == '__main__':
    main()