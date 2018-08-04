# 用户

class User():
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def describe_user(self):
        print("This user is " + self.first_name + " " + self.last_name)
    
    def greet_user(self):
        print("Hello, " + self.first_name + " " + self.last_name)

user = User("shany", "ou")
user.describe_user()
user.greet_user()

print("")

user2 = User("pepper", "perry")
user2.describe_user()
user2.greet_user()

