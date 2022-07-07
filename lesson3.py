# temp = [1,2,3,4,5,6,7,8,9,10]
# print(temp[2])
# print(temp[3:8])
# print(temp[6:9])
# print(temp[0:5:2])


def print_info():
    # 读取hr.txt
    file = open('hr.txt', encoding='utf-8')
    lines = file.readlines()
    file.close()
    # 依次读取每一行数据
    template = '名字{}，性别{}，年龄{}'
    for info in lines:
        # 切割数据
        infos = info.split(', ')
        # 打印我们需要的内容
        print(template.format(infos[0], infos[2], infos[1]))


# print_info()
def ref_info_dict():
    # 读取文件
    file = open('hr.txt', encoding='utf-8')
    lines = file.readlines()
    file.close()
    # 定义结果集
    results = []
    # 依次读取每一行数据
    for info in lines:
        # 切割数据
        data = info.strip().split(', ')
        # 生成目标字典
        temp = {'姓名': data[0], '信息': data[1:]}
        # 添加进结果集
        results.append(temp)
    return results

#
# infos = ref_info_dict()
# for info in infos:
#     if info.get('信息')[1] == 'm':
#         print(info.get('姓名'))


def ref_info_dict2():
    # 读取文件
    file = open('hr.txt', encoding='utf-8')
    lines = file.readlines()
    file.close()
    # 定义结果集
    results = []
    # 依次取出
    for info in lines:
        # 切割数据
        name, age, sex, dpart = info.split(', ')
        # 生成目标字典
        result = {'姓名': name, '年龄': int(age), '性别': sex, '部门': dpart}
        # 添加结果集
        results.append(result)
    return results
data = ref_info_dict2()
for info in data:
    if info.get('年龄') < 30:
        print(info['姓名'])

