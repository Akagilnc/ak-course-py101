import pandas as pd
def read_and_save():
    # 读取Excel
    # 筛选列
    data = pd.read_excel('l5_data.xlsx', usecols="A:D,G")
    # 按照省区分数据
    provinces = data['直辖市/省份'].unique()
    file = pd.ExcelWriter('l5_report.xlsx')
    for p_name in provinces:
        p_data = data[data['直辖市/省份'] == p_name]

    # 按照省份数据保存到响应的省份sheet下
        p_data = p_data.drop(columns=['直辖市/省份'])
        p_data.to_excel(file, sheet_name=p_name, index=False)
    file.save()


read_and_save()
