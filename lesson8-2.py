import json
import pandas as pd
import matplotlib.pyplot as plt


def process_data():
    # 读取json数据，找到世界疫情
    with open('l3.json', encoding='utf-8') as file:
        data = json.load(file).get('data').get('worldlist')
    # 转换为df, 转换数据类型，重命名表头，设置索引
    df = pd.DataFrame(data, columns=['name', 'value', 'cureNum'])
    df = df.astype({'value': int, 'cureNum': int})
    df = df.rename(columns={'name': '国家/地区', 'value': '累计确诊', 'cureNum': '治愈'})
    df = df.set_index('国家/地区')
    # 计算差值
    df['差值'] = df.get('累计确诊') - df.get('治愈')
    # 根据差值，得到状态列的值
    df.loc[df['差值'] >= 1000, '状态'] = '危险'
    df.loc[df['差值'] < 1000, '状态'] = '中等'
    df.loc[df['差值'] < 500, '状态'] = '良好'
    df.loc[df['差值'] < 100, '状态'] = '优秀'
    df = df.drop(columns='差值')
    # 统计状态列的记录条数
    df_count = df['状态'].value_counts()
    # 排序为 危险到优秀
    df_count = df_count.reindex(['危险', '中等', '良好', '优秀'])
    # 生成bar chart
    chart = df_count.plot(kind='bar')
    # 保存图片
    plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']
    plt.bar_label(chart.containers[0])
    plt.savefig('l8_report2.png')
process_data()