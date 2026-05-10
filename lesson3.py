def print_list():
    temp = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(temp[2])
    print(temp[3:8])
    print(temp[-4:-1])
    print(temp[0:5:2])


# print_list()


def read_and_print():
    # 读取文件的数据
    with open('hr.txt') as file:
        # 读取每行的数据
        data = file.readlines()
    for line in data:
        # 切分数据
        infos = line.split(', ')
        # 打印需要的数据
        print(infos[0], infos[1], infos[2])


# read_and_print()


def make_dict_data():
    results = []
    # 读取文件的数据
    with open('hr.txt') as file:
        # 读取每行数据
        infos = file.readlines()
    # 切分数据
    for info in infos:
        data = info.split(', ')
        # 生成字典
        temp = {'姓名': data[0], '信息': data[1:]}
        # 将字典存到list里
        results.append(temp)
    # 打印所有男性员工
    for result in results:
        if result.get('信息')[1] == 'm':
            print(result.get('姓名'))


# make_dict_data()


def big_than_30():
    results = []
    # 读取文件数据
    with open('hr.txt') as file:
        data = file.readlines()
    # 读取每一行数据
    for info in data:
        # 拆数据
        info = info.split(', ')
        # 生成字典
        temp = {'姓名': info[0], '年龄': int(info[1]),
                '性别': info[2], '部门': info[-1].strip()}
        # 保存到结果list里
        results.append(temp)
    # 读取每一条字典
    for result in results:
        # 打印三十岁以上的员工
        if result.get('年龄') > 30:
            print(result.get('姓名'))


big_than_30()
