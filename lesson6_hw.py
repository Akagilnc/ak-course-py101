# 作业
# 根据L5课堂上生成的excel报告，用Python实现如下操作：
#
# 1. 删除不需要的continentName列，并提取出中国的数据，重新生成亚洲和中国两个sheet；
#
# 2. 在中国sheet里面保留provinceName，删除countryName，在除中国和汇总以外的列，删除provinceName, 保留countryName；
#
# 3. 将所有sheet的列名修改为：
# {'confirmedCount': '累计确诊',
# 'currentConfirmedCount': '现存确诊',
# 'curedCount': '治愈人数',
# 'deadCount': '死亡人数',
# 'countryName': '国家', 'provinceName': '省份/直辖市'}
#
# 附加题1： 生成一个重灾区sheet，保存所有累计确诊人数 > 50000 的国家数据
# 附加题2： 生成一个观察区sheet，保存所有累计确诊人数 > 20000, 且治愈人数 < 10000的国家数据
# 附加题3： 生成一个 缓解区sheet，保存所有累计确诊人数 > 20000, 但现存确诊人数比累计确诊人数 少2万以上的国家数据

import pandas as pd


def get_report_from_lesson5():
    data = pd.read_excel('./excel_files/report.xlsx', sheet_name=None)
    writer = pd.ExcelWriter('./excel_files/lesson6_hw.xlsx', engine='openpyxl')
    for key, df in data.items():
        if key == '亚洲':
            df_china_details = df[(df['countryName'] == '中国') & (df['provinceName'] != '中国')]
            df = df.drop(df_china_details.index)
            df_china_details = df_china_details.drop(columns=['countryName', 'continentName'])
            df_china_details = rename_columns(df_china_details, is_china=True)
            df_china_details.to_excel(writer, sheet_name='中国', index=False)
        if key != '汇总':
            df = df.drop(columns=['provinceName', 'continentName'])
            df = rename_columns(df)
        df.to_excel(writer, sheet_name=key, index=False)
    writer.save()


def rename_columns(df, is_china=False):
    key, value = ('provinceName', '省份直辖市') if is_china else ('countryName', '国家')
    df = df.rename(columns={key: value,
                            'currentConfirmedCount': '现存确诊',
                            'confirmedCount': '累计确诊',
                            'curedCount': '治愈人数',
                            'deadCount': '死亡人数'})

    return df


def make_worse_country():
    # 读取所有的sheet
    all_df_dict = pd.read_excel('./excel_files/lesson6_hw.xlsx', sheet_name=None, engine='openpyxl')

    # 去掉不需要的sheet 汇总和中国
    del all_df_dict['汇总']
    del all_df_dict['中国']
    # 整合数据
    all_df = pd.concat(all_df_dict, ignore_index=True)
    # 排序
    all_df = all_df.sort_values(by='累计确诊', ascending=False)
    worse_df = all_df[all_df['累计确诊'] > 50000]
    observe_df = all_df[(all_df['累计确诊'] > 20000) & (all_df['治愈人数'] < 10000)]
    better_df = all_df[(all_df['累计确诊'] > 20000) & ((all_df['累计确诊'] - all_df['现存确诊']) > 20000)]

    # 保存回report_fixed
    writer = pd.ExcelWriter('./excel_files/lesson6_hw.xlsx', engine='openpyxl', mode='a')
    worse_df.to_excel(writer, sheet_name='重灾区', index=False)
    observe_df.to_excel(writer, sheet_name='观察区', index=False)
    better_df.to_excel(writer, sheet_name='缓解区', index=False)
    writer.save()


get_report_from_lesson5()
make_worse_country()
