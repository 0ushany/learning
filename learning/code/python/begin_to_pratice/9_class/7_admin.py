# 管理员

class User():
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def describe_user(self):
        print("This user is " + self.first_name + " " + self.last_name)
    
    def greet_user(self):
        print("Hello, " + self.first_name + " " + self.last_name)

class Admin(User):
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        self.privileges = ['can add post']
    
    def show_privileges(self, i):
        print("Admin:" + self.first_name + " " + self.last_name)
        print("privileges: " + self.privileges[i])

admin = Admin('ou', 'shany')
admin.show_privileges(0)
