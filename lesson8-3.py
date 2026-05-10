import json
import pandas as pd
import matplotlib.pyplot as plt
import openpyxl


def process_data():
    with open('l3.json', encoding='utf-8') as file:
        data = json.load(file).get('data').get('otherhistorylist')
    df = pd.DataFrame(data, columns=['date', 'certain', 'die', 'recure'])
    df = df.astype({'certain': int, 'die': int, 'recure': int})
    df = df.rename(columns={'date': '日期', 'certain': '累计确诊',
                            'die': '死亡人数', 'recure': '治愈人数'})
    df = df.set_index('日期')
    df_chart1 = df[['累计确诊', '治愈人数']].sort_values(by='日期').tail(10)
    df_chart1.plot(kind='bar')
    plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']
    plt.savefig('l8_report_1.png')
    df_chart2 = df[['死亡人数']].sort_values(by='日期')
    df_chart2.plot()
    plt.savefig('l8_report_2.png')
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
