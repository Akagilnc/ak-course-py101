# L2

## 定位

L2 承接 L1 没展开的循环部分：前半用“猜数字游戏”理解程序可以重复做事；后半用股票数据理解循环可以批量处理一批相似数据。

- 前半只做一个动手项目：猜数字游戏。
- 核心知识点：`while`、`random`、计数器、`if` 分支。
- 后半回到股票数据：用 `for` 批量处理多只股票。
- 课堂重点不是写很多代码，而是让学员看懂“程序为什么要重复做事”，以及数字算出来以后怎么解释。

## 统一例子结构

后续每个例子尽量按这个结构组织，个别页可以省略，但主线不应跳过。

1. 目标：先说这个例子要解决什么问题。
2. 前置知识：只讲马上会用到的新东西。
3. 代码 / 运行：看代码或现场手写。
4. 输出：确认程序实际算出了什么。
5. 所以呢：把结果翻译成业务 / 数据判断。
6. AI 可选：让 AI 解释、检查、纠错或总结，但要有标准答案。

## 时间结构

总时长约 2.5 小时。

### 前半

- L1 回顾：函数、变量、`if`、`input()`、`int()`、股票涨跌幅。
- 讲清楚猜数字游戏规则。
- 引入 `while`：只要没猜对，就继续猜。
- 引入 `random.randint(1, 10)`：让电脑生成答案。
- 完成猜数字游戏，并补上“第一次猜中”的特殊提示。

### 后半

- 从猜数字过渡到股票：游戏里重复猜，数据里重复算。
- 讲清楚 `while` 和 `for` 的区别。
- 先补 `list`、下标、切片、`split()`。
- 例子 1：计算每只股票的涨跌额和涨跌幅。
- 例子 2：找出跌的钱最多、跌幅最大的股票。
- 例子 3：统计上涨和下跌数量，并讨论“所以呢”。
- AI 演示：用标准答案检查 AI；让 AI 处理行业统计；让 AI 找一个能运行但公式错的代码问题。

## 课前热身：L1 Quiz

目标不是考试，是把 L1 里最重要的概念叫醒。

### Quiz 1-2：函数和返回值

两道题共用这段完整代码：

```python
def get_round_area(r):
    return 3.14 * r ** 2

result = get_round_area(5)
print(result)
```

#### Quiz 1：函数什么时候真正运行？

- A. 写下 `def get_round_area(r):` 的时候
- B. 写完以后自动运行
- C. 调用 `get_round_area(5)` 的时候
- D. 写下 `return` 的时候

#### Quiz 2：哪一行把结果保存到变量里？

- A. `def get_round_area(r):`
- B. `return 3.14 * r ** 2`
- C. `result = get_round_area(5)`
- D. `print(result)`

### Quiz 3：`=` 和 `==` 分别在做什么？

```python
number = 6
number == 6
```

- A. 两个都是赋值
- B. 两个都是判断相等
- C. `=` 是赋值，`==` 是判断相等
- D. `=` 是判断，`==` 是赋值

### Quiz 4：哪句代码能打印变量里的内容？

```python
stock_name = "贵州茅台"
```

- A. `print(stock_name)`
- B. `print("stock_name")`
- C. `stock_name(print)`
- D. `"贵州茅台" = stock_name`

### Quiz 5：`input()` 拿到的内容通常是什么类型？

```python
r = input("input r pls: ")
```

- A. 整数
- B. 小数
- C. 字符串
- D. 布尔值

### Quiz 6：哪一句是在判断偶数？

- A. `number / 2 == 0`
- B. `number % 2 == 0`
- C. `number = 2 == 0`
- D. `number ** 2 == 0`

### Quiz 7：这段代码会输出什么？

```python
yesterday = 1709
today = 1705
change = today - yesterday
print(change)
```

- A. `4`
- B. `-4`
- C. `1705`
- D. `1709`

### Quiz 8：同样跌 4 元，为什么还要看涨跌幅？

- A. 因为涨跌幅看起来更高级
- B. 因为不同价格的股票，严重程度可能不同
- C. 因为涨跌金额没有意义
- D. 因为股票只能看百分比

答案：`1.C 2.C 3.C 4.A 5.C 6.B 7.B 8.B`

## 前半：猜数字游戏

### 章节页

- `#1 猜数字游戏`
- How to repeat until correct?
- L1 里电脑已经会判断；L2 让电脑重复判断。

### 游戏规则

- 电脑随机想一个 1 到 10 的整数。
- 你每次输入一个数字。
- 没猜中，电脑提示 `too big` 或 `too small`，然后继续猜。
- 猜中了，游戏结束；如果第一次就猜中，会有特殊提示。

### 概念页：while

```python
while guess != answer:
```

- `while`：只要条件成立，就重复执行。
- `!=`：不等于。
- 猜中以后，`guess != answer` 不成立，循环停止。

### 概念页：random

```python
import random

answer = random.randint(1, 10)
```

- `import random`：先把随机数工具拿进来。
- `random` 是 Python 自带的随机工具。
- `randint(1, 10)` 生成 1 到 10 之间的整数。
- 答案每次运行都可能不一样。

### IDE 手写：猜数字

```python
import random

def guess_number():
    answer = random.randint(1, 10)
    count = 1
    guess = int(input("guess: "))

    while guess != answer:
        if guess > answer:
            guess = int(input("too big, guess again: "))
        else:
            guess = int(input("too small, guess again: "))
        count += 1

    if count == 1:
        print("Good Job!")
    else:
        print("you got it at", count, "times")

guess_number()
```

讲解重点：

- `answer` 和 `guess` 都是变量，一个存答案，一个存本次输入。
- `import random`：使用随机工具前，先把工具导入。
- `int(input(...))`：复用 L1 的知识，输入文字要先转成整数。
- `if / else`：老知识，用来判断猜大了还是猜小了。
- `while guess != answer`：只要还没猜中，就继续执行缩进里的代码。
- `count += 1`：每多猜一次，次数就加一次。

## 后半：循环和股票数据

### 过渡：循环有什么用？

- 游戏：猜错一次，就再问一次，直到猜中。
- 股票：一只股票会算涨跌幅，13 只股票也用同一套算法。
- 现实：工资表、商品价格表、销售记录，本质上都是一批相似数据。

### while / for

`while`：

- 不知道要重复几次。
- 猜数字：不知道几次能猜中。

`for`：

- 有一批东西，每个处理一次。
- 股票数据：每一行都算一遍。

### list：什么是 list？

list 是一组数据。最明显的样子，是用 `[]` 把多个元素装在一起。

```python
x = ["贵州茅台", 1705, -0.23, True]
```

- `[]`：list 的外壳。
- `,`：元素之间用逗号隔开。
- 顺序：第一个、第二个、第三个。
- 类型：字符串、整数、小数、布尔值都能放。

### list：按顺序排好的东西

```python
x = ["表头", "贵州茅台", "招商银行", "五粮液", "泸州老窖", "平安银行"]

print(x[0])
print(x[1])
print(x[-1])
```

输出：

```text
表头
贵州茅台
平安银行
```

Python 从 0 开始数。`x[-1]` 是最后一个，东西很多时不用先数总共有几个。

### slice：切片

```python
x = ["表头", "贵州茅台", "招商银行", "五粮液", "泸州老窖", "平安银行"]

x[1:5]    # 从 1 到 5 前面：贵州茅台 到 泸州老窖
x[:5]     # 开头不写：从最前面开始
x[1:]     # 结尾不写：一直到最后
x[1:5:2]  # 每隔 2 个拿一次
```

`lines[1:]` 的意思就是：跳过第 0 行表头，从第 1 行股票数据开始。

### step：第三个数字是步伐

```python
x = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

print(x[1:7:2])
print(x[1:10:3])
```

输出：

```text
["1", "3", "5"]
["1", "4", "7"]
```

## 例子 1：把原始价格变成涨跌信息

### 目标

- 原始数据只有开盘价、收盘价、行业、成交额。
- 程序加工出涨跌额和涨跌幅。
- 先跑通，不急着写漂亮，先确认每只股票都能算出来。

### 前置知识：一行文字，拆成几个字段

```python
line = "贵州茅台, 白酒, 1709, 1705, 86.4"

name, industry, open_text, close_text, amount_text = (
    line.split(", ")
)
```

逗号左边到右边，刚好对应：名称、行业、开盘价、收盘价、成交额。

### 前置数据：stocks.txt

```text
股票名称, 行业, 开盘价格, 收盘价格, 成交额(亿元)
贵州茅台, 白酒, 1709, 1705, 86.4
招商银行, 银行, 35.00, 36.00, 42.8
五粮液, 白酒, 150.00, 153.00, 44.1
泸州老窖, 白酒, 140.00, 137.20, 31.6
平安银行, 银行, 10.00, 10.30, 18.9
兴业银行, 银行, 18.00, 17.80, 21.4
宁德时代, 新能源, 180.00, 174.00, 91.2
比亚迪, 新能源, 210.00, 214.00, 76.5
隆基绿能, 新能源, 18.00, 17.20, 33.6
工业富联, 科技, 25.00, 27.00, 58.9
京东方A, 科技, 4.00, 4.20, 25.4
中芯国际, 科技, 80.00, 78.00, 54.2
科大讯飞, 科技, 50.00, 51.50, 29.7
```

### 代码

```python
file = open("stocks.txt", encoding="utf-8")
lines = file.readlines()
file.close()

data_lines = lines[1:]  # 跳过第一行表头

for line in data_lines:
    name, industry, open_text, close_text, amount_text = (
        line.strip().split(", ")
    )

    open_price = float(open_text)
    close_price = float(close_text)
    change = round(close_price - open_price, 2)
    percent = round(change / open_price * 100, 2)

    print(name, change, percent, "%")
```

### 输出

```text
贵州茅台 -4.0 -0.23 %
招商银行 1.0 2.86 %
五粮液 3.0 2.0 %
```

这一版输出够直接，但还不像一段给人看的报告。

### 问题

- 原始数据里没有哪两个结果？
- 现在的输出适合自己检查，还是适合发给别人看？
- 如果想找“跌得最严重”的股票，还缺哪一步？

### 所以呢

- 原始数据只告诉我们开盘价和收盘价，还没有直接告诉我们“今天变化有多大”。
- 程序做的第一件有用的事，是从原始字段里算出新指标：涨跌额和涨跌幅。
- 简单输出适合老师和自己确认代码跑通；如果要给别人看，就要把结果组织成报告句子。
- 想找“最严重”的股票，靠眼睛扫很容易漏。让程序逐行计算、逐行比较，才是循环真正开始有价值的地方。

## 例子 2：让程序找出“最差”的股票

### 目标

- 上一例每只股票都算出了涨跌额和涨跌幅。
- 这一例不靠眼睛扫，让程序自己比较。
- 关键是先说清楚“最差”到底按什么标准判断。

### 前置知识：format()

```python
print(name, "（", industry, "）今日涨跌额是",
      change, "元，涨跌幅是", percent, "%。")

template = "{}（{}）今日涨跌额是 {} 元，涨跌幅是 {}%。"
print(template.format(name, industry, change, percent))
```

输出：

```text
贵州茅台 （ 白酒 ）今日涨跌额是 -4.0 元，涨跌幅是 -0.23 %。
贵州茅台（白酒）今日涨跌额是 -4.0 元，涨跌幅是 -0.23%。
```

两种写法都能输出报告句子，但模板更工整，也更容易批量复用。

### 前置知识：读文件三步

```python
file = open("stocks.txt", encoding="utf-8")
lines = file.readlines()
file.close()
```

- `open`：打开文件。
- `readlines`：把文件读成一组行。
- `close`：用完以后关掉文件。

### 前置知识：读文件不止一种读法

- `read()`：一次读完整个文件，得到一大段文字。
- `readline()`：一次只读一行。
- `readlines()`：一次读出所有行，得到一个 list。

### 前置知识：read()

```python
file = open("stocks.txt", encoding="utf-8")
text = file.read()
file.close()

print(text)
```

文件里每一行结尾都有一个看不见的 `\n`，`print()` 遇到它就换行。

### 前置知识：反斜杠

```python
print("贵州茅台\n招商银行")
print("名称\t收盘价")
print("他说：\"今天涨了\"")
print("文件位置：C:\\stocks.txt")
```

- `\n`：换行。
- `\t`：空一段距离。
- `\"`：在字符串里写双引号。
- `\\`：在字符串里写反斜杠本身。

### 解题思路

- 先准备两个空位置：跌的钱最多、跌幅最大。
- 每一行都算出涨跌额和涨跌幅。
- 更差时更新记录。最后留下来的就是答案。

### 代码

```python
file = open("stocks.txt", encoding="utf-8")
lines = file.readlines()
file.close()

data_lines = lines[1:]  # 跳过表头，只处理股票数据

worst_money_name, worst_percent_name = "", ""
worst_money_change, worst_percent = 0, 0

for line in data_lines:
    parts = line.strip().split(", ")
    name = parts[0]
    open_price = float(parts[2])
    close_price = float(parts[3])

    change = round(close_price - open_price, 2)
    percent = round(change / open_price * 100, 2)

    if change < worst_money_change:
        worst_money_name = name
        worst_money_change = change

    if percent < worst_percent:
        worst_percent_name = name
        worst_percent = percent

print("跌的钱最多： {} {}".format(worst_money_name, worst_money_change))
print("跌幅最大： {} {}%".format(worst_percent_name, worst_percent))
```

### 输出

```text
跌的钱最多： 宁德时代 -6.0
跌幅最大： 隆基绿能 -4.44%
```

### 所以呢

两个“最差”，回答的是两个问题：

- 跌的钱最多：看的是绝对金额。宁德时代从 180 跌到 174，跌了 6 元；如果持有 1000 股，账面少了 6000 元。
- 跌幅最大：看的是相对比例。隆基绿能只跌 0.8 元，但从 18 跌到 17.2，跌幅是 4.44%，波动反而更重。

先问清楚问题，再决定怎么算：

- 如果关心“账户少了多少钱”，要看涨跌额乘以持有股数。
- 如果关心“这只股票今天波动严不严重”，重点看涨跌幅。
- 如果要比较不同行业，还要把行业、成交额一起放进来。
- 没有唯一的“最差”。你想回答的是账户损失，还是价格波动，决定了应该看哪一个数字。

## 例子 3：不只找第一名，还要看整体

### 目标

- 例子 2 找出最差的一只股票。
- 例子 3 统计上涨和下跌数量，看整体分布。
- 总数有用，但总数不是全部答案。

### 前置知识：encoding

- 电脑保存文字时，底层其实保存的是数字。
- 编码就是“数字”和“文字”之间的对照表。
- `utf-8` 是最常用的编码之一，中文、英文、符号都能处理。
- 摩斯编码也是一种编码：不同的点和横，对应不同字母。

### 前置知识：mode

```python
open("stocks.txt", mode="r")
open("stocks.txt", mode="w")
open("stocks.txt", mode="a")
open("stocks.txt", mode="x")
```

- `r` 是 read：读取文件。默认就是 `r`，所以平时可以不写。
- `w` 是 write：写入文件；如果文件已经存在，会先清空原内容。
- `a` 是 append：追加到文件最后，不清空原内容。
- `x` 是 create：只创建新文件，文件已存在就报错。

### 代码

```python
file = open("stocks.txt", encoding="utf-8")
lines = file.readlines()
file.close()

data_lines = lines[1:]  # 跳过表头
up_count, down_count = 0, 0

for line in data_lines:
    parts = line.strip().split(", ")
    open_price = float(parts[2])
    close_price = float(parts[3])
    change = round(close_price - open_price, 2)

    if change > 0:
        up_count += 1
    if change < 0:
        down_count += 1

print("上涨数量： {}".format(up_count))
print("下跌数量： {}".format(down_count))
```

### 输出

```text
上涨数量： 7
下跌数量： 6
```

### 所以呢

上涨 7、下跌 6，能说明什么？

- 它说明这批股票里，上涨数量略多于下跌数量，但这只是“个数”层面的观察。
- 如果上涨的是小成交额股票，下跌的是宁德时代、贵州茅台这种大成交额股票，市场体感可能完全不同。
- 数量统计适合先看方向，但不能替代行业、成交额和涨跌幅。
- 下一步要问：上涨的集中在哪些行业？下跌的是不是权重更大的股票？这样才不会被“7 比 6”这个表面数字带偏。

## AI 可选演示

### AI 演示 1：让 AI 直接处理原始数据

拍照页给 `stocks.txt`，提问：

```text
请根据左边数据统计：
1. 哪只股票跌的钱最多
2. 哪只股票跌幅最大
3. 上涨数量和下跌数量

只给结论，不要投资建议。
```

标准答案：

```text
跌的钱最多：宁德时代，跌 6.0 元
跌幅最大：隆基绿能，跌 4.44%
上涨数量：7
下跌数量：6
```

课堂目标：

- 如果 AI 算对了，就是帮人类快速处理数据。
- 如果 AI 算错了，就拿程序输出当标准答案对照。
- 同一份数据，可以人工算、程序算、AI 算，结果要能互相检查。

### AI 演示 2：让 AI 按行业统计

拍照页给 `stocks.txt`，提问：

```text
请按行业统计上涨和下跌：
1. 一共有多少个行业
2. 每个行业有几只股票
3. 每个行业上涨几只、下跌几只
4. 哪个行业整体更强，哪个行业整体更弱

最后用两句话说明：
为什么只看总上涨数量还不够？
```

标准答案：

```text
一共有 4 个行业。

白酒：3 只，1 涨 2 跌
银行：3 只，2 涨 1 跌
新能源：3 只，1 涨 2 跌
科技：4 只，3 涨 1 跌

科技整体更强，白酒和新能源整体偏弱。
银行也有分化，不是所有银行股都上涨。

总数告诉我们整体温度；
分行业能看到结构差异。
```

### AI 演示 3：让 AI 找“能运行但逻辑错”的代码

拍照页：

```python
下面这段代码能运行，但结果逻辑可能有问题。
请找出问题，并给出修改后的代码。

stock_name = "隆基绿能"
open_price = 18.00
close_price = 17.20

change = close_price - open_price
percent = change / close_price * 100

print(stock_name, "涨跌幅：", percent, "%")
```

标准答案：

```python
stock_name = "隆基绿能"
open_price = 18.00
close_price = 17.20

change = close_price - open_price
percent = change / open_price * 100

print(stock_name, "涨跌幅：", percent, "%")
```

```text
隆基绿能 涨跌幅： -4.444444444444446 %
```

关键点：涨跌幅要除以变化前的价格，也就是开盘价；原代码除以收盘价，程序能跑，但逻辑错了。

## Recap

- `while` 适合“不知道要重复几次”的流程。
- `for` 适合“一批结构相同的数据”。
- `if` 让程序根据情况走不同路线。
- `readlines()` 把文件读成一行一行的 list。
- 程序的价值不是复制原始数据，而是计算、比较、生成可读结论。
- AI 可以辅助总结，但标准答案要能回到程序和数据。
