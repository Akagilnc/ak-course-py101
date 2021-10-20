import json
import pandas as pd
def read_from_json(file_name):
    with open(file_name, encoding='utf-8') as file:
        return json.load(file).get('data').get('list')
def process_data(infos):
    result_list = []
    for provice in infos:
        p_name, cities = provice.get('name'), provice.get('city')
        for city in cities:
            c_name, e_con = city.get('name'), city.get('econNum')
            con, cure = city.get('conNum'), city.get('cureNum')
            death, zero_days = city.get('deathNum'), city.get('zerodays')
            city_dict = {'直辖市省份': p_name, '城市地区': c_name, '现存确诊': e_con, '累计确诊': con,
                         '治愈': cure, '死亡': death, '无病例天数': zero_days}
            result_list.append(city_dict)
    return result_list
data = read_from_json('l3.json')
result_list = process_data(data)
contents = pd.DataFrame(result_list)
contents = contents.astype({'现存确诊': 'int', '累计确诊': 'int'})
contents = contents[contents.直辖市省份 == '湖北']
contents.to_excel('l4_report.xlsx')
