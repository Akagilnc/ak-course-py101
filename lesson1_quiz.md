# lesson1_quiz

第二节课课前热身。目标不是考试，是把 L1 里最重要的几个概念叫醒。

## 1. 函数什么时候真正运行？

下面哪一句会让函数里的代码真正执行？

```python
def get_round_area(r):
    return 3.14 * r ** 2
```

A. 写下 `def get_round_area(r):` 的时候  
B. 写完整个函数以后自动运行  
C. 调用 `get_round_area(5)` 的时候  
D. 写下 `return` 的时候

## 2. 哪一行把函数结果保存到了变量里？

```python
def get_round_area(r):
    return 3.14 * r ** 2

result = get_round_area(5)
print(result)
```

A. `def get_round_area(r):`  
B. `return 3.14 * r ** 2`  
C. `result = get_round_area(5)`  
D. `print(result)`

## 3. `=` 和 `==` 分别在做什么？

```python
number = 6
number == 6
```

A. 两个都是赋值  
B. 两个都是判断是否相等  
C. `=` 是赋值，`==` 是判断是否相等  
D. `=` 是判断是否相等，`==` 是赋值

## 4. 下面哪一行会打印变量里的内容？

```python
stock_name = "贵州茅台"
```

A. `print(stock_name)`  
B. `print("stock_name")`  
C. `stock_name(print)`  
D. `"贵州茅台" = stock_name`

## 5. `input()` 拿到的内容通常是什么类型？

```python
r = input("input r pls: ")
```

A. 整数  
B. 小数  
C. 字符串  
D. 布尔值

## 6. 下面哪一句是在判断偶数？

A. `number / 2 == 0`  
B. `number % 2 == 0`  
C. `number = 2 == 0`  
D. `number ** 2 == 0`

## 7. 这段代码会输出什么？

```python
yesterday = 1709
today = 1705
change = today - yesterday

print(change)
```

A. `4`  
B. `-4`  
C. `1705`  
D. `1709`

## 8. 同样跌 4 元，为什么还要看涨跌幅？

A. 因为涨跌幅看起来更高级  
B. 因为不同价格的股票，跌同样的钱，严重程度可能不同  
C. 因为涨跌金额没有意义  
D. 因为股票只能看百分比，不能看金额

## 老师参考

1. C
2. C
3. C
4. A
5. C
6. B
7. B
8. B
