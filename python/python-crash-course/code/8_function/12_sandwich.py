# 三明治

# 接受顾客要加在三明治里面的一系列食材
def sandwich(*sandwich):
    for s in sandwich:
        print(s + " is already added")

sandwich('apple', 'pear', 'banana')
