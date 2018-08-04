# 检查用户名
# 确保网站每位用户名都独一无二
current_users = ['Osy', 'apple', 'oshany', 'tencent', 'huawei']
new_users = ['osy', 'tencent', 'banana', 'uu', 'tonyma']

# 不区分大小写的方法，就是全部转化为大写再比较
for user in new_users:
    for user1 in current_users:
        if user.upper() == user1.upper():
            print(user + " is used, please choice another name")

# 两层循环比较，外层循环遍历new_user
# 内存循环对每一位newuser与全部的cur_user进行比较
