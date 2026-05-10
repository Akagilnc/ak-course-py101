import pandas as pd


def process_data():
    # 读取Excel数据
    data = pd.read_excel('l5_data.xlsx')
    # 筛选数据
    df = data[(data['累计确诊'] > 1000) & (data['现存确诊'] < 100)]
    df = df.set_index('直辖市/省份')
    # 写入数据
    with pd.ExcelWriter('l6_report.xlsx', mode='a', engine='openpyxl') as file:
        df.to_excel(file, sheet_name='缓解区')

process_data()
