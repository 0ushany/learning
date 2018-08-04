# 宠物
doge = {'name':'doge', 'owner':'osy'}
cata = {'name':'cata', 'owner':'oshany'}

pets = [doge, cata]
for pet in pets:
    print(pet['name'] + "'s owner is " + pet['owner'])

# 遍历的方法就是这样
# 遍历宠物字典，然后通过字典的键调用对应的元素即可
