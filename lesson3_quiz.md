# lesson3 quiz

1. 一个字典包括key fow 和 值 43， 看起来应该是怎样的
    
    ('fow': 43)
    
    ['fow': 43]
    
    ['fow', 43]
    
    {'fow': 43}
    
    {fow : 43}

2. 字典和列表的主要区别是什么

    都可以用[]的方式来取值
    
    列表有序字典无序
    
    都可以存储多个元素
    
    都用[]表示

3. 如果spam是{'bar': 100}，当试图访问spam['foo']，会发生什么

    None
    
    TypeError
    
    KeyError
    
    IndexError

4. 如果一个字典保存在spam中，表达式'tiger' in spam 和 'tiger' in spam.keys()有什么区别

    前者表示在keys和values中寻找，后者只在keys中寻找
    
    前者在整个字典里寻找，后者只在values中寻找
    
    前者在values中寻找，后者在keys中寻找
    
    前者在整个字典寻找，后者只在values中寻找
    
    前者在keys中寻找，后者在values中寻找
    
    以上都不对

5. 写一段代码，如果一个字典对象 spam 的 key 'status' 不存在，则设置为 'unknown'
    
    ```python
         spam['status] = 'unknown'
    ```
    
    ```python
         if not spam['status']:
             spam['status'] = 'unknown'
    ```
   
    ```python
         if 'status' not in spam:
             spam['status'] = 'unknown'
    ```
    
    ```python
         if 'status' not in spam.keys():
             spam['status'] = 'unknown'
    ```
    
6. 假定spam为列表['a', 'b', 'c', 'd']
    
    spam[int('3'*2)/11]的值为多少？
    
    spam[-1]的值为多少
    
    spam[:1]的值为多少

7. 对于spam = [{1: 2}, {2: 4}, {3: 8}]，如何拿到8这个数字
    
    ```python
    for item in spam:
        if 8 in item:
            print(item)
    ```    
    
    ```python
    print(spam[3])
    ```       
   
    ```python
    spam[2][3]
    ```
   
    ```python
    for temp in spam:
        if temp == 8:
            print(8)
    ```

8. 对于spam = {'name': 'Curry', 'age': '32', 'kids': [{'name': 'Riley'}, {'name': 'Canon'}, {'name': 'Ryan'}]}
如何打印出孩子们的名字？    