# 用户的专辑

def make_album(singer, name):
    album = {'singer':singer, 'name':name}
    return album

flag = 1
while flag:
    singer = input("input the singer:\n")
    name = input("input the album name:\n")
    if singer == '1':
        break
    album = make_album(singer, name)
    print(album)
    
