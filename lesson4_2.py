import json


# 读取data级别的数据
def get_data_in_json():
    # 打开lesson3.json文件。并且读取data下的数据
    with open('lesson3.json', encoding='utf-8') as file:
        return json.load(file).get('data')


# 保存到json文件
def save_to_json(file_name, data):
    # 打开文件
    with open("{}.json".format(file_name), 'w', encoding='utf-8') as file:
        # 保存json文件，不转译中文，间距为4
        json.dump(data, file, ensure_ascii=False, indent=4)


def read_and_save(key, save_file_name):
    data = get_data_in_json().get(key)
    save_to_json(save_file_name, data)


key_file_dict = {
    'list': 'l5_china_area_latest',
    'othertotal': 'l5_oversea_latest',
    'otherhistorylist': 'l5_oversea_history',
    'otherlist': 'l5_oversea_area_latest',
    'historylist': 'l5_china_history',
    'worldlist': 'l5_world_area_latest'
}
for key, value in key_file_dict.items():
    read_and_save(key, value)



