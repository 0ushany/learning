# 不变的魔术师

def make_great(magicians):
    for i in range(len(magicians)):
        magicians[i] = "The Great " + magicians[i]

magicians = ['osy', 'piper', 'oshany']

make_great(magicians[:])
print(magicians)

make_great(magicians)
print(magicians)
