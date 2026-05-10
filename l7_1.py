import json
import pandas as pd


def make_better_report():
    # 读取json数据，并找到海外疫情数据
    with open('lesson4.json', encoding='utf-8') as file:
        data = json.load(file).get('data').get('otherlist')
    # 转换为df , 修改表头和数据类型 （数据整理）
    df = pd.DataFrame(data, columns=['name', 'conNum', 'econNum', 'cureNum', 'deathNum'])
    df = df.astype({'conNum': int, 'econNum': int, 'cureNum': int, 'deathNum': int})
    df = df.rename(columns={'name': '国家/地区', 'conNum': '累计确诊', 'econNum': '现存确诊',
                            'cureNum': '治愈人数', 'deathNum': '死亡人数'})
    # 根据条件筛选出符合缓解区规则的数据
    if_1 = df['累计确诊'] > 20000
    if_2 = df['现存确诊'] < 5000
    # 保存到Excel报告
    df = df[if_1 & if_2].set_index('国家/地区')
    df.to_excel('l7_report.xlsx', sheet_name='缓解区')


make_better_report()
