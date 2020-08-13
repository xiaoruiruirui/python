# 1. 创建tcp套接字(买一个新手机)
# 2. 绑定自己信息(插入手机卡)
# 3. 将tcp服务器变为监听状态,让默认的套接字由主动变为被动(listen) 因为自己创建的套接字默认是链接别人,要想让别人链接自己就需要设置第3步,变为被动模式(为手机设置铃声)
# 4. 当客户端到来时为客户端服务,等待客户端的链接 accept,.accept有两个返回值,第一个是accept新产生的为客户端服务的套接字,第二个是当前客户端的地址
# 5. 关闭套接字

import socket
def main():
    # 1.创建套接字
    tcp_server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    # 2.绑定自己信息
    tcp_server_socket.bind(('',8080))

    # 3.将tcp服务器变为监听状态
    tcp_server_socket.listen(128)

    #循环为多个客户服务
    while True:
        print('等待第一个客户的到来:')

        # 监听套接字负责有新的客户端进行链接,accept产生的新的套接字用来为客户端服务
        new_client_socket,client_addr = tcp_server_socket.accept()
        print('新的客户端%s已经到来'%str(client_addr))

#         循环为一个客户端服务多次
        while True:
            # 接收客户端发来的数据
            recv_data = new_client_socket.recv(1024)
            print('客户端发来的数据%s'%(recv_data.decode('utf-8')))
            # 如果recv解堵塞,那么有两种方式:1.客户端发送过来数据  2.客户端调用了close
            if recv_data:
                new_client_socket.send('----ok----'.encode('utf-8'))
            else:
                break

        new_client_socket.close()
        print('已经服务完毕')

    tcp_server_socket.close()

if __name__ == '__main__':
    main()

