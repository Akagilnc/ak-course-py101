import json
# 定义读取文件函数
def read_json():
    # 读取json文件
    file = open('l3.json', encoding='utf-8')
    data = json.load(file)
    file.close()
    # 返回数据
    return data
# 处理函数
def make_report(data):
    # get中国直辖市/省数据
    infos = data.get('data').get('list')
    # 定义报告模版
    template = '中国：{}：境外输入{}例'
    # 依次取出每一条数据
    for info in infos:
        # 生成结果
        result = template.format(info.get('name'), info.get('jwsrNum'))
        print(result)

data = read_json()
make_report(data)