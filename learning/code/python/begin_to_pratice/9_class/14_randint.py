# 骰子

from random import randint

x = randint(1, 6)

class Die():
    def __init__(self, sides=6):
        self.sides = sides

    def rool_die(self):
        for i in range(1, 11):
            print(randint(1, self.sides))

print("6 side:")
die = Die()
die.rool_die()

print("\n10 sides:")
die10 = Die(10)
die10.rool_die()

print("\n20 sides:")
die20 = Die(20)
die20.rool_die()
