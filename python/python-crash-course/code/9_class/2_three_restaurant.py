# 三个餐馆

class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print("This restaurant is " + self.restaurant_name + "\n")
        print("cuisine is " + self.cuisine_type + "\n")

    def open_restaurant(self):
        print("We are open for guest now!")


restaurant = Restaurant("oshany's MagicRoom", "noodle-maker")

restaurant.describe_restaurant()
restaurant.open_restaurant()

res2 = Restaurant("aaa", 'abasdf')
res3 = Restaurant("asdfa", 'asdf')

res2.describe_restaurant()
res3.describe_restaurant()
