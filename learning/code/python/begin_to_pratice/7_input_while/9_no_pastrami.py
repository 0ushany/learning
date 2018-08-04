# 五香烟熏牛肉卖完了

sandwich_orders = ['pastrami', 'pastrami', 'apple', 'pastrami', 'banana']

print("We have no pastrami now\n")

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

print("We have this now:")
for sandwich in sandwich_orders:
   print(sandwich) 
