# 函数input()的工作原理

# parrot.py
# input显示并且接收用户输出，存储到变量指向的空间里
message = input("Tell me something, and I will repeat it back to you: ")
print(message)

print("--------------------------------------")

# greeter.py
name = input("Please enter your name: ")
print("Hello, " + name + "!")

print("--------------------------------------")

# greeter.py
prompt = "If you tell us who you are, we can personalize the message you see."
# 拼接了一个字符串
prompt += "\nWhat is your first name?"

# input的字符串是用来提示输入的
name = input(prompt)
print("\nHello, " + name + "!")

print("--------------------------------------")

# 啊使用int()获取数值输入
age = input("How old are you? ")
print(age)

print("--------------------------------------")

# 
