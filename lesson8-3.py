import json
import pandas as pd
import matplotlib.pyplot as plt
import openpyxl


def process_data():
    # 读取数据
    with open('l3.json', encoding='utf-8') as file:
        data = json.load(file).get('data').get('otherhistorylist')
    # 转换df
    df = pd.DataFrame(data, columns=['date', 'certain', 'recure', 'die'])
    df = df.astype({'certain': int, 'recure': int, 'die': int})
    df = df.rename(columns={'date': '日期', 'certain': '累计确诊',
                            'recure': '治愈', 'die': '死亡'})
    df = df.sort_values(by='日期')
    df = df.set_index('日期')
    # 生成累计确诊和治愈的图表。并保存为图片
    plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']
    df[['累计确诊', '治愈']].tail(10).plot(kind='bar')
    plt.xlabel('日期')
    plt.ylabel('人数')
    plt.tight_layout()
    plt.savefig('l8_report_1.png')
    plt.clf()
    # 生成死亡人数的图表，并保存为图片
    df['死亡'].plot()
    plt.savefig('l8_report_2.png')
    # 把图片插入Excel
    with pd.ExcelWriter('l8_report.xlsx', engine='openpyxl') as file:
        df.to_excel(file, sheet_name='世界疫情数据')
        sheet = file.sheets['世界疫情数据']
        img1 = openpyxl.drawing.image.Image('l8_report_1.png')
        img2 = openpyxl.drawing.image.Image('l8_report_2.png')
        img1.anchor = 'E1'
        img2.anchor = 'E25'
        sheet.add_image(img1)
        sheet.add_image(img2)

process_data()