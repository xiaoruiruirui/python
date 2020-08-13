#1. 创建套接字
#2. 发送数据
#3. 接收数据
#4. 关闭套接字

import socket

def main():

# 1. 创建套接字
    udp_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

# 2. 发送数据
    dest_ip = input('请输入ip')
    dest_port = int(input('请输入port'))
    send_data = input('请输入要发送的内容')
    udp_socket.sendto(send_data.encode('utf-8'),(dest_ip,dest_port))

# 3.接收数据
    recv_data = udp_socket.recvfrom(1024)
    print(recv_data[0].decode('utf-8'))

# 4.关闭套接字
    udp_socket.close()

if __name__ == '__main__':
    main()
