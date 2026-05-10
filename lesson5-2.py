import pandas as pd


def process_data():
    # 读取Excel文件，并筛选列
    data = pd.read_excel('l5_data.xlsx', usecols=['直辖市/省份', '城市/地区', '累计确诊',
                                                  '现存确诊', '治愈', '死亡', '无病例天数'])
    # 拿到所有的省份/直辖市的名称
    p_names = data['直辖市/省份'].unique()
    # 根据省份/直辖市的名称，筛选数据
    file = pd.ExcelWriter('l5_report.xlsx')
    for p_name in p_names:
        p_df = data[data.get('直辖市/省份') == p_name]

        # 保存当前省份数据到Excel，在省份名的sheet下

        p_df.to_excel(file, sheet_name=p_name, index=False)
    file.close()


process_data()
