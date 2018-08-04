# 喜欢的地方
# 字典里面嵌套列表吧
# 列表里面存放人们喜欢的地方（不止一个）

favorite_places = {'osy':['shenzhen', 'qinzhou', 'hongkong'], 'oshany':
        ['guangxi', 'beijing'], 'ooo':['american']}

for key, value in favorite_places.items():
    print("------")
    print(key + "'s favorite_places is ")
    for var in value:
        print(var)

# 我这里增加了一个循环来遍历列表
# 但是换行了看起来不够好
# 虽然似乎也整洁点
