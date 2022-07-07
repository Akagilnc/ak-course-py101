import pandas as pd
import matplotlib.pyplot as plt
def process_data():
    # 读取数据
    data = pd.read_excel('l5_data.xlsx', usecols=['直辖市/省份', '城市/地区',
                                                  '累计确诊', '治愈'])
    data = data.set_index('城市/地区')
    # 计算差值
    data['差值'] = data.get('累计确诊') - data.get('治愈')
    # 根据差值，设置状态列的值
    data.loc[data.get('差值') >= 1000, '状态'] = '危险'
    data.loc[data.get('差值') < 1000, '状态'] = '中等'
    data.loc[data.get('差值') < 500, '状态'] = '良好'
    data.loc[data.get('差值') < 100, '状态'] = '优秀'
    # 删除差值
    data = data.drop(columns='差值')
    # 根据状态统计总和与平均值
    sum_df = data.groupby(by='状态').sum()
    mean_df = data.groupby(by='状态').mean()
    # 根据状态统计记录条数
    count_df = data['状态'].value_counts()
    count_df.plot(kind='bar')
    plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']
    plt.show()

process_data()
