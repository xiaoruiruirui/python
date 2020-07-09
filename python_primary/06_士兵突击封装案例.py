# 士兵突击封装案例(一个对象的属性可以是另一个类创建的对象)
class Gun:
    def __init__(self,model):
        self.model = model
        self.bullet_count = 0

    def add_bullet(self,count):
        self.bullet_count += count

    def shoot(self):
        # 1.判断子弹数量
        if self.bullet_count <=0:
            print('[%s]没有子弹了...'%self.model)
            return

        # 2.发射子弹 -1
        self.bullet_count -= 1

        # 3.提示发射信息
        print('[%s] 发射子弹[%d]'%(self.model,self.bullet_count))

class Solder:
    def __init__(self,name):
        self.name = name
        self.gun = None

    def fire(self):
# 1.判断士兵是否有枪
        if self.gun is None:
            print('%s 没有枪' % self.name)
            return
# 2.高喊口号
        print('冲啊...[%s]'%self.name)
# 3.让枪装填子弹
        self.gun.add_bullet(10)
# 4.让枪发射子弹
        self.gun.shoot()

# 1.创建枪对象
ak47 = Gun('AK47')
# ak47.add_bullet(3)
# ak47.shoot()
# 2.创建许三多
xusanduo = Solder('许三多')
xusanduo.gun = ak47
print(xusanduo.gun)
xusanduo.fire()