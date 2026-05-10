# 定义函数
def get_round_area(r):
    # 定义pi
    pi = 3.14
    # 计算面积
    area = pi * r ** 2
    # 输出结果
    return area


# r = input("pls input r: ")
# r = int(r)
# result = get_round_area(r)
# print(result)


# 定义函数，2个输入 姓 名
def get_fullname(xing, ming):
    # 获得全名 姓+名
    f_name = xing + ming
    # 输出结果
    return f_name


# # 调用函数
# xing = input('input xing: ')
# ming = input('input ming: ')
# result = get_fullname(xing, ming)
# # 打印结果
# print(result)


# 定义函数
def get_answer(number):
    # 计算平方
    an1 = number ** 2
    # 计算立方
    an2 = number ** 3
    # 返回平方 和 立方
    return an1, an2


# # 获得用户输入，转换为int
# num = input('input a number: ')
# num = int(num)
# # 调用函数，获得结果
# re1, re2 = get_answer(num)
# # 打印结果
# print(re1, re2)


# 定义函数
def odd_or_even(number):
    # 如果能被2整除
    if number % 2 == 0:
        # 输出 even
        return 'even'
    # 否则
    else:
        # 输出 odd
        return 'odd'


# # 获得用户输入的数字
# num = int(input('give me a number:'))
# # 调用函数并打印结果
# print(odd_or_even(num))


    # 如果能被3 整除
        # 输出 divisible by 3
    # 否则
        # 输出 sorry but no


# 获得用户输入的数字
# 调用函数并打印结果