# 列表解析
# 使用列表解析生成一个列表，其中包含前十个整数的立方
cubes = [value**3 for value in range(1, 11)]
for cube in cubes:
    print(cube)


# 这个比前面写的那个简便点，把基本序列直接用一个range(1, 11)给解决了
