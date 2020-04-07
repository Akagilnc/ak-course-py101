import json
import pandas as pd

with open('lesson4.json') as file:
    data = json.load(file)
    data = data.get('data').get('list')[0]
    cities = data.get('city')

df = pd.DataFrame(cities)
df = df.set_index('name')
print(df)
