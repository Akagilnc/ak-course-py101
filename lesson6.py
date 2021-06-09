import pandas as pd
import json


# 读取文件
def read_json_file(file_name):
    with open(file_name, encoding='utf-8') as file:
        return json.load(file)


def process_and_save_to_excel(file_names):
    sum_df = pd.DataFrame()
    with pd.ExcelWriter('l5_report.xlsx') as file:
        for filename in file_names:
            result = read_json_file('{}.json'.format(filename))
            content_df = pd.DataFrame(result, columns=['name', 'cureNum', 'deathNum', 'value'])
            content_df = content_df.rename(columns={'name': '名称', 'conNum': '确诊人数', 'cureNum': '治愈人数',
                                                    'deathNum': '死亡人数', 'value': '确诊人数'})
            cols = ['确诊人数', '治愈人数', '死亡人数']
            content_df = content_df.astype({'确诊人数': int, '治愈人数': int, '死亡人数': int})
            sum_info = content_df[cols].sum()
            sum_info = sum_info.rename('{} sum'.format(filename))
            sum_df = sum_df.append(sum_info)
            content_df.to_excel(file, index=False,
                                sheet_name=filename)
        sum_df.to_excel(file, sheet_name='SUM')


def make_top10_country():
    top_10_sheet_name = 'top10'
    # 讀取所有的sheet數據
    data = pd.read_excel('l5_report.xlsx', sheet_name=None)

    # 去掉不需要的sheet
    del data['SUM']
    # 確保我們的 top10 sheet 不存在
    if top_10_sheet_name in data.keys():
        del data[top_10_sheet_name]
    # 整合數據
    all_df = pd.concat(data, ignore_index=True)
    # 排序，找到Top10的國家
    print(all_df)
    all_df = all_df.sort_values(by='确诊人数', ascending=False)
    top_10_df = all_df.head(10)
    # 保存到report_fixed
    with pd.ExcelWriter('l5_report.xlsx', mode='a', engine='openpyxl') as writer:
        top_10_df.to_excel(writer, sheet_name=top_10_sheet_name, index=False)


process_and_save_to_excel(['l5_oversea_area_latest', 'l5_china_area_latest'])
make_top10_country()
