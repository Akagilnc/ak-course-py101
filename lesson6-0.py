import pandas as pd
def process_data():
    # 读取Excel
    data = pd.read_excel('l5_data.xlsx', usecols=['直辖市/省份', '城市/地区', '累计确诊',
                                                  '现存确诊', '治愈', '死亡', '无病例天数'])
    # 直辖市/省份的值
    p_names = data['直辖市/省份'].unique()
    # 获得汇总数据
    sum_df = data[['累计确诊', '现存确诊', '治愈', '死亡', '无病例天数']].sum()
    # 写入汇总数据
    file = pd.ExcelWriter('l6_report.xlsx')
    sum_df = sum_df.rename('汇总')
    sum_df.to_excel(file, sheet_name='汇总')
    # 按省份筛选数据
    for p_name in p_names:
        # 写入分省数据
        p_df = data[data.get('直辖市/省份') == p_name]
        p_df.to_excel(file, sheet_name=p_name, index=False)
    file.close()
process_data()
