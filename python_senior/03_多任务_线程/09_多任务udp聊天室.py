import threading
import socket


def recv_msg(udp_socket):
    while True:
        recv_data = udp_socket.recvfrom(1024)
        print(recv_data)

def send_msg(udp_socket,dest_ip,dest_port):
    while True:
        send_data = input('请输入要发送的信息')
        udp_socket.sendto(send_data.encode('utf-8'),(dest_ip,dest_port))


def main():

    # 创建socket
    udp_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

    # 绑定自己信息
    udp_socket.bind(('',8080))

    # 输入对方的信息
    dest_ip = input('请输入目的ip')
    dest_port = int(input('请输入目的port'))

    t_recv = threading.Thread(target=recv_msg,args=(udp_socket,))
    t_send = threading.Thread(target=send_msg,args=(udp_socket,dest_ip,dest_port))

    t_recv.start()
    t_send.start()

if __name__ == '__main__':
    main()