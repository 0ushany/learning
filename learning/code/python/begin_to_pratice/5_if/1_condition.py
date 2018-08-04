# 条件测试
# cars.py
cars = ['audi', 'bmw', 'subaru', 'toyota']

for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

print("-------------------------------------------")

# 检查是否不相等
# toppings.py
requested_topping = 'mushrooms'

if requested_topping != 'anchovies':
    print("Hold the anchovies")

print("-------------------------------------------")

# 检查多个条件
# and

age_0 = 22
age_1 = 18
print(age_0 >= 21 and age_1 >= 21)

# or

print(age_0 >= 21 or age_1 >= 21)

print("-------------------------------------------")

# 检查特定值是否包含在列表中
# in

requested_toppings = ['mushrooms', 'onions', 'pineapple']
print('mushrooms' in requested_toppings)
print('peperoni' in requested_toppings)

# not in
# banned_users.py
banned_users = ['andrew', 'carolina', 'david']
user = 'marie'

if user not in banned_users:
    print(user.title() + ", you can post a response if you wish.")


