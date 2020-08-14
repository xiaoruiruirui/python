import threading

class MyThread(threading.Thread):

    def run(self):
        self.login()
        self.register()
        for i in range(5):
            print('--%d--'%i)

    def login(self):
        print('---登录---')

    def register(self):
        print('--注册--')


if __name__ == '__main__':
    t = MyThread()
    # t.start 只调用类里面的run函数，其余函数不调用，如果想要调用类里面的其他方法，可以在run函数里面调用
    t.start()