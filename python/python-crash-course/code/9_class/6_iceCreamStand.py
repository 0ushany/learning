# 冰淇淋小店
class Restaurant():
    def __init__(self, restaurant_name):
        self.restaurant_name = restaurant_name

    def describe_restaurant(self):
        print("This restaurant is " + self.restaurant_name + "\n")

    def open_restaurant(self):
        print("We are open for guest now!")

class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name):
        super().__init__(restaurant_name)
        self.flavors = ['apple', 'coffee', 'banana']

ice = IceCreamStand("osyHome")    
ice.describe_restaurant()
ice.open_restaurant()
print(ice.flavors)
