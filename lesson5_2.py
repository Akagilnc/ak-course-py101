import pandas as pd
import json


def read_json_file(file_name):
    with open(file_name, encoding='utf-8') as file:
        return json.load(file)


def process_and_save_to_excel(file_name):
    data = read_json_file('lesson3.json').get('data').get('otherlist')
    content_df = pd.DataFrame(data, columns=['name', 'conNum', 'cureNum', 'deathNum'])
    content_df = content_df.rename(columns={'name': '地区', 'conNum': '累计确诊',
                                            'cureNum': '治愈', 'deathNum': '死亡'})
    content_df = content_df.astype({'累计确诊': int, '治愈': int, '死亡': int})
    cols = ['累计确诊', '治愈', '死亡']
    content_df = content_df.set_index('地区')
    content_df = content_df.append(content_df[cols].sum().rename('合计'))
    with pd.ExcelWriter(file_name) as file:
        content_df.to_excel(file, sheet_name='oversea_area')


process_and_save_to_excel('l5_2.xlsx')