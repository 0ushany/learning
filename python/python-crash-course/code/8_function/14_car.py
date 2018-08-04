# 汽车

def make_car(maker, type1, **car_info):
    profile = {}
    profile['maker'] = maker
    profile['type1'] = type1
    for key, value in car_info.items():
        profile[key] = value

    return profile

car = make_car('subaru', 'outback', color='blue', tow_package=True)

print(car)
