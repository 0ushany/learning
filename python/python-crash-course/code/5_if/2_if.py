# if语句
# 简单的if语句

# voting.py
age = 19
if age >= 18:
    print("You are old enough to vote!")

print("-----------------------------------------------------")

# if-else语句
age = 17
if age >= 18:
    print("You are old enough to vote!")
    print("Have you registered to vote yet?")
else:
    print("Sorrry, you are too young to vote.")
    print("Please register to vote as soon as you turn 18!")
   
print("-----------------------------------------------------")

# if-elif-else语句
age = 12
if age < 4:
    print("You admission cost is $0")
elif age < 18:
    print("You admission cost is $5")
else:
    print("You admission cost is $10.")
# 这种if-elif-else结构的语句，只会执行其中一个
# 如果要多个判断，就要多个if语句，而不是if-elif-else


    
