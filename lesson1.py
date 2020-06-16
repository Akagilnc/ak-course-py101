def get_round_area(input_r):
    # 定义pi
    pi = 3.14
    # 转化半径为float
    r = float(input_r)
    # 计算面积
    area = pi * r ** 2
    # 输出结果
    return area


def odd_or_even(input_number):
    # 判断奇偶叔
    # 如果是偶数
    if input_number % 2 == 0:
        # 返回even
        return 'even'
    # 否则
    else:
        # 返回odd
        return 'odd'


# r = input('Input r: ')
# area = get_round_area(r)
# print(area)

# 获取用户的输入，转化为数字

number = input('input a number: ')
number = int(number)
result = odd_or_even(number)
print(result)
