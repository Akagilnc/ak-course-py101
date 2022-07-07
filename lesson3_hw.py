spam = {'name': 'Curry',
        'age': '32',
        'kids': [{'name': 'Riley'}, {'name': 'Canon'}, {'name': 'Ryan'}]}

infos = spam.get('kids')
for kid in infos:
    print(kid.get('name'))