import socket
# 1.创建套接字
# 2. 循环发送接收
# 3. 关闭套接字

# 发送消息函数
def send_msg(udp_socket):
    dest_ip = input('请输入目的ip')
    dest_port = int(input('请输入目的port'))
    send_data = input('请输入要发送的内容')
    udp_socket.sendto(send_data.encode('utf-8'),(dest_ip,dest_port))

# 接收消息函数
def recv_msg(udp_socket):
    recv_data = udp_socket.recvfrom(1024)
    print(recv_data[0].decode('utf-8'))

def main():
    # 1.创建套接字
    udp_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

    # 2.循环发送接收
    #     为了方便 先绑定自己的ip和端口号
    udp_socket.bind(('',8080))
    while True:
        print('udp聊天室')
        print('1.发送消息')
        print('2.接收消息')
        print('0.退出系统')
        op = input('请输入数字')
        if op == '1':
            send_msg(udp_socket)
        elif op == '2':
            recv_msg(udp_socket)
        elif op == '0':
            break
        else:
            print('输入错误，请重新输入')

    # 3.关闭套接字
    udp_socket.close()

if __name__ == '__main__':
    main()