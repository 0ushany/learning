# 三个出口

active = 0

while active != 3:
    pizza = input("what pizza you need?\n")
    if pizza == 'quit':
        break
    else:
        print("We add the " + pizza + " already!")
    active = active + 1
