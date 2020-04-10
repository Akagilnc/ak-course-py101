import json
import pandas as pd


def read_china_area_data_from_json(file_name_with_path):
    with open(file_name_with_path, encoding='utf_8') as file:
        return json.load(file).get('data').get('list')


def save_to_excel(input_df, writer, sheet_name, index=False):
    input_df.to_excel(writer, index=index, sheet_name=sheet_name)
    writer.save()


def get_area_info(input_data):
    report = pd.ExcelWriter('lesson5_hw_report.xlsx', engine='openpyxl')
    sum_df = mean_df = mid_df = pd.DataFrame()
    sheet_names_stat = ['汇总', '均值', '中位数']
    df_list = [sum_df, mean_df, mid_df]
    for area_info in input_data:
        area_name = area_info.get('name')
        area_cities = area_info.get('city')
        df = pd.DataFrame(area_cities, columns=['name', 'conNum', 'cureNum',
                                                'deathNum', 'econNum', 'zerodays'])

        columns_need_to_be_int_names = ['conNum', 'cureNum', 'deathNum', 'econNum', 'zerodays']
        df = df[columns_need_to_be_int_names].astype('int')

        df_list = rename_and_append(df, area_name, df_list)

        save_to_excel(df, report, area_name)

    for index, df in enumerate(df_list):
        save_to_excel(df, report, sheet_names_stat[index], True)


def rename_and_append(df, area_name, df_list):
    series_list = [df.sum(), df.mean(), df.median()]
    for index, info in enumerate(series_list):
        info = info.rename(area_name)
        df_list[index] = df_list[index].append(info)
    return df_list


data = read_china_area_data_from_json('lesson4.json')
get_area_info(data)
