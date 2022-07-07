import pandas as pd
import json


def read_json_file(file_name):
    with open(file_name, encoding='utf-8') as file:
        return json.load(file)


def process_and_save_to_excel(file_name):
    data = read_json_file('lesson3.json').get('data').get('otherlist')
    content_df = pd.DataFrame(data, columns=['name', 'conNum', 'cureNum', 'deathNum'])
    content_df = content_df.rename(columns={'name': '地区', 'conNum': '累计确诊',
                                            'cureNum': '治愈', 'deathNum': '死亡'})
    content_df = content_df.astype({'累计确诊': int, '治愈': int, '死亡': int})
    cols = ['累计确诊', '治愈', '死亡']
    content_df = content_df.set_index('地区')
    content_df = content_df.append(content_df[cols].sum().rename('合计'))
    content_df['差值'] = content_df['累计确诊'] - content_df['治愈']
    content_df['差值'] = content_df['差值'].astype(int)
    content_df.loc[content_df['差值'] >= 5000, '状态'] = '危险'
    content_df.loc[content_df['差值'] < 5000, '状态'] = '中等'
    content_df.loc[content_df['差值'] < 1000, '状态'] = '良好'
    content_df.loc[content_df['差值'] < 100, '状态'] = '优秀'
    content_df = content_df.sort_values(by='差值', ascending=False)
    content_df = content_df.drop(columns='差值')
    content_df = content_df[['治愈', '死亡', '状态']].groupby('状态').median()
    content_df = content_df.groupby('状态')[['治愈', '死亡', '状态']].median()
    content_df = content_df['状态'].value_counts()
    print(content_df)
    # with pd.ExcelWriter(file_name) as file:
    #     content_df.to_excel(file, sheet_name='oversea_area')


process_and_save_to_excel('l5_2.xlsx')