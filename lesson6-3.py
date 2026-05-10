import json
import pandas as pd
import matplotlib.pyplot as plt

def read_json():
    with open('l3.json', encoding='utf-8') as file:
        return json.load(file)
def set_font(axes):

    return axes

def process_data():
    # 获取海外地区的数据
    data = read_json().get('data').get('otherlist')
    # 转换为DataFrame
    df = pd.DataFrame(data, columns=['name', 'conNum', 'cureNum'])
    # 重命名表头, 转换数据类型为int
    df = df.astype({'conNum': int, 'cureNum': int})
    df = df.rename(columns={'name': '国家/地区', 'conNum': '累计确诊', 'cureNum': '累计治愈'})
    df = df.set_index('国家/地区')
    # 获得差值
    df['差值'] = df['累计确诊'] - df['累计治愈']
    df = df.sort_values(by='差值', ascending=False)
    # 设置状态
    df.loc[df['差值'] >= 1000, '状态'] = '危险'
    df.loc[df['差值'] < 1000, '状态'] = '中等'
    df.loc[df['差值'] < 500, '状态'] = '良好'
    df.loc[df['差值'] < 100, '状态'] = '优秀'
    # 删除差值
    df = df.drop(columns='差值')
    # 写入Excel
    df.to_excel('l6_oversea_report.xlsx')
    plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']
    df = df.groupby(by='状态').median()
    df = df.reindex(['优秀', '良好', '中等', '危险'])
    df.plot(kind='bar')

    plt.show()
process_data()