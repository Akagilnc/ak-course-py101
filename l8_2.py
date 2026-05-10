import json
import pandas as pd
import matplotlib.pyplot as plt


def make_chart_to_image():
    # 读取json的数据
    with open('lesson4.json', encoding='utf-8') as file:
        data = json.load(file).get('data').get('otherhistorylist')
    # 整理数据
    data = pd.DataFrame(data, columns=['date', 'die'])
    data = data.astype({'die':int})
    data = data.rename(columns={'die': '死亡人数', 'date': '日期'})
    data = data.set_index('日期')
    # 根据日期排序，从老到新，并且截取10条
    data = data.sort_values(by='日期').tail(10)
    # 生成报表
    plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']
    data.plot(kind='bar')
    plt.tight_layout()
    # 保存为图片
    plt.savefig('report1.jpg')


make_chart_to_image()
