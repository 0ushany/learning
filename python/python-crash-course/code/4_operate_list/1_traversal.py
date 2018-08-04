# 遍历列表

#magicians.py
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician)


print("------------------------------------")

# magicians 2
for magician in magicians:
    print(magician.title() + ", that was a great trick!")


print("------------------------------------")
# 缩进了就是for循环中的一部分
for magician in magicians: 
    print(magician.title() + ", that was a great trick!")
    print("I can't wait to see your next trick, " + magician.title() + ".\n")
print("Thank you, everyone. That was a great magic show!")

print("------------------------------------")


