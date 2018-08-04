# 元组
# 元组的所有元素都是不可变的，类似于常量

# dimensions.py
dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])

# 当尝试修改的时候
# dimensions[0] = 250
# 报错

print("-------------------------------")

# 遍历元组中的所有值
for dimension in dimensions:
    print(dimension)

print("-------------------------------")

# 然而直接修改元组变量是可以改变元组的
dimensions = (400, 100)
print("Modified dimensions:")
for dimension in dimensions:
    print(dimension)

print("-------------------------------")

# 元组存储字符串
dimensions = ('apple', 100)
for dimension in dimensions:
    print(dimension)
