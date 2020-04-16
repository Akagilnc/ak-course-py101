# 数据bug问题，亚洲数据
# 中国疫情地区数据
# 确诊人数，排序，从到高低
# 改变成比较好理解的列名
# top10国家sheet
import pandas as pd


def fix_issues_from_boss():
    # 读取亚洲的数据
    data = pd.read_excel('./excel_files/report.xlsx', sheet_name=None, engine='openpyxl')
    # 初始化新的报告文件
    writer = pd.ExcelWriter('./excel_files/report_fixed.xlsx', engine='openpyxl')
    # 依次拿到所有sheet的数据。
    for key, df in data.items():
        df = df.rename(columns={'confirmedCount': '累计确诊', 'curedCount': '治愈',
                                'currentConfirmedCount': '当前确诊', 'deadCount': '死亡'})
        if key == '亚洲':
            # 找到中国的地区数据
            df_china_details = df[(df['countryName'] == '中国') & (df['provinceName'] != '中国')]
            # 从亚洲数据里面，删除中国的地区数据
            df = df.drop(df_china_details.index)
            # 把中国地区数据存入excel
            df_china_details = df_china_details.sort_values(by='累计确诊', ascending=False)
            df_china_details.to_excel(writer, sheet_name='中国', index=False)

        # 保存进新的report, 按照累计确诊排序
        df = df.sort_values(by='累计确诊', ascending=False)
        df.to_excel(writer, sheet_name=key, index=False)

    writer.save()


def make_top10_country():
    # 读取所有的sheet
    all_df_dict = pd.read_excel('./excel_files/report_fixed.xlsx', sheet_name=None, engine='openpyxl')

    # 去掉不需要的sheet 汇总和中国
    del all_df_dict['汇总']
    del all_df_dict['中国']
    # 确保top10sheet是不存在
    if 'top10' in all_df_dict.keys():
        del all_df_dict['top10']
    # 整合数据
    all_df = pd.concat(all_df_dict, ignore_index=True)
    # 排序，找到top10的国家
    all_df = all_df.sort_values(by='累计确诊', ascending=False)
    top_10_df = all_df.head(10)
    # 保存回report_fixed
    writer = pd.ExcelWriter('./excel_files/report_fixed.xlsx', engine='openpyxl', mode='a')
    top_10_df.to_excel(writer, sheet_name='top10', index=False)
    writer.save()


fix_issues_from_boss()
make_top10_country()
