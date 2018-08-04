# 城市
# 城市名字作为主键
# 城市信息用字典来存储，作为值

cities = {
    'newYork':{
        'country':'America',
        'population':'80W',
        'fact':'rich',
        },
    'shenzhen':{
        'country':'China',
        'population':'500W',
        'fact':'new',
        },
    'tokyo':{
        'country':'Japan',
        'population':'900W',
        'fact':'funny',
        },
    }

for key, value in cities.items():
    print(key + "is a country in " + value['country'] + 
    ", it has " + value['population'] + " population, it is " + value['fact'])

# 遍历键值对
# 值需要用值信息中的键再次调用


