def write_to_file(file_name):
    # open
    file = open(file_name, 'w', encoding='utf-8')
    # write
    file.write('ak, 32, m, it\n')
    file.write('elsa, 22, f, hr\n')
    file.write('tiger, 35, m, it\n')
    file.write('lisa, 24, f, hr\n')
    # close
    file.close()


# write_to_file('l2.txt')


def read_and_process(file_name):
    file = open(file_name, encoding='utf-8')
    lines = file.readlines()
    file.close()
    template = '大家好，我叫{}，今年{}岁, 是个{}\n'
    results = []
    for line in lines:
        line = line.strip()
        name, age, sex, dpart = line.split(', ')
        if sex == 'm':
            content = '活泼可爱的大男孩'
        else:
            content = '美丽冻人的小姐姐'
        intro = template.format(name, age, content)
        results.append(intro)
    return results


def write_results(file_name, data):
    file = open(file_name, 'w', encoding='utf-8')
    file.writelines(data)
    file.close()


contents = read_and_process('hr.txt')
write_results('l2_report.txt', contents)