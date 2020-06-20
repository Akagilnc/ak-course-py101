# 创建文件
def create_file():
    # 打开文件
    data_file = open('lesson2.txt', 'w')
    # 操作：写入内容
    data_file.write('ak, 32, it, m\n')
    data_file.write('lily, 22, hr, f\n')
    data_file.write('tiger, 35, it, m\n')
    data_file.write('lisa, 22, hr, f\n')
    # 关闭文件
    data_file.close()


# 读取文件，并且生成欢迎语句
def read_and_process(file_name):
    # 打开文件
    data_file = open(file_name)
    # 操作文件
    # 初始化结果集
    results = []
    # 依次读取每一行记录
    for line in data_file:
        line = line.strip()
        # 分别获取 名字，年龄，部门，性别
        name, age, depart, sex = line.split(', ')
        if sex == 'm':
            # 生成 阳光男孩
            desc = '活泼可爱的大男孩'
        else:
            # 生成 美丽冻人的小姐姐
            desc = '美丽冻人的小姐姐'
        # 把生成的问候语存入结果集
        result = '大家好！我叫{}, 今年{}岁, 是个{}\n'.format(name, age, desc)
        results.append(result)
    # 关闭文件
    data_file.close()
    return results


# 把问候语结果集，保存到文件
def save_results_to_file(input_list):
    # 打开
    report = open('lesson2_report.txt', 'w', encoding='utf_8')
    # 写入
    report.writelines(input_list)
    # 关闭
    report.close()


create_file()
contents = read_and_process('lesson2.txt')
save_results_to_file(contents)
