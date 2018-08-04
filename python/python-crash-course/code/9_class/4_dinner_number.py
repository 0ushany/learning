# 就餐人数

class Restaurant():
    def __init__(self, name):
        self.name = name
        self.number_served = 0

    def show(self):
        print(str(self.number_served) + " come " + self.name + " have dinner ")

    def set_number_serverd(self, i):
        self.number_served = i

    def increament_number_serverd(self, i):
        for num in range(1, i + 1):
            self.number_served += 1
            print("There is 1 people come here")


res = Restaurant("honey")

res.set_number_serverd(5)
res.increament_number_serverd(3)
print(res.number_served)
res.show()
