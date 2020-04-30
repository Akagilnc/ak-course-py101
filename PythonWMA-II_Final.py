import requests
import json
import pandas as pd
from datetime import datetime
from openpyxl.chart import PieChart, BarChart, LineChart, Reference, Series
from openpyxl.chart.label import DataLabelList


# 获取疫情数据，保存至json文件
def call_api(address, js_file_name):
    response = requests.get(address)
    with open(js_file_name, 'w', encoding='utf_8_sig') as file:
        json.dump(response.json(), file, ensure_ascii=False, indent=4)


# 读取json文件获取数据
def read_file(file_name):
    with open(file_name, encoding="utf_8_sig") as file:
        return json.load(file)['results']


# Part I (Cros) 根据全国最新确诊人数，画出饼图
# 生成所需DataFrame
def get_pie_data(input_data):
    # 提取基本data
    df = pd.DataFrame(input_data)
    df = df[['provinceName', 'confirmedCount']]
    # 去除湖北省
    df = df[df['provinceName'] != '湖北省']
    # 建立其他项合并确诊人数低于500的地区
    df2 = df[df['confirmedCount'] <= 500]
    sum_others = df2.sum()
    sum_others['provinceName'] = '其他地区'
    sum_df = sum_others.rename('others')
    # 去除确诊人数低于500的地区
    df = df[df['confirmedCount'] > 500]
    # 按确诊人数从大到小排序
    df = df.sort_values(by=['confirmedCount'], ascending=False)
    df = df.reset_index(drop=True)
    # 将该项并入DataFrame
    df = df.append(sum_df)
    return df


# 画出饼图
def add_pie_chart(writer, df):
    # 初始化excel并确立图表类型
    sheet = writer.sheets['全球最新疫情分布']
    chart = PieChart()
    # 设置插入序列
    max_row = len(df)
    labels = Reference(sheet, min_col=2, max_col=2, min_row=2, max_row=max_row+1)
    chart_data = Reference(sheet, min_col=3, max_col=3, min_row=1, max_row=max_row+1)
    chart.add_data(chart_data, titles_from_data=True)
    chart.set_categories(labels)
    # 设置图表格式
    chart.title = "除湖北外全球各地区确诊人数占比"
    chart.height, chart.width = 14, 21
    chart.style = 5
    chart.dataLabels = DataLabelList()
    chart.dataLabels.showCatName = True
    chart.dataLabels.showPercent = True
    # 插入图表
    sheet.add_chart(chart, 'F1')
    writer.save()


# Part II (Megan) 画出确诊人数与死亡人数散点图，作线性回归
# 生成所需dataframe
def get_scatter_data(input_data):
    # 生成基本数据dataframe
    df = pd.DataFrame(input_data,
                      columns=['provinceName','confirmedCount', 'deadCount'])
    # 建立回归所用数据list
    regress_dead_count = []
    outliers = ['伊朗','意大利','黑龙江省','河南省','浙江省','江苏省','江西省']
    # 将outliers从regression sample中去除
    for data in input_data:
        if data['provinceName'] in outliers:
            regress = None
        else:
            regress = data['deadCount']
        regress_dead_count.append(regress)
    # 将回归list作为一列插入
    df['regressdata'] = regress_dead_count
    # 建立outliers地区字典
    outliers_list = {key:[] for key in outliers}
    # 填充outliers地区字典lists,只填充outiers地区数值
    for key in outliers_list:
        for data in input_data:
            if data['provinceName'] == key:
                outlier = data['deadCount']
            else:
                outlier = None
            outliers_list[key].append(outlier)
    # 生成outlier地区数据data frame
    df2 = pd.DataFrame(outliers_list)
    # 合并两个data frame
    final = pd.concat([df, df2], axis=1)
    # 按确诊人数从小到大排序
    final = final.sort_values(by=['confirmedCount'], ascending=True)
    return final


# 生成散点回归图
def add_scatter_chart(writer,df):
    # 初始化excel确定图表类型
    workbook = writer.book
    worksheet = writer.sheets['全球最新疫情']
    chart = workbook.add_chart({'type':'scatter'})
    # 建立outliers list 及 color list
    outliers = ['伊朗', '意大利', '黑龙江省', '河南省', '浙江省', '江苏省', '江西省']
    colors = ['#E57D7D','#EA9797','#EEACAC','#F1BDBD','#83B1DA','#9CC1E1','#B0CDE7']
    # 加入outliers图表系列
    max_row = len(df)-1
    for i in range (5,12):
        chart.add_series({'values': ['全球最新疫情',1,i,max_row,i],
                          'categories':['全球最新疫情',1,2,max_row,2],
                          'name': outliers[i-5],
                          'marker': {'type': 'circle','size': 8,'border': {'color': '#EEEEEE'},'fill': {'color': colors[i-5]}},
                          })
    # 加入回归图表系列
    chart.add_series({'name': '回归数据',
                      'values': ['全球最新疫情',1,4,max_row,4],
                      'categories':['全球最新疫情',1,2,max_row,2],
                      'marker': {'type': 'circle', 'size': 8, 'border': {'color': '#3B855E'},
                                 'fill': {'color': '#4AA675'}},
                      'trendline': {'type': 'linear',
                                    'display_equation': True,
                                    'display_r_squared': True,
                                    'displayRSqr': True,
                                    'dash_type': 'long_dash'}
                      })
    # 设置和格式化图表
    chart.set_x_axis({'name':'确诊人数','name_font': {'bold': True, 'name': '微软雅黑', 'size': 9, 'color':'black'}})
    chart.set_y_axis({'name':'死亡人数','name_font': {'bold': True, 'name': '微软雅黑', 'size': 9, 'color':'black'}})
    chart.set_size({'width': 720, 'height': 576})
    chart.set_title({'name': '全球除湖北外地区死亡人数与确诊人数分布图','name_font': {'bold': True, 'name': '微软雅黑', 'size': 12, 'color':'black'}})
    # 插入excel
    worksheet.insert_chart('F4',chart)
    writer.save()


# Part III (Jing) 画出死亡率柱状图，并计算湖北外平均死亡率
# 计算各地区死亡率，并获取除湖北外死亡率
def get_death_rate(data):
    df = pd.DataFrame(data,
                      index=[datetime.fromtimestamp(info['updateTime'] / 1000).strftime('%Y-%m-%d') for info in data],
                      columns=['countryName', 'provinceShortName', 'confirmedCount', 'deadCount'])
    # 计算死亡率
    df.eval('deathRate = deadCount/confirmedCount', inplace=True)
    df = df.sort_values(by=['deathRate'], ascending=False)
    # 获取汇总数据
    sum_info = df.sum()
    sum_info = sum_info.rename('合计')
    sum_info['countryName'] = sum_info['provinceShortName'] = ''
    sum_info['deathRate'] = sum_info['deadCount']/sum_info['confirmedCount']
    # 获取除湖北外汇总数据
    sum_info_exhb = df[df['provinceShortName'] != '湖北'].sum()
    sum_info_exhb = sum_info_exhb.rename('除湖北外合计')
    sum_info_exhb['countryName'] = sum_info_exhb['provinceShortName'] = ''
    sum_info_exhb['deathRate'] = sum_info_exhb['deadCount'] / sum_info_exhb['confirmedCount']
    df = df.append(sum_info)
    df = df.append(sum_info_exhb)
    # 获取死亡率数值并保存
    death_rate_exhb = df.loc['除湖北外合计']['deathRate']
    df = df[(df['confirmedCount'] > 100)]
    df['avg_death_rate'] = death_rate_exhb
    return df, death_rate_exhb


# 根据excel文件里的数据，画一个柱形图
def draw_bar_chart(writer, max_row):
    sheet = writer.sheets['死亡率']
    date = sheet['A2'].value
    # 初始化我们的bar chart
    chart = BarChart()
    # 指定bar chart 的数据范围
    chart_data = Reference(sheet, min_col=6, max_col=6, min_row=2, max_row=max_row-1)
    chart_series = Series(chart_data, title='截止{}死亡率'.format(date))
    chart_series.graphicalProperties.solidFill = '5DD092'  # Silver Tree
    # 指定x轴
    x_axis_data = Reference(sheet, min_col=3, max_col=3, min_row=2, max_row=max_row-1)
    # chart 添加到 sheet里
    chart.append(chart_series)
    chart.set_categories(x_axis_data)
    # 设置chart的样式
    chart.height, chart.width = 14, 21
    chart.title, chart.y_axis.title = '主要疫情地区死亡率', '死亡率'
    chart.y_axis.number_format = '0.0%'
    chart.legend.position = 't'
    # 画平均死亡率横线line chart
    line_chart = LineChart()
    line_data = Reference(sheet, min_col=7, max_col=7, min_row=2, max_row=max_row - 1)
    line_series = Series(line_data, title='除湖北外死亡率')
    line_chart.append(line_series)
    # 合并图表
    chart += line_chart
    # 添加图表并保存
    sheet.add_chart(chart, 'I1')
    writer.save()


# Part IV (Gray) 根据其他地区死亡率倒推湖北初期感染人数
# 根据其他地区死亡率，获取模拟的感染人数
def get_adjusted_hb_data(input_data, death_rate):
    df = pd.DataFrame(input_data,
                          index=[datetime.fromtimestamp(info.get("updateTime")/1000).strftime("%Y-%m-%d")
                                    for info in input_data],
                          columns=["confirmedCount", "deadCount", "updateTime"])
    idx = df.groupby(level=0)['updateTime'].transform(max) == df['updateTime']
    df = df[idx]
    df = df.drop(columns='updateTime')
    df['deathRate'] = death_rate
    df.eval("simulationCount= deadCount/deathRate", inplace=True)
    df = df[df["deadCount"] <= 1000]
    df = df.drop(columns=["deadCount", 'deathRate'])
    df = df.rename(columns={"confirmedCount": "报告确诊人数", "simulationCount": "模拟感染人数"})
    return df


# 将模拟数据对比官方数据画线状图
def draw_line_chart(input_writer, max_row):
    sheet = input_writer.sheets["湖北省"]
    chart = LineChart()
    chart_data = Reference(sheet, min_col=2, max_col=3, min_row=1, max_row=max_row)
    # 指定 x 轴
    x_axis_data = Reference(sheet, min_col=1, max_col=1, min_row=2, max_row=max_row)
    # 设置 chart 的样式
    chart.height, chart.width = 15, 30
    chart.title, chart.y_axis.title, chart.x_axis.title = '湖北感染人数（报告数vs模拟数）', '人数', '日期'
    chart.y_axis.scaling.max = 50000
    # chart 添加到 sheet 里
    chart.add_data(chart_data, titles_from_data=True)
    chart.set_categories(x_axis_data)
    sheet.add_chart(chart, 'F1')
    chart.height, chart.width = 14, 21
    chart.style = 5
    # 保存 writer
    input_writer.save()


# 调用函数
address1 = 'https://lab.isaaclin.cn//nCoV/api/area?latest=1'
call_api(address1, '2019_conv_latest.json')
infos = read_file('2019_conv_latest.json')

pie_data = get_pie_data(infos)
scatter_data = get_scatter_data(infos)
death_rate_data, est_death_rate = get_death_rate(infos)

address2 = "https://lab.isaaclin.cn/nCoV/api/area?latest=0&province=湖北省"
call_api(address2, 'hubei.json')
hb_infos = list(reversed(read_file('hubei.json')))
adjusted_hb_data = get_adjusted_hb_data(hb_infos, est_death_rate)

with pd.ExcelWriter('2019_conv_project_final.xlsx') as writer:
    scatter_data.to_excel(writer, sheet_name='全球最新疫情')
    add_scatter_chart(writer, scatter_data)

with pd.ExcelWriter('2019_conv_project_final.xlsx', mode='a', engine='openpyxl') as writer:
    pie_data.to_excel(writer, sheet_name='全球最新疫情分布')
    add_pie_chart(writer, pie_data)
    death_rate_data.to_excel(writer, sheet_name='死亡率')
    draw_bar_chart(writer, len(death_rate_data))
    adjusted_hb_data.to_excel(writer, sheet_name='湖北省')
    draw_line_chart(writer, 20)



