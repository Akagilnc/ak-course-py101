import json
import pandas as pd
import os


def get_data_from_json(file_name):
    with open(file_name, encoding='utf_8') as file:
        return json.load(file)


def save_data_to_excel():
    filenames = os.listdir('./json_files')
    writer = pd.ExcelWriter('./excel_files/report.xlsx', engine='openpyxl')
    sum_df = pd.DataFrame()
    for name in filenames:
        # 从 文件名中截取洲名
        tag_name = name[:name.index('.')]
        # 将文件名添加上路径，用于读取json文件
        file_name = './json_files/{}'.format(name)
        # 从json文件中获取数据
        data_json = get_data_from_json(file_name)

        # 将数据转换为DataFrame，并指定需要的columns
        df = pd.DataFrame(data_json, columns=['locationId', 'continentName', 'continentEnglishName',
                                              'countryName', 'countryEnglishName', 'provinceName',
                                              'provinceEnglishName', 'provinceShortName', 'currentConfirmedCount',
                                              'confirmedCount', 'suspectedCount', 'curedCount', 'deadCount', 'comment'])

        # 生成汇总信息，rename为洲名-汇总并存储到DateFrame里面
        sum_info = df[['currentConfirmedCount', 'confirmedCount',
                       'suspectedCount', 'curedCount', 'deadCount']].sum()
        sum_info = sum_info.rename('{}-汇总'.format(tag_name))
        sum_df = sum_df.append(sum_info)

        # 保存到独立的文件
        df.to_excel('./excel_files/{}.xlsx'.format(tag_name), index=False)
        df.to_csv('./csv_files/{}.csv'.format(tag_name), index=False)

        # 保存到report文件的独立sheet
        df.to_excel(writer, sheet_name=tag_name, index=False)

    # 保存汇总信息到汇总sheet
    sum_df.to_excel(writer, sheet_name='汇总', index=False)
    sum_df.to_csv('./csv_files/report.csv', index=False)

    writer.save()


save_data_to_excel()
