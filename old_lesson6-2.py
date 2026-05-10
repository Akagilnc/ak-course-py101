import pandas as pd


def process_data():
    data = pd.read_excel('l5_report.xlsx', sheet_name=None)
    data = pd.concat(data, ignore_index=True)
    print(data)


process_data()
