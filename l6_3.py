import pandas as pd
import json


def make_data():
    data = json.load(open('l3.json', encoding='utf-8')).get('data').get('otherlist')
    df = pd.DataFrame(data, columns=['name', 'conNum', 'cureNum'])
    df = df.astype({'conNum': 'int', 'cureNum': 'int'})
    df['差值'] = df['conNum'] - df['cureNum']
    df.loc[df.get('差值') >= 1000, '状态'] = '危险'
    df.loc[df.get('差值') < 1000, '状态'] = '中等'
    df.loc[df.get('差值') < 500, '状态'] = '良好'
    df.loc[df.get('差值') < 100, '状态'] = '优秀'
    print(df)

make_data()