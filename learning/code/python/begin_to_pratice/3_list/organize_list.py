# 组织列表

# 使用sort()对列表进行永久排序
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)

# sort()倒过来输出
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort(reverse = True)
print(cars)

print("------------------------------------------")

# sorted()临时排序
cars = ['bmw', 'audi', 'toyota', 'subaru']
print("Here is the original list:")
print(cars)

print("\nHere is the sorted list:")
print(sorted(cars))

print("\nHere is the original list again:")
print(cars)

print("------------------------------------------")

# reverse()倒着打印列表
cars =  ['bmw', 'audi', 'toyota', 'subaru']
print(cars)

cars.reverse()
print(cars)

print("------------------------------------------")

# len()确定列表的长度
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(len(cars))

