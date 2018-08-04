# 序数

# 在一个列表中存储1-9
numbers = list(range(1, 10))

for num in numbers:
    print(num)

# 打印对应的序数
for num in numbers:
    if num == 1:
        print(str(num) + "st")
    elif num == 2:
        print(str(num) + "nd")
    elif num == 3:
        print(str(num) + "rd")
    else:
        print(str(num) + "th")
