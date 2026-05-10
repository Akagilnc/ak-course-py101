import json
import pandas as pd


def process_data():
    # 读取json数据
    with open('l3.json', encoding='utf-8') as file:
        data = json.load(file).get('data').get('otherlist')
    # 找到海外疫情数据，转换为df
    df = pd.DataFrame(data, columns=['name', 'conNum', 'econNum'])
    # 重命名表头，转换数据int
    df = df.astype({'conNum': int, 'econNum': int})
    df = df.rename(columns={'name': '国家/地区', 'conNum': '累计确诊',
                            'econNum': '现存确诊'})
    # 根据条件筛选数据
    df = df[(df.get('累计确诊') > 20000) & (df.get('现存确诊') < 5000)]
    # 写入Excel
    df.to_excel('l7_report.xlsx', index=False, sheet_name='缓解区')


process_data()
