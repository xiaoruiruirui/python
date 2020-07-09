# 方法综合
class Game(object):
    # 类属性 历史最高分
    top_score = 0

    # 类方法
    @classmethod
    def show_top_score(cls):
        print('历史最高分:%d'%cls.top_score)

    # 实例属性player_name
    def __init__(self,player_name):
        self.player_name = player_name

    # 静态方法
    @staticmethod
    def show_help():
        print('游戏帮助信息是:让僵尸进入大门')

    #实例方法
    def start_game(self):
        print('%s开始当前的游戏'%self.player_name)

Game.show_help()
Game.show_top_score()
xiaoli = Game('小李')
xiaoli.start_game()