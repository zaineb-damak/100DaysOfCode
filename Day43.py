

dictionary = {"name": None, "url": None, "desc": None, "rating": None}

for key, value in dictionary.items():
    dictionary[key] = input(f'enter {key} : ')

for key, value in dictionary.items():
    print(f'{key}:{value}')
