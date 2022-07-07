import json
import pandas as pd
import matplotlib.pyplot as plt


def process_data():
    # 读取数据
    with open('l3.json', encoding='utf-8') as file:
        data = json.load(file).get('data').get('worldlist')
    # 转换df
    df = pd.DataFrame(data, columns=['name', 'value', 'cureNum'])
    df = df.astype({'value': int, 'cureNum': int})
    df = df.rename(columns={'value': '累计确诊', 'cureNum': '治愈', 'name': '国家/地区'})
    # 计算差值，并生成状态列
    df['差值'] = df['累计确诊'] - df['治愈']
    df.loc[df['差值'] >= 1000, '状态'] = '危险'
    df.loc[df['差值'] < 1000, '状态'] = '中等'
    df.loc[df['差值'] < 500, '状态'] = '良好'
    df.loc[df['差值'] < 100, '状态'] = '优秀'
    # 计算状态的记录数量
    df_count = df['状态'].value_counts()
    # 生成图表，保存图片
    plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']
    df_count = df_count.reindex(['危险', '中等', '良好', '优秀'])
    df_count.plot(kind='bar')
    plt.savefig('l8_report2.png')

process_data()
