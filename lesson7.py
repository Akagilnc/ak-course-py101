import pandas as pd
from math import pi
import bokeh.plotting as plt
from bokeh.models import ColumnDataSource
from bokeh.palettes import Category20c
from bokeh.transform import factor_cmap
from bokeh.transform import cumsum
# from matplotlib import pyplot as plt
from matplotlib.font_manager import FontProperties

# 筛选国家级别的数据，生成汇总报告
# 从多个excel/sheet读取，然后筛选数据，
# - 重命名列的几种方法
# - 提取、添加、删除列
# - 把字符串转换为数值
# - 把字符串分割为多列


# sheet 增上改查 format 行高列高， 格式为主
# 遍历多层级目录，

# 调整格式。可以展示的文字报告
# 如何取excel里范围数据（比如第7行到第20行）

# 3. DataFrame的常用基本操作

# - df.T 一键转置
# - 反转序列

# 5. DataFrame数据筛选
# - 索引 / 选择
# - 按数据类型选择列
# - 根据多个类别筛选 DataFrame


# plt.rcParams['font.sans-serif'] = ['SimHei']
# plt.rcParams['axes.unicode_minus'] = False

data = pd.read_excel('./excel_files/report.xlsx', sheet_name=0, index_col='provinceName')

data_china = data[(data.countryName == '中国') & (data.index != '中国')]
data = data.drop(data_china.index)
for i in range(1, 6):
    other_data = pd.read_excel('./excel_files/report.xlsx', sheet_name=i, index_col='provinceName')
    data = data.append(other_data)
data = data.sort_values(by='confirmedCount', ascending=False)
chart_data = data['confirmedCount'].head(10).reset_index(name='confirmedCount')

chart_data['color'] = Category20c[len(chart_data)]

chart_data['confirmedCount'] = chart_data['confirmedCount'].astype('int')

chart_data['angle'] = chart_data['confirmedCount'] / chart_data['confirmedCount'].sum() * 2 * pi
print(chart_data)
# countries = chart_data['provinceName'].tolist()
p = plt.figure(plot_height=500, title="Pie Chart", toolbar_location=None,
               tools="hover", tooltips="@provinceName: @confirmedCount", x_range=(-0.5, 1.0))

# color_map = factor_cmap(field_name='provinceName',
#                         palette=Spectral10, factors=countries)

p.wedge(x=0, y=1, radius=0.4,
        start_angle=cumsum('angle', include_zero=True),
        end_angle=cumsum('angle'), legend_field='provinceName',
        line_color="white", fill_color='color', source=chart_data)
p.xaxis.axis_label = 'Country'
p.yaxis.axis_label = 'Confirmed Count'
# p.circle(x='confirmedCount', y='currentConfirmedCount', source=source)
plt.show(p)
