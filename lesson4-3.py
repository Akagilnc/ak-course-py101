import json
def read_from_json():
    file = open('l3.json', encoding='utf-8')
    return json.load(file)
def get_results(data):
    data = data.get('data').get('list')
    template = '{}： 无病例最长 {} 天 现存确诊{}，治愈{}，死亡{}\n'
    results = []
    for info in data:
        result = template.format(info.get('name'), info.get('zerodays'),
                        info.get('econNum'),
                        info.get('cureNum'), info.get('deathNum'))
        results.append(result)
    return results
def write_to_file(file_name, data):
    file = open(file_name, 'w', encoding='utf-8')
    file.writelines(data)
    file.close()

data = read_from_json()
results = get_results(data)
write_to_file('l4_report2.txt', results)
