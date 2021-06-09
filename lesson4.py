import json


# 读取data级别的数据
def read_json_data():
    # 打开lesson3.json文件，并且读取data
    with open('lesson3.json', encoding='utf-8') as file:
        return json.load(file).get('data')


# 保存到文件
def save_to_file(file_name, data_list):
    with open(file_name, 'w', encoding='utf-8') as file:
        file.writelines(data_list)


# 拿到最新的中国分省市的数据，保存到文件
def get_china_area_and_save(save_file_name):
    # 获取data级别的数据
    data = read_json_data()
    # 找到中国的分省市数据 ，当日的时间，初始化一个结果集
    results = []
    times = data.get('times')
    provinces = data.get('list')
    # 依次拿出所有的分省市数据，生成我们需要的报告
    for province in provinces:
        # 截止XXXX时间，某个省市，现存确诊, 治愈
        province_name = province.get('name')
        cities = province.get('city')
        for city in cities:
            city_name = city.get('name')
            confirm = city.get('conNum')
            cure = city.get('cureNum')
            # 保存到结果集
            results.append(
                '{time}，{provice} {city}，'
                '确诊{confirm}, 治愈{cure}\n'.format(
                    time=times, provice=province_name,
                    city=city_name, confirm=confirm,
                    cure=cure
                ))

    # 保存结果集到文件
    save_to_file(save_file_name, results)


get_china_area_and_save('l4_report.txt')





# 获取海外分国家的最新数据
def    get_world_area_and_save(save_file_name):
    # 获取数据
    # 找到海外分国家数据，数据，时间，初始化结果集
        # 生成报告
    # 保存到文件
    pass


