# 修改，删除，增加元素于列表中



# 修改 下表元素直接赋值
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles[0] = 'ducati'
print(motorcycles)

print("------------------------------------------------")

# 添加元素 append 末尾添加
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles.append('ducati')
print(motorcycles)

print("------------------------------------------------")

# 插入元素 insert()方法
motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles.insert(0, 'ducati')
print(motorcycles)

print("------------------------------------------------")

# 删除元素 del 给出删除的对应列表的元素以及下标即可
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

del motorcycles[0]
print(motorcycles)

print("------------------------------------------------")

# 删除元素 pop() 方法 删除最后一个
# pop()方法带返回值，返回值为pop()出来的元素
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

poped_motorcycle = motorcycles.pop()
print(motorcycles)
print(poped_motorcycle)

print("------------------------------------------------")

# 删除元素 pop()方法， 删除任意一个元素
motorcycles = ['honda', 'yamaha', 'suzuki']
first_owned = motorcycles.pop(0)
print('The first motorcycles I owned was a ' + first_owned.title() + '.')


print("------------------------------------------------")

# 删除元素 remove方法，删除规定的某个值
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)

motorcycles.remove('ducati')
print(motorcycles)


