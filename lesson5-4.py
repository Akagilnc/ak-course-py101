import pandas as pd


def process_data():
    data = pd.read_excel('l5_data.xlsx',
                         usecols=['省份/直辖市', '城市/地区', '累计确诊', '现存确诊',
                                  '治愈', '死亡', '最长清零天数'])
    provinces = data.get('省份/直辖市').unique()
    with pd.ExcelWriter('l5_report.xlsx') as writer:
        for p_name in provinces:
            temp_df = data[(data['省份/直辖市'] == p_name)]
            temp_df = temp_df.set_index('城市/地区')

            sum_df = temp_df[['累计确诊', '现存确诊', '治愈', '死亡']].sum()
            sum_df = sum_df.rename('汇总')

            temp_df = temp_df.append(sum_df)
            temp_df.to_excel(writer, sheet_name=p_name)



process_data()