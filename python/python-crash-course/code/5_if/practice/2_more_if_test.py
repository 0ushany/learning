# 更多的条件测试
# 检查两个字符串相等和不等
car1 = 'bmw'
car2 = 'audi'
if car1 != car2:
    print(car1 + " is not " + car2)
if car1 == 'bmw':
    print(car1 + " is 'bmw'")

print("------------------------------------")

# 使用函数lower()测试
man1 = 'David'
if man1.lower() != 'David':
    print(man1.lower() + " is not David?")
if man1.lower() == 'david':
    print(man1.lower() + " is david")

print("------------------------------------")

# 检查两个数字相等、不等、大于、小于、大于等于和小于等于
if 2 == 2:
    print("2 = 2")
if 2 != 1:
    print("2 != 1")
if 2 > 1:
    print("2 > 1")
if 2 < 3:
    print("2 < 3")
if 2 >= 1:
    print("2 >= 1")
if 2 <= 3:
    print("2 <= 3")

print("------------------------------------")

# 使用关键字and和or测试
print("Is 2 > 1 and 2 < 1?")
print(2 > 1 and 2 < 1)
print("Is 2 > 1 or 2 < 1?")
print(2 > 1 or 2 < 1)

print("------------------------------------")

# 测试特定的值是否包含在列表中
cars = ['bmw', 'audi', 'toyota']
if 'bmw' in cars:
    print(cars[0].title() + " is here")

# 测试特定的值是否未包含在列表中
print("Is AAA not here?")
if 'aaa' not in cars:
    print('AAA' not in cars)
