import json
import pandas as pd


def read_and_write_excel(file_name):
    # 读取海外疫情数据
    with open(file_name, encoding='utf-*') as file:
        data = json.load(file).get('data').get('otherlist')
    # 筛选我们要列
    df = pd.DataFrame(data, columns=['name', 'conNum', 'econNum', 'cureNum', 'deathNum'])
    # 转换列的数据类型
    df = df.astype({'conNum': int, 'econNum': int, 'cureNum': int, 'deathNum': int})
    # 重命名表头
    df = df.rename(columns={'conNum': '累计确诊', 'econNum': '现存确诊',
                            'cureNum': '治愈人数', 'deathNum': '死亡人数', 'name': '国家/地区'})
    # 存储Excel
    df.to_excel('l7_data.xlsx', index=False, sheet_name='data')


# read_and_write_excel('l3.json')


def practice_df():
    data = pd.read_excel('l7_data.xlsx')
    data['死亡率'] = data['死亡人数'] / data['累计确诊']
    data['治愈率'] = data['治愈人数'] / data['累计确诊']
    df = data[['国家/地区', '累计确诊', '治愈率', '死亡率']]
    df = df.set_index('国家/地区')
    df.loc['平均'] = df.mean(numeric_only=True)
    df.loc['中位数'] = df.median(numeric_only=True)
    df[['死亡率', '治愈率']] = df[['死亡率', '治愈率']].map('{:.2%}'.format)
    df.to_excel('l7_report.xlsx', sheet_name='报告')


practice_df()
