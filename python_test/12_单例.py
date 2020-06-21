# 单例:让类创建的对象，在系统中只有唯一的一个实例
# __new__是一个由 object基类提供的内置的静态方法

class MusicPlayer(object):

    def __new__(cls, *args, **kwargs):
    #1.创建对象时，new方法会被自动调用
        print('创建方法，分配空间')

    #     2.为对象分配空间
        instance = super().__new__(cls)
    # 3.返回对象的引用
        return instance

    def __init__(self):
        print('播放器初始化')

# 创建播放器对象
player = MusicPlayer()
print(player)

# 单例设计模式:每次都会得到第一次被创建对象的引用（内存地址）
class MusicPlayer(object):
    # 记录第一个被创建对象的引用
    instance = None
    def __new__(cls, *args, **kwargs):
        # 1.判断类属性是否为空对象
        if cls.instance is None:
        # 2.调用父类的方法，为第一个对象分配空间
            cls.instance = super().__new__(cls)
        # 3.返回类属性保存的对象引用
        return cls.instance

player1 = MusicPlayer()
print(player1)

player2 = MusicPlayer()
print(player2)

# 单例初始化一次
class MusicPlayer(object):
    # 记录第一个被创建对象的引用
    instance = None
    # 记录是否执行过初始化动作
    init_flag = False

    def __new__(cls, *args, **kwargs):
        # 1.判断类属性是否为空对象
        if cls.instance is None:
        # 2.调用父类的方法，为第一个对象分配空间
            cls.instance = super().__new__(cls)
        # 3.返回类属性保存的对象引用
        return cls.instance

    def __init__(self):
        # 1.判断是否执行过初始化方法
        if MusicPlayer.init_flag:
            return
        # 2.如果没有执行过，再执行初始化动作
        print('初始化播放器')

        # 3.修改类属性的标记
        MusicPlayer.init_flag = True

player1 = MusicPlayer()
print(player1)

player2 = MusicPlayer()
print(player2)
