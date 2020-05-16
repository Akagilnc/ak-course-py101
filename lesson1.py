# 求圆的面积
def get_round_area(input_r):
    # 定义pi的值
    pi = 3.14
    # 半径转换为float
    input_r = float(input_r)
    # 计算面积
    area = pi * input_r ** 2
    return area


# 定义一个判断奇偶数
def odd_or_even(input_number):
    # 把输入转换为int
    input_number = int(input_number)
    # 判断奇偶
    # 如果是偶数
    if input_number % 2 == 0:
        return 'even'
    # 否则
    else:
        return 'odd'
# # 获取用户输入的半径
# r = input('input r: ')
# result = get_round_area(r)
# # 打印结果
# print(result)

number = input('input a number: ')
result = odd_or_even(number)
print(result)
