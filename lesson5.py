import json
import pandas as pd
import os


# 讀取指定路徑文件的json數據
def read_json_file(filename):
    with open(filename, encoding='utf_8') as file:
        return json.load(file)


# 處理並保持數據到excel
def process_and_save_to_excel():
    # 初始化一個匯總的空的結果集
    sum_df = pd.DataFrame()
    # 獲取目錄下所有的文件名
    file_names = os.listdir('./json_files/')
    with pd.ExcelWriter('./excel_files/report.xlsx', engine='openpyxl') as writer:
        for file_name in file_names:
            sheet_name = file_name[:-5]
            # 獲取數據
            path_name = './json_files/{}'.format(file_name)
            data = read_json_file(path_name)
            # 轉化到pandas的數據結構，DataFrame
            contents_df = pd.DataFrame(data, columns=['continentName', 'countryName', 'provinceName',
                                                      'currentConfirmedCount', 'confirmedCount',
                                                      'curedCount', 'deadCount'])

            # 保存json數據到excel
            contents_df.to_excel(writer, sheet_name=sheet_name, index=False)

            # 獲得匯總數據
            columns = ['currentConfirmedCount', 'confirmedCount',
                       'curedCount', 'deadCount']
            sum_info = contents_df[columns].sum()
            sum_info = sum_info.rename('{} sum'.format(sheet_name))
            # 添加到匯總DF裏面
            sum_df = sum_df.append(sum_info)

        # 保存匯總數據到excel
        sum_df.to_excel(writer, sheet_name='SUM')


process_and_save_to_excel()
