import json


# 读取data级别的数据
def get_data_in_json_file():
    # 打开lesson3.json文件，并且读取data
    with open('lesson3.json', encoding='utf_8') as file:
        return json.load(file).get('data')


# 保存到文件
def save_to_file(file_name, results):
    with open("{}.json".format(file_name), 'w', encoding='utf_8') as file:
        json.dump(results, file, ensure_ascii=False, indent=4)


# 读取原数据并且保存到新文件
def get_and_save(key, file_name):
    save_to_file(file_name, get_data_in_json_file().get(key))


key_file_dict = {
    'list': 'l4_china_area_latest',
    'historylist': 'l4_china_history',
    'otherlist': 'l4_oversea_area_latest',
    'otherhistorylist': 'l4_oversea_history',
    'othertotal': 'l4_oversea_latest',
    'worldlist': 'l4_world_area_latest'
}

for key, value in key_file_dict.items():
    get_and_save(key, value)
