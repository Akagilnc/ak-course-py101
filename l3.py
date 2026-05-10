def write_to_file(file_name):
    # 打开文件 hr.txt 写入模式
    file = open(file_name, 'w')
    # 写内容
    file.write('ak, 32, m, it\n')
    file.write('elsa, 29, f, hr\n')
    file.write('tiger, 33, m, it\n')
    file.write('lisa, 28, f, hr\n')
    # 关闭文件
    file.close()


#调用函数
# write_to_file('hr.txt')


def make_report(file_name):
    reports = []
    # 从文件里读取信息
    file = open(file_name)
    data = file.readlines()
    file.close()
    # 依次取出每一行数据
    for info in data:
        # 拆分数据
        name, age, sex, dpart = info.split(', ')
        dpart = dpart.strip()
        # 生成报告
        if sex == 'm':
            temp = '先生'
        else:
            temp = '小姐'
        result = '{} {}，就职于{}部门\n'.format(name, temp, dpart)
        # 打印在屏幕
        reports.append(result)
    return reports


def write_lines(file_name, data_list):
    report_file = open(file_name, 'w', encoding='utf-8')
    report_file.writelines(data_list)
    report_file.close()


data = make_report('hr.txt')
write_lines('tutorial.txt', data)
