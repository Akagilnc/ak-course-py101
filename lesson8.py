import json
import pandas as pd
from datetime import datetime
from openpyxl.chart import LineChart, Reference, Series
from matplotlib import pyplot


# 读取上海历史json
def read_file(file_name):
    with open(file_name) as file:
        return json.load(file)['results']


# 根据excel文件里的数据，画一个线形图
def draw_line_chart(input_writer, max_row):
    # 拿到我们操作的sheet
    sheet = input_writer.sheets['shanghai']
    # 初始化我们的line chart
    chart = LineChart()
    # 指定line chart 的 数据范围
    chart_data = Reference(sheet, min_col=2, max_col=4, min_row=1, max_row=max_row)
    # 指定x_AXIS
    x_axis_data = Reference(sheet, min_col=1, max_col=1, min_row=2, max_row=max_row)
    # 设置chart的样式
    chart.height, chart.width = 15, 30
    chart.title, chart.y_axis.title, chart.x_axis.title = '上海疫情趋势', '人数', '日期'
    chart.y_axis.scaling.max = 500
    # chart 添加到 sheet 里
    chart.add_data(chart_data, titles_from_data=True)
    chart.set_categories(x_axis_data)
    sheet.add_chart(chart, 'F1')

    # 保存writer
    input_writer.save()


data = read_file('2019_conv_shanghai_history.json')
data = list(reversed(data))
df = pd.DataFrame(
    data,
    index=[datetime.fromtimestamp(info['updateTime'] / 1000).strftime('%Y-%m-%d') for info in data],
    columns=['confirmedCount', 'curedCount', 'deadCount', 'updateTime']
)

idx = df.groupby(level=0)['updateTime'].transform(max) == df['updateTime']
df = df[idx]
df = df.drop(columns='updateTime')
# writer = pd.ExcelWriter('conv_shanghai.xlsx')
# df.to_excel(writer, sheet_name='shanghai')
# draw_line_chart(writer, len(df)+1)
# writer.save()
chart = df.plot(title='conv Shanghai')
pyplot.show()
