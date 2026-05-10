import pandas as pd
def process_data():
    # 读取Excel
    data = pd.read_excel('l5_data.xlsx', usecols=['直辖市/省份', '城市/地区', '累计确诊',
                                                  '现存确诊', '治愈', '死亡', '无病例天数']
                         )
    # 获取直辖市/省份的值
    provinces = data.get('直辖市/省份').unique()
    # 按省份筛选数据
    file = pd.ExcelWriter('l6_report.xlsx')
    for p_name in provinces:
        p_df = data[data.get('直辖市/省份') == p_name]
        p_df = p_df.set_index('城市/地区')
        # 按照省份汇总
        p_sum_df = p_df[['累计确诊', '现存确诊', '治愈', '死亡', '无病例天数']].sum()
        p_sum_df = p_sum_df.rename('汇总')
        # 合并数据集
        p_df = p_df.append(p_sum_df)
        # 写入Excel
        p_df.to_excel(file, sheet_name=p_name)
    file.close()

process_data()