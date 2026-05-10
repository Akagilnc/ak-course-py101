import pandas as pd

def make_report():
    sum_df = pd.DataFrame()
    file = pd.ExcelWriter('l6_report.xlsx')
    use_cols = ['现存确诊', '累计确诊', '治愈', '死亡']
    # 读取excel数据
    data = pd.read_excel('l5_data.xlsx')
    sum_data = data[use_cols].sum()
    sum_data = sum_data.rename('汇总')
    sum_df = sum_df.append(sum_data)
    # 获取直辖市/省份的值
    p_names = data['直辖市/省份'].unique()
    # 筛选数据，并汇总
    for p_name in p_names:
        p_df = data[data.get('直辖市/省份') == p_name]
        p_df = p_df.set_index('直辖市/省份')
        p_sum_data = p_df[use_cols].sum()
        p_sum_data = p_sum_data.rename('{}汇总'.format(p_name))
        p_df = p_df.append(p_sum_data)
        # 写入数据
        p_df.to_excel(file, sheet_name=p_name)
    sum_df.to_excel(file, sheet_name='汇总')
    file.save()


make_report()