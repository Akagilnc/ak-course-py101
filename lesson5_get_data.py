import requests
import json
import pandas as pd


# 获取最新数据 
def call_api_and_save_json(address, file_name):
    data = requests.get(address)
    with open(file_name, 'w', encoding='utf_8') as file:
        json.dump(data.json(), file, ensure_ascii=False, indent=4)


# 读取json
def read_file(file_name):
    with open(file_name, encoding='utf_8') as file:
        # 转换为字典输出
        return json.load(file).get('results')


# 将疫情信息存入excel
def process_and_save(input_df, file_name):
    # # 把数据加载入pandas
    # 把结果写入excel文件
    with open('H:/PycharmProjects/2020/json_files/{}'.format(file_name), 'w', encoding='utf_8') as file:
        input_df.to_json(file, force_ascii=False, indent=4, orient='records')


# call_api_and_save_json('https://lab.isaaclin.cn/nCoV/api/area', '2019_conv.json')
infos = read_file('2019_conv.json')
data_df = pd.DataFrame(infos)
continents = pd.DataFrame(infos, columns=['continentName']).drop_duplicates()
for cont in continents.values:
    cont = cont[0]
    info = data_df[data_df.continentName == cont]
    process_and_save(info, "{}.json".format(cont))
