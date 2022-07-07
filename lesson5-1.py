import pandas as pd
import json


# 读取json文件
def read_json():
    file = open('l3.json', encoding='utf-8')
    return json.load(file).get('data').get('list')
def process_data():
    data = read_json()
    results = []
    for province in data:
        p_name = province.get('name')
        cities = province.get('city')
        for city in cities:
            city['p_name'] = p_name
            results.append(city)
    df = pd.DataFrame(results)
    df = df.rename(columns={'name': '城市/地区', 'p_name': '直辖市/省份', 'conNum': '累计确诊',
                    'econNum': '现存确诊', 'cureNum': '治愈', 'deathNum': '死亡',
                    'zerodays': '无病例天数'})
    df = df.astype({'累计确诊': int, '现存确诊': int, '治愈': int, '死亡': int})

    df = df[['直辖市/省份'] + [col for col in df if col != '直辖市/省份']]

    df.to_excel('l5_data.xlsx', index=False)
process_data()