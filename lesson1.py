# 求圆的面积
def print_round_area():
    # 定义pi = 3.14
    pi = 3.14
    # 获取用户输入的r
    r = input('please input r: ')
    r = float(r)
    # pi * r 的平方
    area = pi * r ** 2
    print(area)


# 判断奇偶数
def odd_or_even():
    # 获取用户输入的数字
    number = int(input('please input a number: '))
    # 判断奇偶
    # 如果是偶数
    if number % 2 == 0:
        # 打印 even
        print('even')
    # 否则
    else:
        # 打印 odd
        print('odd')


print_round_area()
odd_or_even()
