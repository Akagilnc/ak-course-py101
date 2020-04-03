import json
import pandas as pd


def read_data_from_json(file_name):
    with open(file_name, encoding='utf_8') as file:
        return json.load(file)


def process_and_save():
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
                "确诊": float(confirm),
                "治愈": int(cure),
                "死亡": int(death)
            })
    return result_list


def save_to_file(input_result):
    with open('l4_hw_report.txt', 'w', encoding='utf_8') as report:
        report.writelines(input_result)


pd.options.display.float_format = '{:,}'.format
result = process_and_save()
contents = pd.DataFrame(result)
contents = contents.astype({'确诊': 'float', '治愈': 'int32', '死亡': 'float'})
contents.to_csv('l4_hw.csv', index=False)
print(contents[contents.省份 == '湖北'])
contents.to_excel('l4_hw.xlsx', index=False)

import matplotlib
contents.plot.line()
