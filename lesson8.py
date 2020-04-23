from openpyxl.chart import PieChart, BarChart, Reference, Series
from openpyxl import load_workbook
import pandas as pd
from matplotlib import pyplot

pyplot.rcParams['font.sans-serif'] = ['Simhei']
pyplot.rcParams['axes.unicode_minus'] = False


def draw_chart(input_wb, max_row):
    # 拿到我们要操作的sheet
    top_10_sheet = input_wb.worksheets[-1]
    top_10_sheet.sheet_view.zoomScale = 200
    # 初始化我们的barchart
    bar_chart = BarChart()
    pie_chart = PieChart()
    # 指定bar chart数据范围
    bar_chart_data = Reference(top_10_sheet, min_col=4, max_col=7, min_row=1, max_row=max_row)
    pie_chart_data = Reference(top_10_sheet, min_col=4, max_col=4, min_row=1, max_row=max_row)
    # 指定chart的X_axis
    x_data = Reference(top_10_sheet, min_col=2, max_col=2, min_row=2, max_row=max_row)
    # 设置chart样式
    bar_chart.height, bar_chart.width = 15, 30
    pie_chart.height, pie_chart.width = 15, 30
    bar_chart.title, bar_chart.y_axis.title, bar_chart.x_axis.title = 'top10', '人数', '国家'
    bar_chart.y_axis.scaling.max = 5000000
    # 把数据添加进chart，chart添加到sheet，并且保存workbook
    bar_chart.add_data(bar_chart_data, titles_from_data=True)
    bar_chart.set_categories(x_data)
    pie_chart.add_data(pie_chart_data, titles_from_data=True)
    pie_chart.set_categories(x_data)
    top_10_sheet.add_chart(bar_chart, 'I1')
    top_10_sheet.add_chart(pie_chart, 'U1')
    input_wb.save('./excel_files/report_chart.xlsx')


# wb = load_workbook('./excel_files/report_formatted.xlsx')
# draw_chart(wb, wb.worksheets[-1].max_row)
df = pd.read_excel('./excel_files/report_formatted.xlsx', sheet_name='top10')
chart = df.plot.bar(x='countryName', y=['累计确诊', '当前确诊'])
pie_chart = df.set_index(df['countryName']).plot.pie(y='治愈')
pyplot.show()
