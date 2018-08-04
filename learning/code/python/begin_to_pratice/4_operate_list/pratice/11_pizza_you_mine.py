# 你的比萨和我的比萨
pizzas = ['apple', 'pear','banana','orange','lemon']
friend_pizzas = pizzas[:]
# 创建切片，复制给friend

pizzas.append('pineapple')
friend_pizzas.append('chizapple')

print("My favorite pizza are: ")
for pizza in pizzas:
    print(pizza)

print("----------------------------------------")

print("My friend's favorite pizza are: ")
for pizza in friend_pizzas:
    print(pizza)


# 这里还算简单，主要就是一些问题，关于复制
# 复制如果直接赋值，只会指向同一个列表
# 创建一个切片的副本再复制就不会有这个问题

