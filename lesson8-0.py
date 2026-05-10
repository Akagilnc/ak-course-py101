import pandas as pd
import json
import matplotlib.pyplot as plt


def process_data():
    # 读取json数据
    # 获取世界历史疫情数据
    with open('l3.json', encoding='utf-8') as file:
        data = json.load(file).get('data').get('otherhistorylist')
    # 转换为df, 重命名表头，转换数据类型
    df = pd.DataFrame(data, columns=['date', 'die'])
    df = df.astype({'die': int})
    df = df.rename(columns={'date':  '日期', 'die': '死亡人数'})
    df = df.set_index('日期')
    # 排序
    df = df.sort_values(by='日期')
    # 生成line chart
    df.plot()
    plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']
    plt.show()


process_data()
