def make_dict(file_name):
    # 读取信息，依次拿出
    file = open(file_name)
    data = file.readlines()
    for info in data:
        # 切数据，处理数据
        name, age, sex, depart = info.split(', ')
        # 生成字典
        temp = {'name': name, 'age': int(age), 'sex': sex, 'depart': depart.strip()}
        # 打印
        if temp.get('age') > 30:
            print(temp)


# make_dict('hr.txt')


import json
def make_oversea_report(file_name):
    template = '截止今日，海外疫情汇总 累计确诊{} 死亡{} 治愈{}'
    # 从json文件读取数据
    file = open(file_name, encoding='utf-8')
    data = json.load(file)
    data = data.get('data').get('othertotal')
    report = template.format(data.get('certain'), data.get('die'), data.get('recure'))
    print(report)


# make_oversea_report('l3.json')


def print_kids_name():
    temp = {'name': 'Curry', 'age': '32', 'kids': [{'name': 'Riley'}, {'name': 'Canon'}, {'name': 'Ryan'}]}
    temp = temp.get('kids')
    for kid in temp:
        print(kid.get('name'))


# print_kids_name()

def make_china_input_report(file_name):
    template = '中国： {}：境外输入{}例\n'
    results = []
    # 读取数据
    file = open(file_name, encoding='utf-8')
    data = json.load(file).get('data').get('list')
    # 寻找中国直辖市省份数据
    for province in data:
        # 生成报告
        p_report = template.format(province.get('name'), province.get('jwsrNum'))
        results.append(p_report)
    # 存储到文件
    file = open('l5_report.txt', 'w', encoding='utf-8')
    file.writelines(results)
    file.close()


make_china_input_report('l3.json')
