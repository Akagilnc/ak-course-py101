import pandas as pd


def make_top10():
    # 读取数据
    data = pd.read_excel('l7_data.xlsx')
    # 排序
    data = data.sort_values(by='累计确诊', ascending=False)
    # 取前十条
    top10_df = data.head(10)
    # 保存Excel
    top10_df.to_excel('l8_report.xlsx', index=False, sheet_name='top10')


# make_top10()


def make_better():
    # 读取数据
    data = pd.read_excel('l7_data.xlsx')
    data = data.set_index('国家/地区')
    # 找到符合条件的数据
    if_1 = data['累计确诊'] > 20000
    if_2 = data['现存确诊'] < 5000
    data[if_1 & if_2].to_excel('l8_report.xlsx', sheet_name='缓解区')
    # 保存


# make_better()


def make_status_report():
    # 读取数据
    data = pd.read_excel('l7_data.xlsx')
    data = data.set_index('国家/地区')
    # 生成差值列
    data['差值'] = data['累计确诊'] - data['治愈人数']
    # 根据差值的数值，确定状态列
    data.loc[data['差值'] >= 1000, '状态'] = '危险'
    data.loc[data['差值'] < 1000, '状态'] = '中等'
    data.loc[data['差值'] < 500, '状态'] = '良好'
    data.loc[data['差值'] < 100, '状态'] = '优秀'
    data = data.drop(columns='差值')

    print(data.groupby('状态').sum())
    print(data.groupby('状态').mean())
    print(data.groupby('状态').median())
    print(data.groupby('状态').size())


# make_status_report()

import json
import matplotlib.pyplot as plt


def make_history_report():
    with open('l3.json', encoding='utf-8') as file:
        data = json.load(file).get('data').get('otherhistorylist')
    data = pd.DataFrame(data, columns=['certain', 'die', 'recure', 'date'])
    data = data.set_index('date')
    data = data.astype({'certain': int, 'die': int, 'recure': int})
    data = data[::-1]
    plt.figure(figsize=(10, 5))
    # data['certain'].rolling(window=7).mean().plot(label='7-days', alpha=1)
    # data['certain'].rolling(window=30).mean().plot(label='Month-days', alpha=1)
    # data['certain'].rolling(window=90).mean().plot(label='Q-days', linewidth=3)
    # data['certain'].plot(label='Confirm Num', alpha=1)
    # data['recure'].plot(label='Recure Num')

    # plt.legend()
    # plt.show()
    data['die_rate'] = data['die'] / data['certain']
    data['recure_rate'] = data['recure'] / data['certain']
    corr_die = data['die_rate'].corr(data['certain'])
    corr_recure = data['recure_rate'].corr(data['certain'])
    print(data)
    print(corr_die, corr_recure)

make_history_report()
