# 使用字典

# 创建
alien_0 = {'color':'green', 'points':5}

# 访问
print(alien_0['color'])
print(alien_0['points'])

# 打怪
new_points = alien_0['points']
print("You just earned " + str(new_points) + " points！")

print("--------------------------------------")

# 添加键值对
# 添加一个xy坐标
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

print("--------------------------------------")

# 创建一个空字典
alien_0 = {}

alien_0['color'] = 'green'
alien_0['points'] = 5

print(alien_0)

print("--------------------------------------")

# 修改字典的值
# 直接根据键的索引赋值就行了
alien_0 = {'color':'green'}
print("The alien is " + alien_0['color'] + ".")

alien_0['color'] = 'yellow'
print("The alien is now " + alien_0['color'] + ".")

print("--------------------------------------")

# 删除键值对
# del + 对应索引就行了
alien_0 = {'color':'green', 'points':5}
print(alien_0)

del alien_0['points']
print(alien_0)

print("--------------------------------------")

# 由对象构成的字典
# favorite_language.py
favorite_languages = {
        'jen':'python',
        'sarah':'c',
        'edward':'ruby',
        'phil':'python',
    }

print("Sarah's favorite_language is " +
        favorite_languages['sarah'].title()
        + ".")

