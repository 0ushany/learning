# 处理没有用户的情形

users = ['admin', 'osy', 'oshany']

for user in users:
    print(user)

for user in range(3):
    print(users)
    del users[0]

if users: 
    print("We have users")
else:
    print("We need to find some users!") 
