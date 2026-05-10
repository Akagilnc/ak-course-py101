import pandas as pd
import matplotlib.pyplot as plt
import openpyxl


def process_data():
    data = pd.read_excel('l5_data.xlsx', usecols=['直辖市/省份', '城市/地区', '累计确诊'])
    data = data.set_index('城市/地区')
    p_names = data.get('直辖市/省份').unique()
    plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']
    plt.tight_layout()
    with pd.ExcelWriter('l8_report_details.xlsx', engine='openpyxl') as file:
        for p_name in p_names:
            p_df = data[data['直辖市/省份'] == p_name]
            p_df.to_excel(file, sheet_name=p_name)
            p_df.sort_values(by='累计确诊', ascending=False).head(5).plot(kind='bar')
            img_name = '{}.png'.format(p_name)
            plt.savefig(img_name)
            sheet = file.sheets[p_name]
            img = openpyxl.drawing.image.Image(img_name)
            img.anchor = 'E1'
            sheet.add_image(img)

process_data()