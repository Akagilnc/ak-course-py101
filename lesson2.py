# 创建文件
def create_file():
    # 打开文件
    file = open('lesson2.txt', 'w')
    # 操作：写入数据
    file.write('ak, 32, it, m\n')
    file.write('lily, 22, hr, f\n')
    file.write('tiger, 37, it, m\n')
    file.write('lisa, 25, hr, f\n')
    # 关闭文件
    file.close()


# 读取文件，生成每个人的欢迎语句
# name, age 岁，是一个 描述语
def read_and_process_file():
    # 打开文件
    data = open('lesson2.txt', 'r', encoding='utf_8')
    # define a list
    results = []
    # 依次读取每一条记录
    for line in data:
        name, age, depart, sex = line.split(', ')
        sex = sex.strip()
        if sex == 'm':
            desc = '阳光男孩'
        elif sex == 'f' and age < 45:
            desc = '美丽冻人的小姐姐'
        else:
            desc = '和蔼可亲的婶婶'
        # 生成问候语
        results.append('{}, {}岁, 是一个{}\n'.format(name, age, desc))

    # 关闭文件
    data.close()

    return results


# 把问候语的结果，保存到文件
def save_results_to_file(input_list):
    # 打开文件
    report = open('lesson2_report.txt', 'w', encoding='utf_8_sig')
    # 保存文件
    report.writelines(input_list)
    # 关闭文件
    report.close()


# create_file()


contents = read_and_process_file()
save_results_to_file(contents)
