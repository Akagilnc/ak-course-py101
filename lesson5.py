import json
import pandas as pd
import os


# 读取指定路径文件的json数据
def read_json_data(file_name):
    with open(file_name, encoding='utf_8') as file:
        return json.load(file)


# 保存数据到excel
def process_and_save_data_to_excel():
    # 初始化一个汇总的空的DataFrame
    sum_df = pd.DataFrame()
    file_names = os.listdir('./json_files/')
    with pd.ExcelWriter('./excel_files/report.xlsx', engine='openpyxl') as writer:
        for file_name in file_names:
            sheet_name = file_name[:-5]
            path_name = './json_files/{}'.format(file_name)
            # 获取data
            data = read_json_data(file_name=path_name)
            # 保存到report.xlsx的文件里
            # 转换data到pandas的DataFrame
            contents = pd.DataFrame(data, columns=['continentName', 'countryName', 'provinceName',
                                                   'currentConfirmedCount', 'confirmedCount', 'curedCount',
                                                   'deadCount'])
            # 获得汇总数据
            sum_info = contents[['currentConfirmedCount', 'confirmedCount',
                                 'curedCount', 'deadCount']].sum()
            print(sum_info)
            sum_info = sum_info.rename('{}汇总'.format(sheet_name))
            print(sum_info)
            sum_df = sum_df.append(sum_info)
            # 添加到汇总DF里面
            contents.to_excel(writer, index=False, sheet_name=sheet_name)
        # 把汇总的df写入excel
        sum_df.to_excel(writer, sheet_name='汇总')


process_and_save_data_to_excel()
