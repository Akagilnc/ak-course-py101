import requests
import json
# 调用远程API的函数，远程的数据保存到我本地的一个json文件
def call_api(address):
    # 调用API拿到数据
    resp = requests.get(address)
    # 保存到文件（打开，保存，关闭）
    with open('l3.json', 'w', encoding='utf-8') \
            as file:
        json.dump(resp.json(), file, indent=4, 
                  ensure_ascii=False)


# 读取json文件，获得海外疫情的汇总数据，打印到屏幕
def read_and_print():
    # 读取文件：打开，读取，关闭
    with open('l3.json', encoding='utf-8') as file:
        infos = json.load(file)
    # 找到我们需要的海外疫情汇总数据
    data = infos.get('data').get('list')
    # 打印： 截止今日，海外疫情 确诊 较昨日， 死亡 较昨日， 治愈 较昨日
    report = '截止今日，海外疫情 确诊{} 较昨日{}， 死亡{} 较昨日{}， 治愈{} 较昨日{}'
    report = report.format(
        data.get('certain'), data.get('certain_inc'),
        data.get('die'), data.get('die_inc'),
        data.get('recure'), data.get('recure_inc')
    )
    # for info in data:
    #     print(info.get('name'), info.get('value'))
    #     cities = info.get('city')
    #     for city in cities:
    #         print(city.get('name'), city.get('conNum'))
    #     print('===================')
read_and_print()


