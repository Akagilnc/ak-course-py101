import requests
import json


def call_api(address):
    resp = requests.get(address)
    with open('l3.json', 'w', encoding='utf-8') as file:
        json.dump(resp.json(), file,
                  indent=4, ensure_ascii=False)


# 教室内网机器
call_api('http://192.168.5.245:8080/mock')
# 请连我的Wi-Fi AK 11223344aa
call_api('http://192.168.78.142:8080/mock')


# def read_and_print():
#     with open('l3.json', encoding='utf-8') as file:
#         infos = json.load(file)
#
#     data = infos.get('data').get('othertotal')
#     report = '截止今日，海外疫情 确诊{}，较昨日{}，死亡{}，较昨日{}，治愈{}，较昨日{}'
#     report = report.format(
#         data.get('certain'), data.get('certain_inc'),
#         data.get('die'), data.get('die_inc'),
#         data.get('recure'), data.get('recure_inc')
#     )
#     return report
#
#
# print(read_and_print())

