# 数据bug
# 中国疫情地区详情
# 确诊排序
# 列名
# top10国家排名
import pandas as pd


# 数据bug修复
def fix_issues_from_boss():
    # 读取excel文件的亚洲sheet
    data = pd.read_excel('./excel_files/report.xlsx', sheet_name=None)
    # 初始化新的报告文件
    writer = pd.ExcelWriter('./excel_files/report_fixed.xlsx', engine='openpyxl')

    # 依次拿出所有的数据
    for key, df in data.items():
        if key == '亚洲':
            # 找到中国的地区信息
            df_china_details = df[(df['countryName'] == '中国') & (df['provinceName'] != '中国')]
            # 把它从原始数据中删除
            df = df.drop(df_china_details.index)
            df_china_details = df_china_details.sort_values(by='confirmedCount', ascending=False)
            df_china_details.to_excel(writer, sheet_name='中国', index=False)
        # 新的亚洲数据，保存到新的report
        df = df.sort_values(by='confirmedCount', ascending=False)
        df = df.rename(columns={'confirmedCount': '累计确诊', 'currentConfirmedCount': '现存确诊'})
        df.to_excel(writer, sheet_name=key, index=False)
    writer.save()


def make_top10_country():
    # 读取excel，读取多个sheet
    all_df_dict = pd.read_excel('./excel_files/report_fixed.xlsx', sheet_name=None)

    # 删除国家信息之外的数据，汇总和中国
    del all_df_dict['汇总']
    del all_df_dict['中国']
    # 确保top10这个sheet是唯一的
    if 'top10' in all_df_dict.keys():
        del all_df_dict['top10']
    # 整合数据
    all_df = pd.concat(all_df_dict, ignore_index=True)
    # 排序，找到top10的国家
    all_df = all_df.sort_values(by='累计确诊', ascending=False)
    top10_df = all_df.head(10)
    top10_df = top10_df.rename(columns={'countryName': '国家',
                                        'curedCount': '治愈',
                                        'deadCount': '死亡'})
    top10_df = top10_df.drop(columns=['provinceName', 'continentName'])
    # 保存到report_fixed里面去
    with pd.ExcelWriter('./excel_files/report_fixed.xlsx', engine='openpyxl', mode='a') as writer:
        top10_df.to_excel(writer, sheet_name='top10', index=False)


fix_issues_from_boss()
make_top10_country()
