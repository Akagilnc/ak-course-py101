import json
import pandas as pd
import matplotlib.pyplot as plt
import openpyxl


def process_data():
    plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']
    # 读取世界历史数据并整理
    with open('l3.json', encoding='utf-8') as file:
        data = json.load(file).get('data').get('otherhistorylist')
    # 排序并获得最近十天的数据
    data = pd.DataFrame(data,columns=['date', 'certain', 'recure', 'die'])
    data = data.astype({'certain': int, 'recure': int, 'die': int})
    data = data.rename(columns={'date': '日期', 'certain': '累计确诊',
                                'recure': '治愈', 'die': '死亡'})
    data = data.set_index('日期')
    # 生成累计确诊与治愈人数的bar chart
    df_chart1 = data[['累计确诊', '治愈']].sort_values(by='日期').tail(10)
    df_chart1.plot(kind='bar')
    plt.savefig('l8_report_1.png')
    # 死亡人数的line chart
    df_chart2 = data[['死亡']].sort_values(by='日期')
    df_chart2.plot()
    plt.savefig('l8_report_2.png')
    # 保存到Excel 世界疫情数据 sheet
    with pd.ExcelWriter('l8_report.xlsx', engine='openpyxl') as file:
        data.to_excel(file, sheet_name='世界疫情数据')
        sheet = file.sheets['世界疫情数据']
        img1 = openpyxl.drawing.image.Image('l8_report_1.png')
        img2 = openpyxl.drawing.image.Image('l8_report_2.png')
        img1.anchor = 'E1'
        img2.anchor = 'E25'
        sheet.add_image(img1)
        sheet.add_image(img2)
process_data()