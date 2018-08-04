# 梦想的度假圣地

active = True
dream_place = []

while active == True:
    dream = input("If you could visit one place in the world, where would you go?\n")

    if dream == 'quit':
        break

    dream_place.append(dream)

print("\nThe people's dream holiday resort:")
for dream in dream_place:
    print(dream)



