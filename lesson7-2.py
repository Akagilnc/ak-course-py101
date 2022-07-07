import pandas as pd
import json


def process_data():
    # 读取json数据
    with open('l3.json', encoding='utf-8')as file:
        data = json.load(file).get('data').get('otherlist')
    # 转换为df
    df = pd.DataFrame(data, columns=['name', 'conNum', 'cureNum', 'deathNum'])
    df = df.astype({'conNum': int, 'cureNum': int, 'deathNum': int})
    df = df.rename(columns={'name': '国家/地区', 'conNum': '累计确诊',
                            'cureNum':'治愈', 'deathNum':'死亡'})
    df = df.set_index('国家/地区')
    # 插入死亡率和治愈率
    df['死亡率'] = df.get('死亡') / df.get('累计确诊')
    df['治愈率'] = df.get('治愈') / df.get('累计确诊')
    # 获得死亡率最低的10条
    df_death_rate = df.sort_values(by='死亡率')
    df_death_rate.style.format({'死亡率': '{:,.2%}'.format})
    print(df_death_rate.head(10))
    # 获得治愈率最高的10条
    df_cure_rate = df.sort_values(by='治愈率', ascending=False)
    df_cure_rate.style.format({'治愈率': '{:,.2%}'.format})
    print(df_cure_rate.head(10))


process_data()
