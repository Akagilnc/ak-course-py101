# 定义一个求圆的面积的函数
def get_round_area(r):
    # 定义pi，获得半径
    pi = 3.14
    # 计算面积
    area = pi*r**2
    # 输出结果
    return area


# r = input("please input r: ")
# r = int(r)
# result = get_round_area(r)
# print(result)


# 定义一个获得全名的函数
def get_full_name(f_name, l_name):
    # 姓+名 为全名
    full_name = l_name + f_name
    # 输出全名
    return full_name


# # 获得姓，名
# f_n = input('plz input first name: ')
# l_n = input('plz input last name: ')
# # 调用函数并打印在屏幕上
# full_name = get_full_name(f_n, l_n)
# print(full_name)


# 定义函数
def get_answer(number):
    # 计算平方
    # 计算立方
    result1 = number ** 2
    result2 = number ** 3
    # 输出结果
    return result1, result2


# # 获取用户的输入，并转换为数字
# number = int(input('input a number: '))
# # 调用函数并且打印结果
# r1, r2 = get_answer(number)
# print(r1, r2)


# 定义函数、
def odd_or_even(number):
    # 对2求模，如果为1
    if number % 2 == 1:
        # 输出奇数
        return 'odd'
    # 否则
    else:
        # 输出偶数
        return 'even'


# # 获取用户输入
# number = int(input('input a number: '))
# # 调用函数，打印结果
# print(odd_or_even(number))


def is_divisible_3(num):
    # 如果对3求模，结果为0
    if num % 3 == 0:
        # 输出被3整除
        return 'is divisible by 3'
    # 否则
    else:
        # 输出提示
        return 'sorry but no'


# # 获取用户输入
# number = int(input('input a number: '))
# # 调用函数，打印结果
# print(is_divisible_3(number))


def check_pass():
    # 获取用户的输入
    noun = input('plz input your password: ')
    # 如果是yes
    if noun == 'yes':
        return 'you are wrong'
    # 如果是no
    if noun == 'no':
        return 'no, not you'
    # 如果是chengfei
    if noun == 'chengfei':
        return 'yes you are'
    # 否则
    else:
        return "???"

#
# # 调用并打印
# print(check_pass())


import random
def guess_number():
    # 生成答案1-10随机数字，次数 1
    n = 1
    answer = random.randint(1, 10)
    # 获得用户的猜测
    number = int(input('plz input a number: '))
    # 如果 猜测不等于答案
    while number != answer:
        # 如果猜测大于答案
        if number > answer:
            # 输出猜大了，并且继续猜
            number = int(input('too big, guess again: '))
        # 否则
        else:
            # 输出猜小了，并且继续猜
            number = int(input('too small, guess again: '))
        n += 1

    # 如果是第一次猜对
    if n == 1:
        # 提示特别 棒
        print('棒！')
    # 输出 第几次猜对的
    else:
        print('你在第{}次猜对的'.format(n))


guess_number()