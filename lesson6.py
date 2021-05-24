# 数据bug问题，亚洲数据
# 中国疫情地区数据
# 确诊人数，排序，从高到低
# 改变成比较好理解的列名
# top10国家sheet
import pandas as pd


def fix_issues_from_boss():
    # 讀取所有的數據
    data = pd.read_excel('./excel_files/report.xlsx', sheet_name=None, engine='openpyxl')
    # 初始化一個新的報告文件
    writer = pd.ExcelWriter('./excel_files/report_fixed.xlsx', engine='openpyxl')
    # 依次拿到每一個sheet的數據
    for key, df in data.items():
        # 改列名
        df = df.rename(columns={'confirmedCount': '纍計確診', 'curedCount': '治愈',
                                'currentConfirmedCount': '當前確診', 'deadCount': '死亡'})
        # 如果是亞洲的數據
        if key == 'Asia':
            # 找到中國的地區數據
            df_china_area = df[(df['countryName'] == '中国') & (df['provinceName'] != '中国')]
            # 從亞洲的數據裏面，刪除中國的地區數據
            df = df.drop(df_china_area.index)
            # 把中國的地區數據，保存到一個sheet
            df_china_area = df_china_area.sort_values(by='纍計確診', ascending=False)
            df_china_area.to_excel(writer, sheet_name='China', index=False)
        # 保存到新的report
        df = df.sort_values(by='纍計確診', ascending=False)
        df.to_excel(writer, sheet_name=key, index=False)

    writer.save()


def make_top10_country():
    top_10_sheet_name = 'top10'
    # 讀取所有的sheet數據
    data = pd.read_excel('./excel_files/report_fixed.xlsx', sheet_name=None, engine='openpyxl')

    # 去掉不需要的sheet
    del data['SUM']
    del data['China']
    # 確保我們的 top10 sheet 不存在
    if top_10_sheet_name in data.keys():
        del data[top_10_sheet_name]
    # 整合數據
    all_df = pd.concat(data, ignore_index=True)
    # 排序，找到Top10的國家
    all_df = all_df.sort_values(by='纍計確診', ascending=False)
    top_10_df = all_df.head(10)
    # 保存到report_fixed
    with pd.ExcelWriter('./excel_files/report_fixed.xlsx', engine='openpyxl', mode='a') as writer:
        top_10_df.to_excel(writer, sheet_name=top_10_sheet_name, index=False)


fix_issues_from_boss()
make_top10_country()
