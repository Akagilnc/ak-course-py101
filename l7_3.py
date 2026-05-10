import json
import pandas as pd


def make_report():
    # 读取json数据
    with open('lesson4.json', encoding='utf-8') as file:
        data = json.load(file).get('data').get('otherlist')
    # 整理数据
    data = pd.DataFrame(data, columns=['name', 'conNum', 'cureNum', 'deathNum'])
    data = data.astype({'conNum': int, 'cureNum': int, 'deathNum': int})
    data = data.rename(columns={'name': '国家/地区', 'conNum': '累计确诊',
                                'cureNum': '治愈人数', 'deathNum': '死亡人数'})
    data = data.set_index('国家/地区')
    # 计算死亡率和治愈率
    data['死亡率'] = data['死亡人数'] / data['累计确诊']
    data['治愈率'] = data['治愈人数'] / data['累计确诊']
    # 根据两个率排序，找到死亡率最低和治愈率最高的十条
    death_rate = data.sort_values(by=['死亡率', '治愈率']).head(10)
    cure_rate = data.sort_values(by='治愈率', ascending=False).head(10)
    # 写入报告
    with pd.ExcelWriter('l7_report.xlsx', mode='a', engine='openpyxl') as writer:
        death_rate.to_excel(writer, sheet_name='死亡率')
        cure_rate.to_excel(writer, sheet_name='治愈率')

make_report()
