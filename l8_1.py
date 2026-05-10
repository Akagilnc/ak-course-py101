import json
import pandas as pd
import matplotlib.pyplot as plt


def make_line_chart():
    with open('lesson4.json', encoding='utf-8') as file:
        data = json.load(file).get('data').get('otherhistorylist')
    data = pd.DataFrame(data, columns=['die', 'date'])
    data = data.astype({'die': int})
    data = data.rename(columns={'die': '死亡人数', 'date': '日期'})
    data = data.set_index('日期')
    data = data.sort_values(by='日期')
    data.plot()
    plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']
    plt.show()


make_line_chart()
