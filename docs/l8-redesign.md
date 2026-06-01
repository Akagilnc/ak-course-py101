# L8

## 定位

L8 是收官课：把一份嵌套的疫情数据整理成城市明细，再汇总到省份层面，最后做一份能讨论“结构差异”的 Excel 报告。

前面几节课已经反复做过读取、重命名、转类型、保存 Excel。L8 不再把这些当主角，而是把重点放在：一份数据可以先变成长表，再用 `groupby` 回答不同层级的问题。

- 输入：`lesson4.json` 里的省份和城市疫情数据。
- 处理：从省份列表里展开城市明细，按省份汇总，比较总量、典型水平和集中度。
- 输出：`l8_city_detail.xlsx`、`l8_province_report.xlsx`。
- 课堂重点：总数高、平均高、中位数高、集中度高，不是一回事。

## 时间结构

总时长约 2.5 小时。

### 前半

- 课前热身：复习函数、字典/list 取值、DataFrame、新增列、筛选、排序、导出多 sheet。
- 主任务：生成一份城市明细和省份结构报告。
- Step 1：把嵌套城市数据展开成一张城市明细表。
- Step 2：按省份分组，计算总数、城市数量、平均数、中位数。
- Step 3：加入“最大地区占比”，把不同角度的结果写进同一个 Excel。

### 后半

后半继续 3 个案例，学生不跟敲，主要看表格、讨论、拍照问 AI。

- 案例 1：平均数和中位数为什么会讲出不同故事。
- 案例 2：总量高和集中度高为什么不是一回事。
- 案例 3：让 AI 写报告，但输入必须给够表格和问题。

## 课前热身方向

建议 8-10 页，每页完整代码块 + 两题。

重点复习：

- `def` / 参数 / 返回值。
- 字典取值：`data["list"]`。
- list 循环：`for item in items:`。
- `pd.DataFrame(rows)`。
- `df["新列"] = ...`。
- 条件筛选：`df[df["现存确诊"] > 0]`。
- `sort_values()` / `head()`。
- `with pd.ExcelWriter(...) as writer`。

## 前半：城市明细到省份结构报告

### 章节页

`#1 从城市到省份`

One table, many levels.

### 主任务

函数名：

```python
make_province_structure_report(file_name)
```

输入：

- 一份疫情 JSON 数据。

输出：

- `l8_city_detail.xlsx`
- `l8_province_report.xlsx`

目标：

- 从嵌套数据里整理出城市明细。
- 按省份汇总城市数据。
- 比较总数、平均数、中位数和集中度。

### 数据页

JSON 里大概是这样的结构：

```text
省份
  城市 1
  城市 2
  城市 3
```

我们要先把它整理成一张表：

```text
省份    地区        累计确诊    现存确诊    累计治愈    累计死亡
北京    朝阳区      77          0           77          0
北京    海淀区      82          0           82          0
广东    广州        377         8           368         1
```

这一步的意义：

- 原始数据适合机器保存。
- 表格数据适合人看，也适合 pandas 继续分析。

## Step 1：展开城市明细

### 目标

把“省份下面套城市”的结构，展开成一张城市明细表。后面所有分析都从这张表开始。

### 代码

```python
import json
import pandas as pd


def make_province_structure_report(file_name):
    file = open(file_name, encoding="utf-8")
    raw_data = json.load(file)
    file.close()

    provinces = raw_data["data"]["list"]
    rows = []

    for province in provinces:
        province_name = province["name"]
        cities = province["city"]

        if len(cities) == 0:
            rows.append({
                "省份": province_name,
                "地区": province_name,
                "累计确诊": int(province["value"]),
                "现存确诊": int(province["econNum"]),
                "累计治愈": int(province["cureNum"]),
                "累计死亡": int(province["deathNum"]),
            })

        for city in cities:
            rows.append({
                "省份": province_name,
                "地区": city["name"],
                "累计确诊": int(city["conNum"]),
                "现存确诊": int(city["econNum"]),
                "累计治愈": int(city["cureNum"]),
                "累计死亡": int(city["deathNum"]),
            })

    city_df = pd.DataFrame(rows)
    city_df.to_excel("l8_city_detail.xlsx", index=False)
```

### Recap

- `rows = []`：先准备一个空列表，用来收集每一行。
- 外层 `for province in provinces`：逐个省份处理。
- 内层 `for city in cities`：逐个地区处理。
- `if len(cities) == 0`：没有城市列表的地区，用省份本身补成一行。
- `rows.append({...})`：把一个地区整理成一行。
- `pd.DataFrame(rows)`：把很多行变成一张表。

## Step 2：按省份汇总

### 目标

同一张城市明细表，可以按省份重新汇总。这里开始出现 L8 最重要的新概念：分组统计。

### 代码

```python
    city_df = pd.read_excel("l8_city_detail.xlsx")

    province_df = city_df.groupby("省份").agg(
        累计确诊总数=("累计确诊", "sum"),
        现存确诊总数=("现存确诊", "sum"),
        地区数量=("地区", "count"),
        平均每地确诊=("累计确诊", "mean"),
        中位数每地确诊=("累计确诊", "median"),
        最大地区确诊=("累计确诊", "max"),
    ).round(2)

    province_df = province_df.reset_index()
```

### Recap

- `groupby("省份")`：把同一个省份的地区放到一组。
- `sum`：看总量。
- `count`：看这一组有多少个地区。
- `mean`：看平均水平。
- `median`：看中间位置的水平。
- `max`：看这一组里最大的地区。
- `reset_index()`：把分组后的省份重新变回普通列。

### 真实输出预览

```text
省份    累计确诊总数    地区数量    平均每地确诊    中位数每地确诊    最大地区占比
湖北    68139           17          4008.18         931.0           73.88%
香港    5113            1           5113.00         5113.0          100.00%
广东    1835            20          91.75           22.0            39.56%
```

这里要让学生先看见：同一张城市明细表，被按省份重新组织以后，问题就变成了“每个省内部是什么结构”。

## Step 3：比较省份结构

### 目标

总数最高不一定代表每个地区都高。Step 3 加入“最大地区占比”，看看一个省份的数据主要集中在哪个地区。

### 代码

```python
    province_df["最大地区占比"] = (
        province_df["最大地区确诊"] / province_df["累计确诊总数"] * 100
    ).round(2)

    total_top = province_df.sort_values(
        by="累计确诊总数",
        ascending=False,
    ).head(10)

    median_top = province_df.sort_values(
        by="中位数每地确诊",
        ascending=False,
    ).head(10)

    concentration_top = province_df.sort_values(
        by="最大地区占比",
        ascending=False,
    ).head(10)

    with pd.ExcelWriter("l8_province_report.xlsx") as writer:
        city_df.to_excel(writer, sheet_name="城市明细", index=False)
        province_df.to_excel(writer, sheet_name="省份汇总", index=False)
        total_top.to_excel(writer, sheet_name="总数Top10", index=False)
        median_top.to_excel(writer, sheet_name="中位数Top10", index=False)
        concentration_top.to_excel(writer, sheet_name="集中度Top10", index=False)
```

最后调用：

```python
make_province_structure_report("lesson4.json")
```

### Recap

- `最大地区占比`：最大地区确诊数占全省总确诊数的比例。
- 总数 Top 10：看规模。
- 中位数 Top 10：看典型地区水平。
- 集中度 Top 10：看数据主要压在哪一个地区。
- 同一份明细表，可以导出多个观察角度。

### 结构预览

```text
省份    累计确诊总数    最大地区确诊    最大地区占比
广东    1835            726             39.56%
上海    1022            680             66.54%
```

按总量看，广东更靠前；按集中度看，上海更突出。排序列一换，课堂上要讨论的问题也跟着换。

## 后半：从汇总到判断

### 后半章节页

`#2 同一份数据，不止一个答案`

换一个统计口径，问题就变了。

## 案例 1：平均数 91.75，为什么中位数只有 22？

### 目标

理解平均数和中位数的差别。平均数容易被极端值拉动，中位数更像“典型水平”。

### 展示数据

广东 20 个地区参与计算；下面只列几个代表值，先看差异有多大。

```text
广东部分地区    累计确诊
河源            5
汕尾            6
潮州            7
韶关            10
清远            12
深圳            471
广州            726

广东 20 个地区：
平均每地确诊 91.75
中位数每地确诊 22.0
```

### 问题

- 如果报告里只写“平均每地 91.75”，读者可能形成什么印象？
- 中位数 22 更接近哪一类地区的状态？
- 广州、深圳这种高值应该混进一句平均数里，还是单独拿出来解释？

### 所以呢

- 平均数适合回答“整体摊下来是多少”。
- 中位数适合回答“多数地区大概什么水平”。
- 高值单独讲，典型水平单独讲，报告会更清楚。

### AI 可选

```text
广东部分地区累计确诊：
河源 5，汕尾 6，潮州 7，韶关 10，清远 12，深圳 471，广州 726。

广东 20 个地区：平均每地确诊 91.75，中位数每地确诊 22.0。

请解释：为什么平均数和中位数会讲出不同故事？
用普通人能听懂的话回答。
```

参考输出：

```text
广东多数地区的确诊数并不高，但广州和深圳明显高很多。
平均数会把广州、深圳一起算进去，所以被拉高到 91.75。
中位数是 22，更接近多数地区的典型水平。

所以这两个数字回答的是不同问题：平均数看整体摊下来，中位数看典型地区。
```

## 案例 2：同一张表，先看哪一列？

### 目标

理解“最大地区占比”。它回答的不是总量问题，而是结构问题：数据主要集中在哪个地方。

### 展示数据

```text
省份    累计确诊总数    最大地区确诊    最大地区占比
广东    1835            726             39.56%
上海    1022            680             66.54%
```

### 问题

- 如果你关心整体规模，应该优先解释哪一个省？
- 如果你关心压力集中到单个地区，应该优先追问哪一个省？
- 这两种排序，分别会引导你去看“全省问题”还是“单点问题”？

### 所以呢

- 总量回答“盘子有多大”。
- 集中度回答“压力压在少数地区，还是分散在多地”。
- 排名之前，先说清楚问题，再决定按哪一列排序。

## 案例 3：让 AI 写报告

### 目标

最后一次 AI 演示：让 AI 把表格写成给普通人看的说明。重点不是让 AI 代替判断，而是把输入给完整，让它能围绕正确问题表达。

### AI 输入页

拍照页要同时包含表格和任务。

```text
省份    累计确诊总数    中位数每地确诊    最大地区占比
湖北    68139           931.0             73.88%
广东    1835            22.0              39.56%
上海    1022            12.0              66.54%

请写一段给普通同事看的数据说明：
1. 分别说明总量、典型水平、集中度。
2. 说明为什么不能只看第一列。
3. 结尾给一句最值得继续追问的问题。
```

### 参考输出

```text
这张表不是只在比较哪个省总数最高。湖北累计确诊总数最高，说明整体规模最大；
湖北的中位数每地确诊也最高，说明典型地区水平也更突出；
上海最大地区占比达到 66.54%，说明它比广东更集中在少数地区。

所以，只看累计确诊总数会漏掉结构差异。下一步最值得追问的是：
湖北为什么总量和典型水平都高，上海为什么集中度这么高。
```

## 收官回顾

- 原始 JSON 可以整理成表格。
- 表格可以按地区、按省份、按时间重新组织。
- 排序、筛选、分组、导出 Excel，是数据分析最常见的几步。
- 计算结果不是终点。真正有价值的是：你用哪个指标回答哪个问题。
