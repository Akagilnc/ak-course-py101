# 数据bug
# 中国疫情地区详情
# 确诊排序
# top10国家排名
# 列名
import pandas as pd


def sort_by_column(data, column_name, ascending=False):
    return data.sort_values(by=column_name, ascending=ascending)


def save_to_excel(data, sheet_name, writer, index_flag=False):
    data.to_excel(writer, sheet_name=sheet_name, index=index_flag)
    writer.save()


# BUG 修复
def fix_issue_from_boss():
    # 读取excel文件，并且读取亚洲sheet
    data = pd.read_excel('./excel_files/report.xlsx', sheet_name=None)
    # 初始化报告文件
    writer = pd.ExcelWriter('./excel_files/report_fixed.xlsx', engine='openpyxl')

    # 依次读取每一个sheet的信息
    for name, df in data.items():
        sort_by_column_name = 'confirmedCount'
        if name == '亚洲':
            # 找到中国的地区信息，并且从原始数据中删除
            data_china_details = df[(df['countryName'] == '中国') & (df['provinceName'] != '中国')]
            # 生成新的亚洲数据
            df = df.drop(data_china_details.index)  # 常用的，删除行和列的用法
            # 排序并保存中国数据到excel
            data_china_details = sort_by_column(data_china_details, sort_by_column_name)
            save_to_excel(data_china_details, '中国', writer)

        # 对已经生成好的df按照confirmedCount排序
        df = sort_by_column(df, sort_by_column_name)
        save_to_excel(df, name, writer)
    writer.close()


def make_top10_country():
    # 读取excel文件，读取多个sheet。
    all_df = pd.read_excel('./excel_files/report_fixed.xlsx', sheet_name=None)
    # 删除国家信息之外的sheet信息
    del all_df['汇总']
    del all_df['中国']
    # 确保每次生成的‘top10'为唯一
    if 'top10' in all_df.keys():
        del all_df['top10']
    # 整和数据
    all_df = pd.concat(all_df, ignore_index=True)
    # 排序，并且找到top10的国家
    all_df = sort_by_column(all_df, 'confirmedCount')
    top10_df = all_df.head(10)
    top10_df = top10_df.rename(columns={'confirmedCount': '累计确诊', 'currentConfirmedCount': '现存确诊',
                                        'curedCount': '治愈人数', 'deadCount': '死亡人数',
                                        'countryName': '国家'})
    top10_df = top10_df.drop(columns=['provinceName', 'continentName'])
    top10_df = top10_df.set_index('国家')

    # 保存到report里面去
    with pd.ExcelWriter('./excel_files/report_fixed.xlsx', engine='openpyxl', mode='a') as writer:
        save_to_excel(top10_df.T, 'top10', writer, True)


fix_issue_from_boss()
make_top10_country()
