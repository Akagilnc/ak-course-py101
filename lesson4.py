import json


# 读取data级别的数据
def get_data_in_json_file():
    # 打开lesson3.json文件，并且读取data
    with open('lesson3.json', encoding='utf_8') as file:
        return json.load(file).get('data')


# 保存到文件
def save_to_file(file_name, results_list):
    with open(file_name, 'w', encoding='utf_8') as file:
        file.writelines(results_list)


# 拿到最新的中国分省市的数据，保存到文件
def get_china_area_and_save(save_file_name):
    # 获取data级别的数据
    data = get_data_in_json_file()
    # 找到中国的分省市数据 ，当日的时间，初始化一个结果集
    china_area_infos = data.get('list')
    update_time = data.get('times')
    results = []

    # 依次拿出所有的分省市数据，生成我们需要的报告
    for info in china_area_infos:
        # 截止XXXX时间，某个省市，现存确诊，死亡，治愈，境外输入        # 保存到结果集
        results.append("{time} {area}, 现存确诊{conf} 死亡{dead} 治愈{cure} 境外输入{input}\n".format(
            time=update_time,
            area=info.get('name'),
            conf=info.get('econNum'),
            dead=info.get('deathNum'),
            cure=info.get('cureNum'),
            input=info.get('jwsrNum')
        ))

    # 保存结果集到文件
    save_to_file(save_file_name, results)


# 获取海外分国家的最新数据
def get_world_area_and_save(save_file_name):
    # 获取数据
    data = get_data_in_json_file()
    world_area_data = data.get('otherlist')
    update_time = data.get('times')
    results = []
    # 找到海外分国家数据，数据，时间，初始化结果集
    for info in world_area_data:
        # 生成报告
        results.append("{time} {area} 现存确诊{econ} 死亡{dead} 治愈{cure}，较昨日 确诊{econ_add}，死亡{dead_add}，治愈{cure_add}\n".format(
            time=update_time,
            area=info.get('name'),
            econ=info.get('econNum'),
            dead=info.get('deathNum'),
            cure=info.get('cureNum'),
            econ_add=info.get('conadd'),
            dead_add=info.get('deathadd'),
            cure_add=info.get('cureadd')
        ))
    # 保存到文件
    save_to_file(save_file_name, results)


get_china_area_and_save('lesson4.txt')
get_world_area_and_save('lesson4_world.txt')
