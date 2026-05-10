import pandas as pd


def process_data():
    data = pd.read_excel('l5_data.xlsx')
    data = data[(data.get('累计确诊') > 1000) & (data.get('现存确诊') < 100)]
    with pd.ExcelWriter('l5_report.xlsx', mode='a', engine='openpyxl') as writer:
        data.to_excel(writer, sheet_name='缓解区2', index=False)


process_data()
