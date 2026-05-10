import json
import pandas as pd
import matplotlib.pyplot as plt
def process_data():
    # 读取json数据。并找到世界历史数据
    with open('l3.json', encoding='utf-8') as file:
        data = json.load(file).get('data').get('otherhistorylist')
    # 转换为df , 转换数据类型，重命名表头，设置index
    df = pd.DataFrame(data, columns=['date', 'die'])
    df = df.astype({'die': int})
    df = df.rename(columns={'date': '日期', 'die': '死亡人数'})
    df = df.set_index('日期')
    # 排序，日期从老到新
    # 筛选最新的十天
    df = df.sort_values(by='日期').tail(10)
    # 生成bar chart
    df.plot(kind='bar')
    plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']
    plt.xlabel('日期')
    plt.ylabel('人数')
    plt.tight_layout()
    # 保存图片
    plt.savefig('l8_report1.png')
process_data()
