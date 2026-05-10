import pandas as pd
import json


# 读取json文件
def read_json():
    file = open('l3.json', encoding='utf-8')
    return json.load(file).get('data').get('list')


def process_data(data):
    # 获取省份/直辖市疫情数据
    results = []
    for province in data:
        # 获得省份/直辖市的名称和城市地区数据
        p_name = province.get('name')
        cities = province.get('city')
        for city in cities:
            # 组装字典，添加入结果集
            result = {"直辖市/省份": p_name, '城市/地区': city.get('name'),
                      '现存确诊': city.get('econNum'), '累计确诊': city.get('conNum'),
                      '治愈': city.get('cureNum'), '死亡': city.get('deathNum'),
                      '无病例天数': city.get('zerodays')}
            results.append(result)
    # 转换为DF
    df = pd.DataFrame(results)
    # 设置int数据类型
    df = df.astype({'现存确诊': int, '累计确诊': int, '治愈': int, '死亡': int})
    # 写入Excel
    df.to_excel('l5_data.xlsx', index=False)
data = read_json()
process_data(data)
