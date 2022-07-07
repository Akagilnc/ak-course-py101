spam = {'name': 'Curry', 'age': '32',
        'kids': [{'name': 'Riley'}, {'name': 'Canon'}, {'name': 'Ryan'}]}

data = spam.get('kids')
for kid in data:
    print(kid.get('name'))

