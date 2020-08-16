import json
import requests as req


# 调用api获得最新的疫情数据。
def call_api_and_save_to_file():
    # 调用api
    data = req.get('https://interface.sina.cn/news/wap/fymap2020_data.d.json')
    # 打开/保存/关闭 目标文件lesson4.json
    with open('lesson4.json', 'w', encoding='utf_8') as file:
        json.dump(data.json(), file, ensure_ascii=False, indent=4)


def get_data():
    # 获取原始数据
    with open('lesson4.json', encoding='utf_8') as file:
        data = json.load(file).get('data')
    return data


def save_data_to_file(data, filename):
    with open(filename, 'w', encoding='utf_8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)


def get_and_save(keyword, filename):
    save_data_to_file(get_data().get(keyword), '{}.json'.format(filename))


# call_api_and_save_to_file()
keyword_filename_dict = {
    'list': 'l4_china_area_latest',
    'historylist': 'l4_china_history',
    'otherlist': 'l4_oversea_area_latest',
    'otherhistorylist': 'l4_oversea_history',
    'othertotal': 'l4_oversea_latest',
    'worldlist': 'l4_world_area_latest'
}

for key, value in keyword_filename_dict.items():
    get_and_save(key, value)

