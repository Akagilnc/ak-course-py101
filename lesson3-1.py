import requests
import json


def call_api(address):
    resp = requests.get(address)
    return resp.json()


def write_to_json(filename, data):
    file = open(filename, 'w', encoding='utf-8')
    json.dump(data, file, indent=4, ensure_ascii=False)
    file.close()

# # 自带电脑连我的Wi-Fi AK 密码11223344aa
# address = 'http://192.168.47.142:8080/mock'
# # 教室电脑：
# # address = 'http://192.168.5.245:8000/mock'
#
# data = call_api(address)
# write_to_json('l3.json', data)


def read_and_make():
    # 读取json文件
    file = open('l3.json', encoding='utf-8')
    data = json.load(file)
    # 获取海外疫情汇总数据
    data = data.get('data').get('othertotal')
    # 生成报告
    temp = "海外疫情：累计确诊{} 现存确诊{} 死亡{} 死亡变化{} 治愈{} 治愈变化{}"
    # 打印
    print(temp.format(data.get('certain'), data.get('ecertain'),
                      data.get('die'), data.get('die_inc'),
                      data.get('recure'), data.get('recure_inc')))


read_and_make()
