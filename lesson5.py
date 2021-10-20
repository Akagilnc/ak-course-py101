import pandas as pd


def read_excel_from_file(file_name):
    data = pd.read_excel(file_name)
    return data


def process_data(infos):
    provinces = infos['直辖市省份'].unique()
    useful_col_names = ['直辖市省份', '城市地区', '现存确诊', '累计确诊', '治愈', '死亡', '无病例天数']
    with pd.ExcelWriter('l5_data.xlsx') as writer:
        for province in provinces:
            p_info = infos[infos.直辖市省份 == province]
            p_info[useful_col_names].to_excel(writer, sheet_name=province, index=False)


# data = read_excel_from_file('l4_report.xlsx')
# process_data(data)

data = pd.read_excel('l5_data.xlsx', sheet_name=None)
print(data)
