# 定义函数，写入特定信息到hr.txt
def write_to_file(file_name):
    # 打开文件，写入模式
    file = open('{}.txt'.format(file_name), 'w')
    # 写入特定信息
    file.write('ak, 32, m, it\n')
    file.write('elsa, 22, f, hr\n')
    file.write('tiger, 35, m, it\n')
    file.write('lisa, 24, f, hr\n')
    # 关闭文件
    file.close()
#
#
# # 调用函数
# write_to_file('hr')


# 定义一个函数，读取hr.tx，生成 欢迎语
def read_and_make():

    # 定义我们的欢迎语模版
    template = '大家好！我是{}，今年{}岁，{}\n'
    # 读取数据
    file = open('hr.txt')
    infos = file.readlines()
    file.close()
    # 依次取出数据
    results = []
    for info in infos:
        # 拿到 姓名，年龄，性别
        name, age, sex, dpart = info.split(', ')
        # 根据性别，决定一句欢迎语
        if sex == 'm':
            intro = '是个活泼可爱的大男孩'
        else:
            intro = '是个美丽冻人的小姐姐'
        # format模版
        result = template.format(name, age, intro)
        results.append(result)
    return results


def write_lines_to_file(file_name, infos):
    file = open('{}.txt'.format(file_name), 'w', encoding='utf-8')
    file.writelines(infos)
    file.close()


# 定义函数
def read_and_print():
    # 读取数据
    file = open('hr.txt')
    data = file.readlines()
    # 定义模版
    template = '{} {}, 就职于{}部门\n'
    # 依次拿出每一条数据
    hr_results = []
    it_results = []
    for line in data:
        # 切分数据
        name, age, sex, dpart = line.split(', ')
        # 数据处理
        dpart = dpart.rstrip()
        if sex == 'm':
            title = '先生'
        else:
            title = '小姐'
        # 根据模版生成数据
        result = template.format(name, title, dpart)
        if dpart == 'hr':
            hr_results.append(result)
        if dpart == 'it':
            it_results.append(result)
    return hr_results, it_results


# data = read_and_make()
# write_lines_to_file('report', data)
# 调用函数
hr_data, it_data = read_and_print()
write_lines_to_file('hr_dpart', hr_data)
write_lines_to_file('it_dpart', it_data)