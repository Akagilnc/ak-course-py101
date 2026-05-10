import json
import pandas as pd
import matplotlib.pyplot as plt
import openpyxl


def make_report_with_image():
    # 读取json的数据，世界历史疫情数据
    with open('lesson4.json', encoding='utf-8') as file:
        data = json.load(file).get('data').get('otherhistorylist')
    # 整理数据：转换dF，筛选要得列，转换数据类型，重命名表头，设置index
    data = pd.DataFrame(data, columns=['date', 'die', 'certain', 'recure'])
    data = data.astype({'die': int, 'certain': int, 'recure': int})
    data = data.rename(columns={'date': '日期', 'die': '死亡人数',
                                'certain': '累计确诊', 'recure': '治愈人数'})
    data = data.set_index('日期')
    # 根据日期排序，降序
    data = data.sort_values(by='日期').tail(10)
    # 生成bar chart 累计确诊和治愈人数
    plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']
    data[['累计确诊', '治愈人数']].plot(kind='bar')
    plt.savefig('report1.png')
    plt.close()
    # 生成line chart 死亡人数
    data[['死亡人数']].plot()
    plt.savefig('report2.png')
    # 保存到Excel（数据，图片）
    with pd.ExcelWriter('l8_report.xlsx', engine='openpyxl') as file:
        data.to_excel(file, sheet_name='世界疫情数据')
        sheet = file.sheets['世界疫情数据']
        img1 = openpyxl.drawing.image.Image('report1.png')
        img2 = openpyxl.drawing.image.Image('report2.png')
        img1.anchor = 'E1'
        img2.anchor = 'E25'
        sheet.add_image(img1)
        sheet.add_image(img2)


make_report_with_image()

