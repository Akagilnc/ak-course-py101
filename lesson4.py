import json
import requests


# 调用API获得最新的疫情数据，并保存到一个json文件
def call_api_and_save_to_file():
    # 调用API
    data = requests.get('https://interface.sina.cn/news/wap/fymap2020_data.d.json')
    # 打开文件
    file = open('lesson4.json', 'w', encoding='utf_8')
    # 保存文件
    json.dump(data.json(), file, ensure_ascii=False, indent=4)
    # 关闭文件
    file.close()


call_api_and_save_to_file()

# 获取原始数据
def get_data():
    # 读取原始文件
    with open('lesson4.json', encoding='utf_8') as file:
        return json.load(file).get('data')


# 保存目标文件
def save_data_to_file(input_data, file_name):
    # 保存到目标文件
    with open('{}.json'.format(file_name), 'w', encoding='utf_8') as report:
        json.dump(input_data, report, ensure_ascii=False, indent=2)


def get_and_save(keyword, file_name):
    # 读取原始文件找到数据保存到目标文件
    save_data_to_file(get_data().get(keyword), file_name)


keyword_filename_dict = {
    'historylist': 'l4_china_history',
    'otherhistorylist': 'l4_oversea_history',
    'othertotal': 'l4_oversea_latest',
    'worldlist': 'l4_world_area_latest',
    'list': 'l4_china_area_latest',
    'otherlist': 'l4_oversea_area_latest'
}
for key, value in keyword_filename_dict.items():
    get_and_save(key, value)
