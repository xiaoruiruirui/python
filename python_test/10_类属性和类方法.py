# 类属性和类方法
class Tool(object):
    # 使用赋值语句定义类属性 记录所有工具对象的数量
    # 类属性
    count = 0
    # 类方法
    @classmethod
    def show_tool_count(cls):
        print('工具对象的数量%d'%cls.count)

    def __init__(self,name):
        self.name = name
#         让类属性的值加一
        Tool.count += 1

# 1.创建工具对象
tool1 = Tool('斧头')
tool2 = Tool('榔头')
tool3 = Tool('水桶')

# 2.输出工具对象的总数
# 使用类名.类属性的方式获取类属性值
print(Tool.count)
# 使用对象名.类属性获取类属性值。用该方法程序会先在对象属性中查找该属性 如果么有找到就往上一层的类属性中寻找
print('工具对象总数 %d'%tool1.count)

# 调用类方法
Tool.show_tool_count()