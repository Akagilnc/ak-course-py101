# Lesson5 Quiz

1. 如何初始化一个DataFrame, 
    ```python
    import pandas as pd
    
    df = DataFrame()
    
    df = pd.dataFrame()
    
    df = pd.DataFrame()
    
    df = pd.Dataframe()
    ```
   
    <details>
    <summary>答案</summary>
    
    答案为3. 1是因为没有pd. 
    
    2和4 都是大小写有错误
    </details>
    
2. 对于 `import pandas as pd` 以下说法正确的是？
    
    引入了pandas这个外部包
    
    引入了pd这个外部包
    
    调用需要写pandas.xxx()
    
    调用需要写pd.xxx()   
    
    <details>
    <summary>答案</summary>
    
    答案为1和4 
    
    2 pd 只是一个别名
    
    3 定义了别名就只能用别名来调用了
    
    </details>
    
3. 对于一个 DataFrame df , df['x']是在做什么？
    
    取得key为'x'的value
    
    取第x个元素
    
    取包含'x'的列
    
    取列名为'x'的列

4. 对于DataFrame.append()的描述正确的为：
    
    df.append(x)即可把x添加到df里面去
    
    df.append()可以把一个df添加进另外一个df
    
    df.append()没有返回值
    
    df.append()和list.append()的工作方式不同

5. 对于初始化 DataFrame df 时， `df = pd.DataFrame(data, columns=['1', '2', '3'])` 是在做什么

    新建3列，列名分别为1, 2, 3
    
    从原始数据中，只拿列名为1, 2, 3的
    
    从原始数据中，只拿行名为'1', '2', '3'的
    
    从原始数据中，只拿列名为'1', '2', '3'的
    
6. 对于已知的`DataFrame df，df.sum()` 的描述正确的是？
    
    只能对一列数字(整数或浮点数或其它数据类型)求和
    
    只能对所有数字(整数或浮点数或其它数据类型)的列求和
    
    对所有的行求和,但是忽略包含NaN的列
    
    对所有的列尝试求和，包括NaN的列
    
    最终返回的是一个Series

7. `df.to_excel()` 的描述正确的是？

    第一个参数可以传文件名，但是必须要是'xlsx'结尾的
    
    `index=True` 参数可以去掉自动生成的数字参数
    
    第一个参数可以传入一个pd.ExcelWriter
    
    第一个参数可以用`'{}.json'.format(x)`的方式传入

8. 对于`writer = pd.ExcelWriter('x.xlsx', engine='openpyxl')`，以下描述正确的是：

    之后我可能会把数据存入到x.xlsx的默认sheet里面
    
    后续我可以在x.xlsx文件中多次写入数据
    
    writer有可能被我用来作为`df.to_csv()`的参数

    当我调用`df.to_excel(writer)`时，我必须还需要加上`sheet_name='xxx'`这个参数才可以成功



