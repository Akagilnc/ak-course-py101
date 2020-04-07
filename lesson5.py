import json
import pandas as pd
import os


# 读取json文件的数据
def read_json_file(file_name):
    with open(file_name, encoding='utf_8') as file:
        return json.load(file)


# 把数据依次的存储到excel里
def save_to_excel():
    # 获取文件名
    file_names = os.listdir('./json_files')
    # 初始化汇总的信息
    sum_df = pd.DataFrame()
    # 生成我们最终要保存的excel
    with pd.ExcelWriter('./excel_files/report.xlsx', engine='openpyxl') as excel_file:
        for file_name in file_names:
            # 抓取大洲的名字
            sheet_name = file_name[:-5]
            # 获取json的信息
            file_name = './json_files/{}'.format(file_name)
            data = read_json_file(file_name)

            # 转换json到pandas.DataFrame
            columns_names = ['continentName', 'countryName', 'provinceName', 'currentConfirmedCount',
                             'confirmedCount', 'curedCount', 'deadCount']
            df = pd.DataFrame(data, columns=columns_names, index=range(1, len(data)+1))
            sum_columns_list = ['currentConfirmedCount', 'confirmedCount', 'curedCount', 'deadCount']
            # 从原始的df选出四列，求和
            sum_info = df[sum_columns_list].sum()
            # 给sum_info 取了个名字，大洲名字+汇总
            sum_info = sum_info.rename('{}汇总'.format(sheet_name))
            sum_df = sum_df.append(sum_info)
            # 保存到excel文件
            df.to_excel(excel_file, index=True, sheet_name=sheet_name)

        sum_df.to_excel(excel_file, sheet_name='汇总')
        string_sum = sum_df.to_string()
        with open('report.txt', 'w', encoding='utf-8') as file:
            file.write(string_sum)


save_to_excel()
