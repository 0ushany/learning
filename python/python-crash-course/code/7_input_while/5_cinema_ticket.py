# 电影票

print("Welcome to ticket program!\n0 to quit :)")

m = input("How old are you?")
m = int(m)

while m != 0:
    if m < 3:
        print("Free! have fun!")
    elif 3 <= m < 12:
        print("You need to pay 10$!")
    else:
        print("You need to pay 15$!")
    m = input("\nHow old are you?\n")
    m = int(m)

print("Welcome to your next time!")

