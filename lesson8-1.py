import json
import pandas as pd
import matplotlib.pyplot as plt


def process_data():
    # 读取世界疫情历史数据
    with open('l3.json', encoding='utf-8') as file:
        data = json.load(file).get('data').get('otherhistorylist')
    # 转换为df
    df = pd.DataFrame(data, columns=['date', 'die', 'certain'])
    df = df.astype({'die': int, 'certain': int})
    df = df.rename(columns={'date': '日期', 'die': '死亡人数'})
    # 对日期排序, 获取最近的十天
    df = df.sort_values(by='日期').tail(10)
    df = df.set_index('日期')
    plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']
    # 生成报表
    df.get('死亡人数').plot(kind='bar')
    # 保存图片
    plt.savefig('l8_report1.png')


process_data()
