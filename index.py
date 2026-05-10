# 第5晚：股价趋势与涨跌幅计算
# 目标：掌握pandas基本操作、时间索引、列运算、涨跌幅计算

import akshare as ak
import pandas as pd
import matplotlib.pyplot as plt

# 获取数据
symbol = "600519"
df = ak.stock_zh_a_hist(symbol=symbol, period="daily", start_date="20240101", end_date="20240601")

# 日期处理
df['日期'] = pd.to_datetime(df['日期'])
df.set_index('日期', inplace=True)

# 添加昨收、涨跌额、涨跌幅
df['昨收'] = df['收盘'].shift(1)
df['涨跌额'] = df['收盘'] - df['昨收']
df['涨跌幅'] = df['涨跌额'] / df['昨收'] * 100

# 可视化收盘价
plt.figure(figsize=(10,5))
plt.plot(df.index, df['收盘'], label="收盘价")
plt.title("股票收盘价趋势图")
plt.xlabel("日期")
plt.ylabel("元")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()

# 导出数据
export_cols = ['收盘', '昨收', '涨跌额', '涨跌幅']
df[export_cols].to_excel("涨跌幅结果.xlsx")

# 小练习建议：
# - 找出涨跌幅最大的一天及其数值
# - 计算2024年4月的平均涨跌幅


# 第6晚：筛选高波动交易日 + 多股票对比分析
# 目标：掌握DataFrame筛选、合并、分组；多只股票比较

# 高波动筛选
high_vol_df = df[df['涨跌幅'].abs() > 3]  # 涨跌幅大于±3%
high_vol_df.to_excel("高波动交易日.xlsx")

# 多股票收盘价对比
symbols = {"600519": "茅台", "000001": "平安银行", "002594": "比亚迪"}
result_df = pd.DataFrame()

for code, name in symbols.items():
    temp = ak.stock_zh_a_hist(symbol=code, period="daily", start_date="20240401", end_date="20240601")
    temp['日期'] = pd.to_datetime(temp['日期'])
    temp.set_index('日期', inplace=True)
    result_df[name] = temp['收盘']

# 可视化多股走势
result_df.plot(figsize=(12,6), title="多只股票收盘价对比")
plt.ylabel("收盘价")
plt.grid(True)
plt.tight_layout()
plt.show()

# 小练习建议：
# - 哪只股票波动最大？哪只最稳定？
# - 4月初买入，6月初卖出，哪只股票收益最高？


# 第7晚：模拟买入策略 + 生成报告
# 目标：结合时间筛选、逻辑判断、计算收益率

buy_day = "2024-04-02"
sell_day = "2024-05-31"

buy_price = df.loc[buy_day, '收盘']
sell_price = df.loc[sell_day, '收盘']
profit = (sell_price - buy_price) / buy_price * 100
print(f"在 {buy_day} 买入并持有到 {sell_day}，收益率为：{profit:.2f}%")

# 批量计算收益
buy_sell_df = pd.DataFrame(columns=['股票', '买入价', '卖出价', '收益率'])

for code, name in symbols.items():
    temp = ak.stock_zh_a_hist(symbol=code, period="daily", start_date="20240401", end_date="20240601")
    temp['日期'] = pd.to_datetime(temp['日期'])
    temp.set_index('日期', inplace=True)
    try:
        bp = temp.loc[buy_day, '收盘']
        sp = temp.loc[sell_day, '收盘']
        rate = (sp - bp) / bp * 100
        buy_sell_df.loc[len(buy_sell_df)] = [name, bp, sp, rate]
    except:
        continue

buy_sell_df.to_excel("模拟买入收益率.xlsx", index=False)

# 小练习建议：
# - 更换买入/卖出日期，观察收益变化
# - 尝试加一列“是否收益为正”作为标签


# 第8晚：自定义指标计算 + 导出图文报告（简单版）
# 目标：实践分析流程，结合计算+图表+导出

# 自定义指标：振幅 = (最高 - 最低) / 昨收

df['振幅'] = (df['最高'] - df['最低']) / df['昨收'] * 100

# 找出前10大振幅交易日
top_vol = df.sort_values(by='振幅', ascending=False).head(10)
top_vol.to_excel("振幅Top10.xlsx")

# 画图
plt.figure(figsize=(10, 5))
plt.bar(top_vol.index.strftime('%Y-%m-%d'), top_vol['振幅'])
plt.title("振幅最大的10个交易日")
plt.xticks(rotation=45)
plt.ylabel("振幅（%）")
plt.tight_layout()
plt.show()

# 小练习建议：
# - 输出包含涨跌幅、振幅、收盘价的汇总图表
# - 思考哪些日子可能对应重大新闻/政策事件
