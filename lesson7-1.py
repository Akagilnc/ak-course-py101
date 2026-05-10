import pandas as pd
import json


def process_data():
    # 读取json数据
    with open('l3.json', encoding='utf-8') as file:
        data = json.load(file).get('data').get('worldlist')
    # 转换为df，并且重命名表头和转换数据类型
    df = pd.DataFrame(data, columns=['name', 'value'])
    df = df.astype({'value': int})
    df = df.rename(columns={'name': '国家/地区', 'value': '累计确诊'})
    # 根据累计确诊排序
    df = df.sort_values(by='累计确诊', ascending=False)
    df = df.set_index('国家/地区')
    # 筛选最多的10个
    df_result = df.head(10)
    # 保存到Excel（append）
    with pd.ExcelWriter('l7_report.xlsx', mode='a', engine='openpyxl') as file:
        df_result.to_excel(file, sheet_name='top10')


process_data()
