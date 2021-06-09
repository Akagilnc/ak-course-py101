import json
import pandas as pd


# 读取文件
def read_json_file(file_name):
    with open(file_name, encoding='utf-8') as file:
        return json.load(file)


def process_and_save_to_excel(filename):
    sum_df = pd.DataFrame()
    with pd.ExcelWriter('l5_report.xlsx') as file:
        result = read_json_file('{}.json'.format(filename))
        content_df = pd.DataFrame(result)
        cols = ['conNum', 'cureNum', 'deathNum']
        content_df = content_df.astype({'conNum': int, 'cureNum': int, 'deathNum': int})
        sum_df = sum_df.append(content_df[cols].sum(), ignore_index=True)
        content_df.to_excel(file, index=False,
                            sheet_name=filename)
        sum_df.to_excel(file, index=False, sheet_name='SUM')


file_names = [
    'l5_china_area_latest',
    'l5_oversea_history',
    'l5_oversea_area_latest',
    'l5_china_history',
    'l5_world_area_latest'
]
process_and_save_to_excel('l5_oversea_area_latest')
