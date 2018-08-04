# 河流
rivers = {'changjiang':'china', 'yelloriver':'china', 'oshayriver':'china'}
for key, value in rivers.items():
    print("The " + key + " runs through " + value)


# 输出每条河流
for key in rivers.keys():
    print(key)

# 输出每个国家
for value in rivers.values():
    print(value)
