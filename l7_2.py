import json
import pandas as pd


def make_top10_report():
    # 读取json文件
    with open('lesson4.json', encoding='utf-8') as file:
        data = json.load(file).get('data').get('otherlist')
    # 整理数据
    data = pd.DataFrame(data, columns=['name', 'conNum', 'econNum', 'cureNum', 'deathNum'])
    data = data.astype({'conNum': int, 'econNum': int, 'cureNum': int, 'deathNum': int})
    data = data.rename(columns={'name': '国家/地区', 'conNum': '累计确诊', 'econNum':"现存确诊",
                       'cureNum': '治愈人数', 'deathNum': '死亡人数'})
    data = data.set_index('国家/地区')
    # 累计确诊最多的十条数据
    data = data.sort_values(by='累计确诊', ascending=False)
    data = data.head(10)
    # 写入报告
    with pd.ExcelWriter('l7_report.xlsx', mode='a', engine='openpyxl') as file:
        data.to_excel(file, sheet_name='top10')


make_top10_report()
