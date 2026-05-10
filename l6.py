import json
import pandas as pd


def write_to_file(file_name, infos):
    file = open(file_name, 'w', encoding='utf-8')
    file.writelines(infos)
    file.close()


def make_oversea_report(file_name):
    # 读取json文件，找到相应海外国家/地区数据
    file = open(file_name, encoding='utf-8')
    data = json.load(file).get('data').get('otherlist')
    data = pd.DataFrame(data, columns=['name', 'citycode', 'econNum', 'conadd', 'cureNum',
                                       'cureadd', 'deathNum', 'deathadd'])
    data = data.rename(columns={'name': '国家/地区', 'econNum': '现存确诊', 'conadd': '确诊新增',
                                'cureNum': '治愈人数', 'cureadd': '治愈新增',
                                'deathNum': '死亡人数', 'deathadd': '死亡新增'})
    data = data.astype({'现存确诊': int})
    data.to_excel('l6_report.xlsx', index=False)


make_oversea_report('l3.json')
