import pandas as pd
import json


# 读取json文件
def read_json_file(file_name):
    with open(file_name, encoding='utf-8') as file:
        return json.load(file)


def process_and_save_to_excel(file_names):
    with pd.ExcelWriter('l6_report.xlsx') as file:
        sum_df = pd.DataFrame()
        for name in file_names:
            result = read_json_file(name)
            data = pd.DataFrame(result, columns=[
                'name', 'value', 'econNum', 'cureNum', 'deathNum'
            ])
            columns = {'name': '名称', 'value': '累计确诊',
                       'econNum': '现存确诊', 'cureNum': '治愈人数',
                       'deathNum': '死亡人数'}
            data = data.rename(columns=columns)
            cols_to_sum = ['累计确诊', '现存确诊',
                           '治愈人数', '死亡人数']
            data = data.astype({'累计确诊': int, '现存确诊': int,
                                '治愈人数': int, '死亡人数': int})
            sum_info = data[cols_to_sum].sum()
            sum_info = sum_info.rename(name[:-5])
            sum_df = sum_df.append(sum_info)

            data.to_excel(file, index=False, sheet_name=name[:-5])
        print(sum_df)
        sum_df.to_excel(file, sheet_name='SUM')


def make_sp_area():
    all_df_dict = pd.read_excel(
        'l6_report.xlsx', sheet_name=None)
    del all_df_dict['SUM']
    print(all_df_dict.keys())
    if 'top10' in all_df_dict.keys():
        del all_df_dict['top10']
    all_df = pd.concat(all_df_dict, ignore_index=True)
    better_df = all_df[
        (all_df['累计确诊'] > 20000) & (all_df['现存确诊'] < 5000)]
    all_df = all_df.sort_values(by='累计确诊', ascending=False)
    top10_df = all_df.head(10)
    with pd.ExcelWriter('l6_report.xlsx', engine='openpyxl',
                        mode='a') as file:
        better_df.to_excel(file, sheet_name='缓解区',
                          index=False)


make_sp_area()
