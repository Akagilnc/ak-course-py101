# 创建文件。并且写入内容
def create_file():
    # 打开文件
    data_file = open('lesson2.txt', 'w')
    # 操作：写入内容
    data_file.write('ak, 32, it, m\n')
    data_file.write('lily, 22, hr, f\n')
    data_file.write('tiger, 36, it, m\n')
    data_file.write('lisa, 23, hr, f\n')
    # 关闭文件
    data_file.close()


# 读取文件，生成欢迎语句
def read_and_process(file_name):
    # 打开文件
    data_file = open(file_name)
    # 操作文件
    # 初始化结果集
    results = []
    # 依次读取每一行记录
    for line in data_file:
        # 分别读取 名字，年龄，部门和性别
        name, age, depart, sex = line.split(', ')
        sex = sex.strip()
        # 生成欢迎语。 模板：大家好，我叫XXX，今年XX岁，是个 活泼可爱的大男孩/美丽冻人的小姐姐
        # 如果为M,生成M欢迎语
        if sex == 'm':
            desc = '活泼可爱的大男孩'
        # 如果为F,生成F欢迎语
        else:
            desc = '美丽冻人的小姐姐'
        result = '大家好，我叫{}，今年{}岁，是个{}\n'.format(name, age, desc)
        # 把问候语存入结果集
        results.append(result)
    # 关闭文件
    data_file.close()
    # 返回结果集
    return results


# 把问候语结果集，保存到一个新的文件，lesson2_report.txt
def save_to_file(input_list):
    # 打开
    report_file = open('lesson2_report.txt', 'w', encoding='utf_8')
    # 操作：写入
    report_file.writelines(input_list)
    # 关闭
    report_file.close()


create_file()
contents = read_and_process('lesson2.txt')
for item in contents:
    print(item.strip())
save_to_file(contents)

