import socket
import threading

def recv_msg(udp_socket):
    # 4.接收数据
    while True:
        recv_data = udp_socket.recvfrom(1024)
        print(recv_data)

def send_msg(udp_socket,dest_ip, dest_port):
    # 5.发送数据
    while True:
        send_data = input('请输入要发送的数据：')
        udp_socket.sendto(send_data.encode('utf-8'),(dest_ip, dest_port))

def main():

#     1.创建套接字
    udp_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

# 2.绑定本地信息
    udp_socket.bind(('192.168.43.105',8080))

# 3.输入对方信息
    dest_ip = input('请输入ip:')
    dest_port = int(input('请输入port:'))

    t_recv = threading.Thread(target=recv_msg,args=(udp_socket,))
    t_send = threading.Thread(target=send_msg,args=(udp_socket,dest_ip, dest_port))

    t_recv.start()
    t_send.start()

# 不能关闭套接字



if __name__ == '__main__':
    main()