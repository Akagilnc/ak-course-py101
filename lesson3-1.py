import requests as req
import json
def call_api(address):
    data = req.get(address)
    return data.json()

# data = call_api('http://127.0.0.1:8080/mock')
def write_to_file(file_name, infos):
    file = open(file_name, 'w', encoding='utf-8')
    json.dump(infos, file, indent=4, ensure_ascii=False)

# write_to_file('l3.json', data)
#
# # 自带电脑连我的Wi-Fi AK 密码11223344aa
# address = 'http://192.168.50.142:8080/mock'
# # 教室电脑：
# address = 'http://192.168.5.104:8080/mock'


def read_and_make():
    file = open('l3.json', encoding='utf-8')
    data = json.load(file)
    data = data.get('data').get('othertotal')
    template = '截止今日，海外疫情确诊总人数达到{}人，治愈{}人，死亡{}人。当日新增确诊达{}人'
    print(template.format(data.get('certain'), data.get('recure'), data.get('die'),
                          data.get('ecertain_inc').strip('+')))


read_and_make()

