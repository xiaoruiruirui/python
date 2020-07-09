def print_info(name, title='', gender = True):
    # 给函数添加注释：点击函数名，左上角显示小灯泡，选择第二行。
    """

    :param title: 职位
    :param name: 班上同学的姓名
    :param gender:同学的性别True 男生
    """
    gender_text = '男生'

    if not gender:
        gender_text='女生'
    print('[%s]%s 是 %s'%(title,name,gender_text))

# 运行函数快捷键:shift+F10

print_info('小明',title='经理',gender= False)