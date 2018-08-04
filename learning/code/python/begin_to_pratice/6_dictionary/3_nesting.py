# 嵌套
# 字典嵌套在字典里，字典嵌套在列表里，列表嵌套在字典里 

# aliens.py
# 字典嵌套在列表里面
alien_0 = {'color':'green', 'point':5}
alien_1 = {'color':'yellow', 'point':10}
alien_2 = {'color':'red', 'point':15}

aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
    print(alien)

print("-----------------------------------")

# pizza.py
# 列表嵌套在字典里面
pizza = {
        'crust':'thick',
        'toppings':['mushrooms', 'extra cheese'],
        }

# 概述所有的比萨
print("You ordered a " + pizza['crust'] + "-crust pizza" +
        "with the following toppings:")

for toppings in pizza['toppings']:
    print("\t" + toppings)

print("-----------------------------------")

# many_users.py
# 字典嵌套在字典里面
# 名字作为键，详细信息作为值
users = {
        'aeinstein': {
            'first':'albert',
            'last':'einstein',
            'location':'princeton',
            },

        'mcurie': {
            'first':'marie',
            'last':'curie',
            'location':'paris',
            },

        }

# 遍历users字典的键值对，从值中在取出对应的数据，然后拼凑一下组成别的
for username, user_info in users.items():
    print("\nUsername: " + username)
    full_name = user_info['first'] + " " + user_info['last']
    location = user_info['location']

    print("\tFull name: " + full_name.title())
    print("\tLocation: " + location.title())
    
