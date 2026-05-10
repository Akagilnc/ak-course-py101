import requests
import json


def get_data_from_api(address):
    data = requests.get(address).json()
    return data


def make_json_file(file_name, data):
    file = open(file_name, 'w', encoding='utf-8')
    json.dump(data, file, indent=4, ensure_ascii=False)
    file.close()


# data = get_data_from_api('http://127.0.0.1:8000/mock')
# make_json_file('lesson5.json', data)

def make_oversea_total_report(file_name):
    # 从文件读取数据
    file = open(file_name, encoding='utf-8')
    data = json.load(file).get('data').get('othertotal')
    # 提取我们需要的数据
    # 根据模版生成报告
    report = "海外疫情数据汇总： 累计确诊{} 现存确诊{} 死亡{} 治愈{}".format(data.get('certain'),
                                                                   data.get('ecertain'),
                                                                   data.get('die'),
                                                                   data.get('recure'))
    return report


# print(make_oversea_total_report('lesson5.json'))


def make_china_input_report(file_name):
    # 定义模版和结果集
    template = '中国： {}：境外输入{}例'
    results = []
    # 读取json文件并提取需要的数据
    file = open(file_name, encoding='utf-8')
    data = json.load(file).get('data').get('list')
    for info in data:
        # 生成报告
        temp_report = template.format(info.get('name'), info.get('jwsrNum'))
        # 保存
        results.append(temp_report)
    return results


reports = make_china_input_report('lesson5.json')
for info in reports:
    print(info)