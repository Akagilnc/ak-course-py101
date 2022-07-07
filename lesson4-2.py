import json
def read_json():
    file = open('l3.json', encoding='utf-8')
    data = json.load(file)
    return data
def get_results(data):
    data = data.get('data').get('otherlist')
    template = '{}： 确诊{} 确诊新增{} 累计确诊{}，治愈{} 治愈新增{}，死亡{} 死亡新增{}\n'
    results = []
    for info in data:
        result = template.format(info.get('name'), info.get('econNum'),
                                 info.get('conadd'), info.get('conNum'),
                                 info.get('cureNum'), info.get('cureadd'),
                                 info.get('deathNum'), info.get('deathadd'))
        results.append(result)
    return results
def write_to_file(file_name, data):
    file = open(file_name, 'w', encoding='utf-8')
    file.writelines(data)
    file.close()
data = read_json()
results = get_results(data)
write_to_file('l4_report.txt', results)