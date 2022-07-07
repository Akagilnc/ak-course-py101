import json
import pandas as pd


def process_data():
    with open('l3.json', encoding='utf-8') as file:
        data = json.load(file).get('data').get('list')
    useful_list = ['name', 'value', 'econNum', 'cureNum', 'deathNum', 'zerodays']
    data = pd.DataFrame(data, columns=useful_list)
    data = data.astype({'value': int, 'econNum': int, 'cureNum': int, 'deathNum': int})

    # temp_data = data.get(['name', 'value'])
    # temp_data = data.head(10)
    # temp_data2 = data.tail(10)

    # temp_data = data[data.get('value') > 100]
    # temp_data = data[data.get('name').isin(['香港', '澳门'])]
    # data = data[data.get('zerodays').notna() & (data.get('zerodays') != '')]

    # temp_data = data.loc[data.get('deathNum') > 10, ['name', 'deathNum']]
    # temp_data = data.iloc[9:20, 0:5]

    data.loc[data.get('zerodays') == '', 'zerodays'] = -1
    data = data.astype({'zerodays': int})

    # data['死亡率'] = data['deathNum'] / data['value']
    # data['治愈率'] = data['cureNum'] / data['value']

    data['差值'] = data['value'] - data['cureNum']
    data.loc[data.get('差值') >= 1000, '状态'] = '危险'
    data.loc[data.get('差值') < 1000, '状态'] = '中等'
    data.loc[data.get('差值') < 50, '状态'] = '良好'
    data.loc[data.get('差值') < 10, '状态'] = '优秀'

    data = data.drop(columns='差值')
    data = data.sort_values(by=['econNum', 'value'], ascending=False)

    temp_data = data[['value', 'cureNum', '状态']].groupby('状态').sum()
    temp_data = data[['value', 'cureNum', '状态']].groupby('状态').mean()
    temp_data = data[['value', 'cureNum', '状态']].groupby('状态').median()

    temp_data = data.get('状态').value_counts()
    print(temp_data)


process_data()