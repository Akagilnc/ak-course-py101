# L4

## 定位

L4 的前半主题：读取 JSON 文件，把结构化数据变成可保存的报告。

L3 已经看过 API 返回的 JSON，也讲过 dict / list 的取值。L4 把这件事落到本地文件：打开 `lesson4.json`，找到海外疫情汇总数据，先保存成 `txt`，再保存成 `xlsx`。

- 输入：本地 `lesson4.json`。
- 读取：`json.load(file)` 把 JSON 文件变成 Python 数据。
- 取值：用 dict / list 的方式找到 `data -> othertotal`。
- 输出：第一步写入 `l4_oversea_report.txt`，第二步写入 `l4_oversea_report.xlsx`。
- 课堂重点：JSON 不是新魔法，本质还是 dict 和 list；文件输出可以从纯文字走到表格。

## 时间结构

总时长约 2.5 小时。

### 前半

- 课前热身：复习 L1-L3 的函数、`if`、`for`、list、dict、`append()`、写文件、JSON。
- 认识 `lesson4.json`：先看最外层结构，再找到 `data` 和 `othertotal`。
- 第一步：读取 JSON，生成海外疫情汇总文字，保存到 `txt`。
- 第二步：读取同一份 JSON，把汇总指标保存到 Excel。

## 前半结构

1. 课前热身：L1-L3 复习，重点叫醒 dict / list / JSON。
2. 章节页：从 JSON 到文件。
3. 看文件结构：`lesson4.json` 最外层有 `data_title` 和 `data`。
4. 找到目标数据：`raw_data["data"]["othertotal"]`。
5. 第一步目标：把海外疫情汇总保存到 `txt`。
6. 第二步目标：把同样的数据保存到 Excel。

## 课前热身：L1 + L2 + L3 Quiz

目标不是考试，是把 L4 会继续用到的基础能力叫醒。前半先复习变量、判断、循环、报告 list 和写文件；后半再少量复习 dict / list 结构。

展示时仍然参考 L2 / L3：每页一个完整代码块，下面放两道题。

### Quiz 1 / 7：变量和模板

```python
name = "海外疫情"
certain = "35270206"

text = "{} 累计确诊 {} 例".format(name, certain)
print(text)
```

1. `text` 里会保存哪句话？

- A. `海外疫情 累计确诊 35270206 例`
- B. `{} 累计确诊 {} 例`
- C. `name 累计确诊 certain 例`
- D. `35270206 累计确诊 海外疫情 例`

2. 这里的 `certain` 是什么类型？

- A. 整数
- B. 小数
- C. 字符串
- D. list

### Quiz 2 / 7：判断和报告文字

```python
change = -4

if change < 0:
    direction = "下跌"
else:
    direction = "上涨"

text = "今日{} {} 元".format(direction, 0 - change)
print(text)
```

3. 最后 `direction` 是什么？

- A. `上涨`
- B. `下跌`
- C. `-4`
- D. `4`

4. 最后一行会输出什么？

- A. `今日下跌 -4 元`
- B. `今日上涨 4 元`
- C. `今日下跌 4 元`
- D. `今日上涨 -4 元`

### Quiz 3 / 7：list 和下标

```python
row = ["累计确诊", "35270206"]

name = row[0]
value = row[1]

print(name, value)
```

5. `row[0]` 取到什么？

- A. `累计确诊`
- B. `35270206`
- C. `name`
- D. `value`

6. 这段代码最后会打印什么？

- A. `累计确诊 35270206`
- B. `35270206 累计确诊`
- C. `row[0] row[1]`
- D. `name value`

### Quiz 4 / 7：for 循环和报告列表

```python
rows = [
    ["累计确诊", "35270206"],
    ["累计死亡", "1036359"],
    ["累计治愈", "26340847"],
]

reports = []
for row in rows:
    text = "{} {} 例\n".format(row[0], row[1])
    reports.append(text)
```

7. 这段循环会执行几次？

- A. 1 次
- B. 2 次
- C. 3 次
- D. 不确定

8. 最后 `reports` 里有几条文字？

- A. 0 条
- B. 1 条
- C. 2 条
- D. 3 条

### Quiz 5 / 7：写入 txt 文件

```python
reports = [
    "累计确诊 35270206 例\\n",
    "累计死亡 1036359 例\\n",
]

file = open("report.txt", "w", encoding="utf-8")
file.writelines(reports)
file.close()
```

9. `writelines(reports)` 会做什么？

- A. 把 list 里的文字写入文件
- B. 只写入第一条文字
- C. 读取文件内容
- D. 删除 `reports`

10. `"w"` 模式对旧文件有什么影响？

- A. 只会在旧内容后面追加
- B. 如果文件已存在，会覆盖旧内容
- C. 只能读取，不能写入
- D. 会自动生成 Excel

### Quiz 6 / 7：dict 取值

```python
summary = {
    "certain": "35270206",
    "die": "1036359",
    "recure": "26340847",
}

print(summary["die"])
```

11. `summary["die"]` 会取到什么？

- A. `35270206`
- B. `1036359`
- C. `26340847`
- D. `die`

12. 如果要取治愈人数，应该写哪一句？

- A. `summary["recure"]`
- B. `summary["cure"]`
- C. `summary[2]`
- D. `summary.recure`

### Quiz 7 / 7：两层 dict

```python
data = {
    "mtime": "2020-10-05 21:01:00",
    "othertotal": {
        "certain": "35270206",
        "die": "1036359",
    }
}

total = data["othertotal"]
print(total["certain"])
```

13. `data["othertotal"]` 取到的是什么？

- A. 一个 dict
- B. 一个 list
- C. 字符串 `"othertotal"`
- D. `1036359`

14. 最后一行会输出什么？

- A. `othertotal`
- B. `certain`
- C. `35270206`
- D. `1036359`

答案：`1.A 2.C 3.B 4.C 5.A 6.A 7.C 8.D 9.A 10.B 11.B 12.A 13.A 14.C`

## 章节页

`#1 从 JSON 到文件`

How to read JSON and save reports?

L3 看过接口返回的 JSON；L4 直接读取本地 JSON 文件。

## 认识 lesson4.json

先打开文件看结构，不急着写代码。

```json
{
    "data_title": "fymap",
    "data": {
        "mtime": "2020-10-05 21:01:00",
        "othertotal": {
            "certain": "35270206",
            "die": "1036359",
            "recure": "26340847",
            "ecertain": "7893000"
        }
    }
}
```

实际文件里内容很多，但前半只关心这条路径：

```python
raw_data["data"]["othertotal"]
```

### 字段说明

- `mtime`：数据更新时间。
- `othertotal`：海外疫情汇总。
- `certain`：累计确诊。
- `die`：累计死亡。
- `recure`：累计治愈。
- `ecertain`：现存确诊。

## 前置知识：读取 JSON 文件

```python
import json

file = open("lesson4.json", encoding="utf-8")
raw_data = json.load(file)
file.close()
```

讲解重点：

- `import json`：把 JSON 工具拿进来。
- `open("lesson4.json", encoding="utf-8")`：打开本地 JSON 文件。
- `json.load(file)`：从文件里读取 JSON，并转成 Python 的 dict / list。
- 这里是 `json.load(file)`，L3 API 那里是 `json.loads(text)`；一个读文件，一个读字符串。

## 找到 total 数据

```python
data = raw_data["data"]
total = data["othertotal"]

print(total["certain"])
print(total["die"])
print(total["recure"])
print(total["ecertain"])
```

标准输出：

```text
35270206
1036359
26340847
7893000
```

所以呢：

- JSON 文件读进来以后，不需要切字符串。
- 只要路径找对，就可以像读字典一样读字段。
- `total` 是一个小 dict，第一次上手先处理它，不进入更深的国家列表。

## 第一步：保存海外疫情汇总到 txt

### 目标

从 `lesson4.json` 里取出海外汇总数据，生成一段可以直接读的文字，写入 `l4_oversea_report.txt`。

### 第一步代码

```python
import json

file = open("lesson4.json", encoding="utf-8")
raw_data = json.load(file)
file.close()

data = raw_data["data"]
time = data["mtime"]
total = data["othertotal"]

reports = []
reports.append("截至{}，海外疫情汇总：\n".format(time))
reports.append("累计确诊 {} 例\n".format(total["certain"]))
reports.append("现存确诊 {} 例\n".format(total["ecertain"]))
reports.append("累计死亡 {} 例\n".format(total["die"]))
reports.append("累计治愈 {} 例\n".format(total["recure"]))

file = open("l4_oversea_report.txt", "w", encoding="utf-8")
file.writelines(reports)
file.close()
```

### 运行后得到的 `l4_oversea_report.txt`

```text
截至2020-10-05 21:01:00，海外疫情汇总：
累计确诊 35270206 例
现存确诊 7893000 例
累计死亡 1036359 例
累计治愈 26340847 例
```

### Recap

- `json.load(file)` 负责把 JSON 文件读成 Python 数据。
- `raw_data["data"]["othertotal"]` 是这次最关键的路径。
- `reports` 仍然是 L3 的老办法：先把文字放进 list，再一次性写入文件。
- `txt` 适合给人读，但不适合继续排序、筛选、做表格处理。

## 第二步：保存海外疫情汇总到 Excel

### 目标

同样的数据，换成表格输出。

Excel 里应该长这样：

| 指标 | 数值 |
| --- | --- |
| 累计确诊 | 35270206 |
| 现存确诊 | 7893000 |
| 累计死亡 | 1036359 |
| 累计治愈 | 26340847 |

### 前置知识：DataFrame

```python
import pandas as pd

rows = [
    ["累计确诊", "35270206"],
    ["累计死亡", "1036359"],
]

df = pd.DataFrame(rows, columns=["指标", "数值"])
df.to_excel("l4_oversea_report.xlsx", index=False, sheet_name="汇总")
```

讲解重点：

- `pd` 是 `pandas` 的常用简称。
- `df` 是这张表，先理解成“Python 里的 Excel 表格”。
- `pd.DataFrame(rows, columns=["指标", "数值"])`：用 `rows` 生成表，并指定列名。
- `to_excel("文件名.xlsx")`：保存成 Excel 文件。
- `index=False`：不保存自动生成的行号。
- `sheet_name="汇总"`：设置工作表名称。

## 第二步代码

```python
import json
import pandas as pd

file = open("lesson4.json", encoding="utf-8")
raw_data = json.load(file)
file.close()

data = raw_data["data"]
total = data["othertotal"]

rows = [
    ["累计确诊", total["certain"]],
    ["现存确诊", total["ecertain"]],
    ["累计死亡", total["die"]],
    ["累计治愈", total["recure"]],
]

df = pd.DataFrame(rows, columns=["指标", "数值"])

df.to_excel("l4_oversea_report.xlsx", index=False, sheet_name="汇总")
```

### 运行后得到的 Excel

文件名：

```text
l4_oversea_report.xlsx
```

表格内容：

| 指标 | 数值 |
| --- | --- |
| 累计确诊 | 35270206 |
| 现存确诊 | 7893000 |
| 累计死亡 | 1036359 |
| 累计治愈 | 26340847 |

### Recap

- `txt` 是文字报告，适合直接阅读。
- `xlsx` 是表格报告，适合继续加工。
- 代码前半段没有变：还是读取 JSON，找到 `total`。
- 输出方式变了：从 `writelines()` 换成 `DataFrame` 和 `to_excel()`。
