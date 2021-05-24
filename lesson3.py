import requests
import json


# 调用远程API的函数，远程的数据保存到我本地的一个json文件
def call_api_and_save_to_file(api_address, file_name):
    # 调用API拿到数据
    response = requests.get(api_address)
    # 保存到文件（打开，保存，关闭）
    with open(file_name, 'w', encoding='utf_8') as file:
        json.dump(response.json(), file, indent=4, ensure_ascii=False)


# 读取json文件，获得海外疫情的汇总数据，打印到屏幕
def read_and_process(file_name):
    # 读取文件：打开，读取，关闭
    with open(file_name, encoding='utf_8') as file:
        data = json.load(file)
    # 找到我们需要的海外疫情汇总数据
    infos = data.get('data').get('othertotal')
    # 打印： 截止今日，海外疫情 确诊 较昨日， 死亡 较昨日， 治愈 较昨日
    template = '截止今日，海外疫情 确诊{} 较昨日{}， 死亡{} 较昨日{}， 治愈{} 较昨日{}'
    print(template.format(
        infos.get('certain'), infos.get('certain_inc'),
        infos.get('die'), infos.get('die_inc'),
        infos.get('recure'), infos.get('recure_inc')
    ))


address = 'https://interface.sina.cn/news/wap/fymap2020_data.d.json'
# call_api_and_save_to_file(address, 'lesson3.json')
read_and_process('lesson3.json')

