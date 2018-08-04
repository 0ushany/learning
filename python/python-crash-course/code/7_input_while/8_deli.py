# 熟食店

sandwich_orders = ['apple', 'banana', 'pear']
finished_sandwiches = []

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print("I made your " + current_sandwich + " sandwich\n")
    finished_sandwiches.append(current_sandwich)

print("All the sandwich made are this")
for sandwich in finished_sandwiches:
    print(sandwich)
