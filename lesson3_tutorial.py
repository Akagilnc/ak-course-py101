import json


def save_to_file(file_name, results):
    # 把格式报告，保存到txt文件
    with open(file_name, 'w', encoding='utf_8') as file:
        file.writelines(results)


def get_data_in_json():
    # 打开json文件，读取数据
    with open('lesson3.json', encoding='utf_8') as file:
        data = json.load(file).get('data')
    return data


# 拿到最新的中国分省市的数据，写入txt文件
def get_china_area_and_save(file_name):
    data = get_data_in_json()

    # 找到中国分省市数据
    china_area_infos = data.get('list')
    update_time = data.get('times')
    results = []

    # 根据数据，来生成我们需要的格式报告
    for info in china_area_infos:
        results.append("{time} {area}, 现存确诊{conf} 死亡{dead} 治愈{cure} 境外输入{input}。较昨日确诊新增{daily_add}\n".format(
            time=update_time,
            area=info.get('name'),
            conf=info.get('econNum'),
            dead=info.get('deathNum'),
            cure=info.get('cureNum'),
            input=info.get('jwsrNum'),
            daily_add=info.get('adddaily').get('conadd')
        ))

    save_to_file(file_name, results)


# 获取海外分国家的最新数据
def get_world_area_and_save(file_name):
    # 获取数据
    data = get_data_in_json()
    # 找到海外分国家数据
    world_area_infos = data.get('otherlist')
    update_time = data.get('times')
    results = []
    # 生成的报告
    for info in world_area_infos:
        results.append(
            "{time}, {area} 现存确诊{econNum} 死亡{deathNum} 治愈{cureNum}, 较昨日， 确诊{con_add} 死亡{death_add} 治愈{cure_add}\n".format(
                time=update_time,
                area=info.get('name'),
                econNum=info.get('econNum'),
                deathNum=info.get('deathNum'),
                cureNum=info.get('cureNum'),
                con_add=info.get('conadd'),
                death_add=info.get('deathadd'),
                cure_add=info.get('cureadd')
            ))
    # 保存到TXT文件
    save_to_file(file_name, results)


get_china_area_and_save('l3_china_area_latest.txt')
get_world_area_and_save('l3_world_area_latest.txt')
