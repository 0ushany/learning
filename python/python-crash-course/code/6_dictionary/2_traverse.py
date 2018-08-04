# 遍历字典的所有键
# keys()方法遍历所有键
# items()方法遍历所有键值对


favorite_languages = {
        'jen':'python',
        'sarah':'c',
        'edward':'ruby',
        'phil':'python',
        }

for name in favorite_languages.keys():
    print(name.title())

print("------------------------------------")

for key, value in favorite_languages.items():
    print(key + ":" + value)

print("------------------------------------")

# 按顺序遍历
# 函数sorted()，将字典内容先排序好在遍历出来
for name in sorted(favorite_languages.keys()):
    print(name.title() + ", thank you for taking the poll.")

print("------------------------------------")

# 遍历字典的所有值
# values()方法
print("The follwing languages have been mentioned:")
for language in favorite_languages.values():
    print(language.title())

print("------------------------------------")

# 提取为集合（值不重复，独一无二)
# set()方法
print("The follwing languages have been mentioned:")
for language in set(favorite_languages.values()):
    print(language.title())

# 总结一下：
# items()
# keys()
# values()
# sorted()
# set()
