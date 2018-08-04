# 创建数值列表
# 自动生成

# numbers.py
for value in range(1,5):
    print(value)

# range()
# range(1, 5)，生成的数字是1-4,所以要生成1-5需要range(1,6)

print("--------------------------------------")

# 使用list()和range()创建数字列表
numbers = list(range(1, 6))
print(numbers)


print("--------------------------------------")

# range()函数可以指定步长
even_numbers = list(range(2, 11, 2))
# 2-11，不断加2
print(even_numbers)

print("--------------------------------------")



# squares.py
# 将前十个整数的平方加入到一个列表中
squares = []
for value in range(1, 11):
    square = value**2
    squares.append(square)

    print(squares)

print("--------------------------------------")


# 几个专门用于处理数字列表的python函数
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(min(digits))
print(max(digits))
print(sum(digits))


print("--------------------------------------")


# 列表解析
# squares.py
squares = [value**2 for value in range(1, 11)]
print(squares)
# value**2是其中的值，for value in range(1, 11)是为了给value**2提供变量值

