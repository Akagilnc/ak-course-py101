import json
import pandas as pd


def read_data_from_json(file_name):
    with open(file_name, encoding='utf_8') as file:
        return json.load(file)


def process_data():
    data = read_data_from_json('lesson4.json').get('data').get('list')
    result_list = []

    for info in data:
        cities = info.get('city')
        province_name = info.get('name')
        for city in cities:
            name = city.get('name')
            confirm = city.get('conNum')
            cure = city.get('cureNum')
            death = city.get('deathNum')
            result_list.append({
                '省份': province_name,
                '地区': name,
                '确诊': confirm,
                '治愈': cure,
                '死亡': death
            })
    return result_list


result = process_data()
contents = pd.DataFrame(result)
contents = contents.astype({'确诊': 'int', '治愈': 'int', '死亡': 'int'})
print(contents[contents.省份 == '湖北'])
# contents.to_excel('l4_hw.xlsx', index=False)
