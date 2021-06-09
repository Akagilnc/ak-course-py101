# 创建文件。并且写入内容
def create_file():
    # 打开文件
    file = open('hr.txt', 'w', encoding='utf-8')
    # 操作：写入内容
    file.write('ak, 32, m, it\n')
    file.write('elsa, 22, f, hr\n')
    file.write('tiger, 35, m, it\n')
    file.write('lisa, 27, f, hr\n')
    # 关闭文件
    file.close()


# create_file()


# 读取文件，生成欢迎语句
def read_and_process():
    # 打开文件
    file = open('hr.txt', encoding='utf-8')
    # 操作文件
    # 初始化结果集
    results = []
    # 依次读取每一行记录
    for line in file.readlines():
        name, age, sex, depart = line.split(', ')
        temp = '大家好，我叫{}，今年{}岁，新加入{}部门，是个{}\n'
        if sex == 'm':
            content = '活泼可爱的大男孩'
        else:
            content = '美丽冻人的小姐姐'
        result = temp.format(name, age, depart.strip(), content)
        results.append(result)
    file.close()
    return results


def write_results_to_file(content_list):
    file = open('report.txt', 'w')
    file.writelines(content_list)
    file.close()


# results = read_and_process()
# write_results_to_file(results)
write_results_to_file(read_and_process())
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
# # 把问候语结果集，保存到一个新的文件，lesson2_report.txt
# def save_to_file(input_list):
#     # 打开
#     # 操作：写入
#     # 关闭


