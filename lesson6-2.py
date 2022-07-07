import pandas as pd

def process_data():
    # 读取Excel数据
    data = pd.read_excel('l5_data.xlsx', usecols=['直辖市/省份', '城市/地区', '累计确诊',
                                                  '现存确诊', '治愈', '死亡', '无病例天数'])
    # 根据条件筛选数据
    df = data[(data.get('累计确诊') > 1000) & (data.get('现存确诊') < 100)]
    df = df.set_index('城市/地区')
    sum_data = df[['累计确诊', '现存确诊', '治愈', '死亡', '无病例天数']].sum()
    sum_data = sum_data.rename('汇总')
    df = df.append(sum_data)
    # 将数据写入到已有文件。并且保留之前的数据
    with pd.ExcelWriter('l6_report.xlsx', mode='a', engine='openpyxl') as file:
        df.to_excel(file, sheet_name='缓解区')

process_data()