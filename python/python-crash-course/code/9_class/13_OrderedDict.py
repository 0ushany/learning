from collections import OrderedDict

favorite = OrderedDict()

favorite['a'] = 'a'
favorite['e'] = 'e'
favorite['b'] = 'b'

for key, value in favorite.items():
    print(key.title() + "'s favorite is " + value.title() + ".")
