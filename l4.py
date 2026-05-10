def print_over_30(file_name):
    results = []
    # 读取hr.txt所有行
    file = open(file_name)
    data = file.readlines()
    file.close()
    # 依次拿到每一行
    for info in data:
        # 切数据
        name, age, sex, dpart = info.split(', ')
        age = int(age)
        dpart = dpart.strip()
        if sex == 'm':
            sex = '先生'
        else:
            sex = '小姐'
        # 如果 年龄 大于 30，存结果
        if age > 30:
            result = '{} {}，就职于{}部门\n'.format(name, sex, dpart)
            results.append(result)
        # 保存到文件
        # write_to_file('tutorial.txt', results)


def write_to_file(file_name, data):
    file = open(file_name, 'w', encoding='utf-8')
    file.writelines(data)
    file.close()


# print_over_30('hr.txt')


def write_by_dpart(file_name):
    it_results, hr_results = [], []
    file = open(file_name)
    data = file.readlines()
    file.close()
    for line in data:
        # 切分数据，对数据做处理
        name, age, sex, dpart = line.split(', ')
        age, dpart = int(age), dpart.strip()
        if sex == 'm':
            sex = '先生'
        else:
            sex = '小姐'
        # 根据部门，保存到两个不同的结果集
        result = '{} {}，就职于{}部门\n'.format(name, sex, dpart)
        if dpart == 'it':
            it_results.append(result)
        if dpart == 'hr':
            hr_results.append(result)
        # 存文件it文件和hr文件
    write_to_file('hr_dpart.txt', hr_results)
    write_to_file('it_dpart.txt', it_results)

write_by_dpart('hr.txt')