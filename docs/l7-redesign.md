# L7

## 定位

L7 的主题：从累计数据走到变化速度。

L5 讲了 DataFrame 和图，L6 讲了排序、筛选和多 sheet。L7 开始把“历史数据”真正用起来：同一条曲线，既能看累计规模，也能看每天变化速度。

- 输入：`lesson4.json` 里的海外历史疫情数据。
- 处理：最后一次把 JSON 历史数据整理成 Excel，再读 Excel 计算昨日累计、每日新增、增长率和 7 日平均，最后画一张新增趋势图。
- 输出：`l7_history.xlsx`、`l7_change_report.xlsx`、`l7_analysis_report.xlsx`、`l7_new_cases.png`。
- 课堂重点：累计数看规模，新增数看速度；异常日是线索，不是结论。

## 时间结构

总时长约 2.5 小时。

### 前半

- 课前热身：复习 DataFrame、新增列、排序、多 sheet、基础百分比。
- 主任务：生成一份全球疫情历史变化报告。
- Step 1：最后一次从 JSON 整理历史数据，导出 `l7_history.xlsx`。
- Step 2：读 `l7_history.xlsx`，用 `shift(1)` 计算昨日累计和每日新增，导出 `l7_change_report.xlsx`。
- Step 3：读 `l7_change_report.xlsx`，计算增长率和 7 日平均，导出多 sheet 分析报告，并保存一张新增趋势图。

### 后半

后半继续 3 个案例，学生不跟敲，主要看图表、讨论、拍照问 AI。

- 案例 1：时间数据的周期性，先比较同类日期。
- 案例 2：新增 Top 10 和 7 日平均分别适合看什么。
- 案例 3：用股票最大回撤做类比：最终结果之外，过程也重要。

## 课前热身：L1-L6 Quiz

目标不是考试，是把今天会继续用到的基础能力叫醒。展示时沿用前几节课的结构：每页一个完整代码块，下面放两道题。

### Quiz 1 / 8：函数调用和返回值

```python
def make_report(file_name):
    print("正在处理：", file_name)
    return "完成"

status = make_report("lesson4.json")
print(status)
```

1. 真正触发函数运行的是哪一行？

- A. `def make_report(file_name):`
- B. `print("正在处理：", file_name)`
- C. `status = make_report("lesson4.json")`
- D. `print(status)`

2. 变量 `status` 最后保存的是什么？

- A. `lesson4.json`
- B. `正在处理`
- C. `完成`
- D. `file_name`

### Quiz 2 / 8：嵌套数据先找到那一层

```python
raw_data = {
    "data": {
        "history": [
            {"date": "10.01", "certain": "1000"},
            {"date": "10.02", "certain": "1260"},
        ]
    }
}

history = raw_data["data"]["history"]
first_day = history[0]
```

3. `history` 更像什么？

- A. 一批按日期排列的记录
- B. 一个 Excel 文件名
- C. 一张已经画好的图
- D. 一个单独的数字

4. `first_day["certain"]` 取到的是？

- A. `10.01`
- B. `1000`
- C. `history`
- D. `data`

### Quiz 3 / 8：DataFrame 只拿这次要分析的列

```python
df = pd.DataFrame(
    history,
    columns=["date", "certain", "die", "recure"],
)
```

5. `columns=[...]` 在这里更像什么动作？

- A. 只挑出本次报告要用的字段
- B. 把所有数字加起来
- C. 按日期从大到小排序
- D. 把表格保存成 Excel

6. 如果原始记录里还有很多字段，会怎样？

- A. 没写进 `columns` 的字段不会进入这张表
- B. pandas 会自动全部保留
- C. 程序一定报错
- D. 字段会变成 sheet 名

### Quiz 4 / 8：字段名和数据类型

```python
df = df.rename(columns={"certain": "累计确诊"})
df = df.astype({"累计确诊": int})

df["累计确诊"] = df["累计确诊"] + 100
```

7. 哪一行让后面的列名变成中文？

- A. `rename(...)`
- B. `astype(...)`
- C. `+ 100`
- D. 这三行都不是

8. 为什么加 100 前要先 `astype`？

- A. 原始数字可能是文本，直接计算会出问题
- B. 中文列名必须转成整数
- C. Excel 只能保存整数列
- D. 排序之前必须加 100

### Quiz 5 / 8：新增列把原始数字变成指标

```python
df["死亡率"] = (
    df["累计死亡"] / df["累计确诊"] * 100
).round(2)
```

9. 这句代码生成的不是原始数据，而是？

- A. 一个计算出来的比例指标
- B. 一个新的 JSON 文件
- C. 一个排序规则
- D. 一个函数参数

10. 为什么报告里常常需要比例，而不只看人数？

- A. 比例更适合比较规模不同的对象
- B. 比例一定比人数更真实
- C. 人数不能保存到 Excel
- D. pandas 只能计算比例

### Quiz 6 / 8：排序先看哪个问题

```python
current_top = df.sort_values(
    by="现存确诊",
    ascending=False,
).head(10)
```

11. 多选：如果想改成“按累计确诊从高到低排”，哪些改动合理？

- A. 把 `by="现存确诊"` 改成 `by="累计确诊"`
- B. 把 `ascending=False` 改成 `ascending=True`
- C. 把 `head(10)` 改成 `head("累计确诊")`
- D. 把变量名 `current_top` 改成 `total_top`

12. 这段代码执行后，`current_top` 里最多有几行？

- A. 10 行
- B. 100000 行
- C. 和 `df` 一样多
- D. 0 行

### Quiz 7 / 8：筛选条件写在中括号里

```python
serious = df[df["死亡率"] > 5]
active = df[df["现存确诊"] > 100000]
```

13. 如果口径改成“死亡率大于等于 5”，第一行条件应该怎么写？

- A. `df["死亡率"] >= 5`
- B. `df["死亡率"] <= 5`
- C. `df["现存确诊"] >= 5`
- D. `df["死亡率"] = 5`

14. 如果要筛出“现存确诊超过 50 万”的地区，哪种写法是对的？

- A. `df[df["现存确诊"] > 500000]`
- B. `df["现存确诊" > 500000]`
- C. `df[df["死亡率"] > 500000]`
- D. `df[df["现存确诊"] = 500000]`

### Quiz 8 / 8：多 sheet 写入同一个 Excel

```python
with pd.ExcelWriter("report.xlsx") as writer:
    df.to_excel(writer, sheet_name="完整明细", index=False)
    current_top.to_excel(writer, sheet_name="当前压力Top10", index=False)
```

15. 这段代码里，哪个对象负责写 Excel 文件？

- A. `writer`
- B. `index`
- C. `sheet_name`
- D. `current_top`

16. `sheet_name="当前压力Top10"` 在设置什么？

- A. 工作表名字
- B. Excel 文件名
- C. DataFrame 变量名
- D. 行号是否导出

答案：`1.C 2.C 3.A 4.B 5.A 6.A 7.A 8.A 9.A 10.A 11.A/D 12.A 13.A 14.A 15.A 16.A`

## 前半：生成全球疫情历史变化报告

### 章节页

`#1 今天和昨天差多少`

Use yesterday to understand today.

### 主任务

函数名：

```python
make_daily_change_report(file_name)
```

输入：

- 一份历史疫情 JSON 数据。

输出：

- `l7_history.xlsx`
- `l7_change_report.xlsx`
- `l7_analysis_report.xlsx`
- `l7_new_cases.png`

目标：

- 把历史 JSON 整理成 Excel。
- 计算昨日累计、每日新增。
- 计算增长率、7 日平均。
- 找出新增确诊最高的日期。
- 画出最近 30 天新增确诊和 7 日平均趋势。

## Step 1：历史 JSON -> 历史 Excel

### 目标

把历史 JSON 先整理成 Excel。后面的计算尽量读 Excel，不在每一步都重新拆 JSON。

### 代码

```python
import json
import pandas as pd
import matplotlib.pyplot as plt


def make_daily_change_report(file_name):
    file = open(file_name, encoding="utf-8")
    raw_data = json.load(file)
    file.close()

    history = raw_data["data"]["otherhistorylist"]

    df = pd.DataFrame(
        history,
        columns=["date", "certain", "die", "recure"],
    )

    df = df.rename(columns={
        "date": "日期",
        "certain": "累计确诊",
        "die": "累计死亡",
        "recure": "累计治愈",
    })

    df = df.astype({
        "累计确诊": int,
        "累计死亡": int,
        "累计治愈": int,
    })

    df = df.sort_values(by="日期")

    df.to_excel("l7_history.xlsx", index=False)
```

### Recap

- `columns`：只保留这节课要分析的列。
- `rename`：把字段名改成中文。
- `astype`：把文本数字转成整数。
- `sort_values(by="日期")`：按日期排序，让旧日期排在前面，新日期排在后面。

### 读 Excel 前：pandas 会猜数据类型

pandas 读 Excel 时，会根据内容猜每一列是什么类型。

- `09.26` 这种日期看起来像小数，可能被当成数字。
- 一旦按数字读，前面的 `0` 可能消失，变成 `9.26`。
- 所以读回 Excel 时，用 `dtype={"日期": str}` 明确告诉 pandas：日期这一列按文字读。

读数据时，第一步不是计算，而是先确认数据有没有被读成正确的样子。

## Step 2：读 Excel，计算每日新增

### 目标

用昨天的数据解释今天的数据。累计数本身一直在增加，新增数才更接近“变化速度”。

### 代码

```python
    df = pd.read_excel("l7_history.xlsx", dtype={"日期": str})

    df["昨日确诊"] = df["累计确诊"].shift(1)
    df["新增确诊"] = df["累计确诊"] - df["昨日确诊"]

    df["昨日死亡"] = df["累计死亡"].shift(1)
    df["新增死亡"] = df["累计死亡"] - df["昨日死亡"]

    df = df.dropna()

    df.to_excel("l7_change_report.xlsx", index=False)
```

### Recap

- `shift(1)`：把一列整体往下挪一格。
- `dtype={"日期": str}`：读 Excel 时，把日期当成文字，不让 `09.26` 变成 `9.26`。
- 往下挪以后，每一行旁边就有了昨天的数据。
- 今天累计减昨天累计，就是今天新增。
- 第一行没有昨天，用 `dropna()` 去掉空值行。

## Step 3：增长率、7 日平均、新增 Top 10 和趋势图

### 目标

新增最高的一天很重要，但单日数字会抖。Step 3 同时看“异常日”和“趋势”，并把最近 30 天画成图。

### 代码

```python
    df = pd.read_excel("l7_change_report.xlsx", dtype={"日期": str})

    df["增长率"] = (df["新增确诊"] / df["昨日确诊"] * 100).round(2)
    df["7日平均新增"] = df["新增确诊"].rolling(7).mean().round(0)

    top10 = df.sort_values(by="新增确诊", ascending=False).head(10)

    with pd.ExcelWriter("l7_analysis_report.xlsx") as writer:
        df.to_excel(writer, sheet_name="每日变化", index=False)
        top10.to_excel(writer, sheet_name="新增Top10", index=False)

    recent = df.tail(30)
    plt.plot(recent["日期"], recent["新增确诊"])
    plt.plot(recent["日期"], recent["7日平均新增"])
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig("l7_new_cases.png")
```

最后调用：

```python
make_daily_change_report("lesson4.json")
```

### Recap

- `增长率`：把新增确诊放回昨日累计里看比例。
- `rolling(7).mean()`：每一天看最近 7 天的平均新增；前 6 天不够 7 天，会先空着。
- `sort_values(...).head(10)`：找出新增最高的 10 天。
- 一个 Excel 可以同时放每日明细和 Top 10。
- `plt.plot()`：画折线。
- `plt.savefig()`：把图保存成图片文件。

## 后半：看变化速度

### 后半章节页

`#2 不是只看总数`

总数告诉你规模，变化告诉你速度；时间数据还要先看周期。

## 案例 1：周期性，先看同类日期

### 目标

理解时间数据经常有自己的节奏。今天比昨天低，不一定代表趋势变差；有时要和上周同一天、同类日期比较。

### 展示数据

```text
奶茶店订单：
5.10 周日 230
5.11 周一 132
5.12 周二 148
5.13 周三 158
5.14 周四 165
5.15 周五 205
5.16 周六 275
5.17 周日 248
```

### 问题

- 周日比周六少，是不是说明生意变差了？
- 平日和周末的订单节奏有什么差别？
- 如果你是店长，排班和备货会怎么调整？

### 所以呢

- 排班和备货看星期规律，不看某一天的孤立升降。
- 同类日期连续变差，才更像真实下滑。
- 结论要带比较对象：比昨天、比上周，含义不一样。

### AI 可选

```text
奶茶店订单：
5.10 周日 230
5.11 周一 132
5.12 周二 148
5.13 周三 158
5.14 周四 165
5.15 周五 205
5.16 周六 275
5.17 周日 248

5.17 比 5.16 少 27 单，
但比上周日 5.10 多 18 单。
请分析：
1. 订单数有什么周期规律？
2. 能不能直接说生意变差？
3. 店长排班和备货要注意什么？
```

参考输出：

```text
这组数据里，周末订单明显高于工作日，周六最高，周日也高于多数平日。
5.17 比 5.16 少，不能直接说明生意变差，因为周六和周日的消费节奏不同。
如果要判断周日表现，应该继续看更多周日数据；如果做排班备货，周五到周日更需要准备人手和库存。
结论：时间数据要先看周期，再谈趋势和动作。
```

## 案例 2：Top 10 和 7 日平均分别看什么

### 目标

Top 10 适合找异常日，7 日平均适合看趋势。两个都要看，但不能混成一个问题。

### 轻代码

```python
top10 = df.sort_values(by="新增确诊", ascending=False).head(10)
df["7日平均新增"] = df["新增确诊"].rolling(7).mean().round(0)
```

### 展示效果

单日新增会抖，7 日平均更稳。一个高点先当线索，不急着当结论。

可以用一张图展示两条线：

- 每日新增：某一天可能突然冲高。
- 7 日平均：更适合看连续方向。

### 问题

- 黄色线那个单日冲高，适合写成“趋势变坏”吗？
- 绿色线缓慢上行，说明它不是完全偶发；还需要看什么？
- 如果要安排下一步，是先查冲高那一天，还是继续观察后面几天？

### 所以呢

- 尖峰是调查入口，不是原因本身。
- 均线看尖峰背后有没有连续抬升。
- 一边查异常日，一边盯后续均线有没有继续走高。

## 案例 3：最大回撤，收益之外的痛感

### 目标

引入一个成人容易理解的概念：最终结果之外，过程也重要。

这部分由老师展示，学生只看图和讨论。重点是理解“最后赚了”和“中途能不能扛住”不是一回事。

### 场景

```text
股票A：最终收益 20%，中途最大下跌 8%
股票B：最终收益 35%，中途最大下跌 40%
```

### 问题

- 如果你是保守型，A 和 B 哪个更容易拿住？
- 如果你追求高收益，B 的 -40% 需要提前接受什么代价？
- 比较两个方案时，只看收益率还缺哪一项？

### 所以呢

- 收益高，只说明终点诱人。
- 最大回撤是在问：最难受的时候，你还拿不拿得住。
- 两个产品最后都赚钱，但一个中途只跌 8%，另一个中途跌 40%，真实体验完全不同。
- 如果中途会被迫退出，最后的收益率就是纸面数字。

## 后半 Recap

- 比较之前先确认口径：昨天、同类日期、平均线，回答的是不同问题。
- `shift` 让我们把“今天”和“昨天”放在同一行比较。
- Top 10 找调查入口，7 日平均看方向是否持续。
- 最大回撤不是看最后赚多少，而是看中途会不会把你逼到提前退出。
