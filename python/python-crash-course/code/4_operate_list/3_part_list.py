# 使用列表的一部分
# 切片
# players.py
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])
# 输出了0-2下标的元素，也就是一部分（不包括3）


# 不指定第一个的索引
print(players[:4])
# 他就会从头开始一直到4,不包括4

# 不指定第二个索引
print(players[2:])
# 它就会从第3个开始到结尾

# 负数索引返回距离末尾相应距离的元素
print(players[-3:])
# 返回了最后3个元素


print("---------------------------------")

# 遍历切片
# 也就是遍历一部分

for player in players[:3]:
    print(player)


print("---------------------------------")

# 复制列表
# foods.py
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

print("My favorite foods are:")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friend_foods)
# 通过切片完成了列表的复制
# 创建了一个新的副本，创建了一个新的内存空间来存放列表，可行


print("---------------------------------")

# 不使用切片直接赋值是行不通的

friend_foods = my_foods
my_foods.append('cannoli')
friend_foods.append('ice cream')

print("My favorite foods are:")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friend_foods)
# 这种情况是把两个变量都指向了同一个列表上（在内存里）
