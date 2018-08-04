# 了不起的魔术师

def make_great(magicians):
    for i in range(len(magicians)):
        magicians[i] = "the Great " + magicians[i]


magicians = ['osy', 'oshany', 'peppri']

make_great(magicians)

print(magicians)
