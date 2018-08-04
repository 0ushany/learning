# 调查

people = {'osy':'ckd', 'oshany':'ckd', '0shany':'nck', 'oshay':'nck'}
for key, value in people.items():
    if value == 'ckd':
        print(key + "Thank you to check by us!")
    elif value == 'nck':
        print(key + "Please take a check with us!")

# 这个很简单，只要遍历对应的键值对
# 只要值是检查过了，那就打印感谢
# 如果没检查过，那就要求进行检查



