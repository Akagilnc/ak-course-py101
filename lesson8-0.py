import json
import pandas as pd
import matplotlib.pyplot as plt


def process_data():
    # 读取json，找到国内历史数据
    with open('l3.json', encoding='utf-8') as file:
        data = json.load(file).get('data').get('historylist')
    # 获取治愈人数数据
    df = pd.DataFrame(data, columns=['date', 'cn_conNum'])
    df = df.astype({'cn_conNum': int})
    df = df.rename(columns={'date': '日期', 'cn_conNum': '累计确诊'})
    date_list = df['日期'].values.tolist()
    print(date_list)
    df = df.set_index('日期')
    # 生成报表
    plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']

    df.plot()
    plt.xticks(range(len(date_list))[0::10])
    plt.show()


process_data()

