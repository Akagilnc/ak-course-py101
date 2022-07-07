import json
import pandas as pd


def process_data():
    # 读取json数据
    with open('l3.json', encoding='utf-8') as file:
        data = json.load(file).get('data').get('list')
    # 转换df
    df = pd.DataFrame(data, columns=['name', 'zerodays'])
    df = df.rename(columns={'name': '直辖市/省份', 'zerodays': '无病例天数'})
    df.loc[df.get('无病例天数') == '', '无病例天数'] = 0

    df = df.astype({'无病例天数': int})

    # 筛选省份为香港/澳门的数据
    df_hm = df[df.get('直辖市/省份').isin(['香港', '澳门'])]
    # 筛选无病例天数为空的数据，并改写为0
    print(df_hm)


process_data()