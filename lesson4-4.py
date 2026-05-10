import json
import pandas
def read_json():
    file = open('l3.json', encoding='utf-8')
    data = json.load(file)
    return data
def get_df(data):
    data = data.get('data').get('otherlist')
    results = []
    for info in data:
        result = {'国家/地区': info.get('name'), '代码': info.get('citycode'),
                  '现存确诊': info.get('econNum'), '确诊新增': info.get('conadd'),
                  '治愈': info.get('cureNum'), '治愈新增': info.get('cureadd'),
                  '死亡':info.get('deathNum'), '死亡新增': info.get('deathadd')}
        results.append(result)
    df = pandas.DataFrame(results)
    df = df.astype({'现存确诊': int, '确诊新增': int})
    return df
def write_to_excel(file_name, df):
    df.to_excel(file_name, index=False, sheet_name='报告')
data = read_json()
df = get_df(data)
write_to_excel('l4_report.xlsx', df)