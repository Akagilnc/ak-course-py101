# 定义函数
def get_answer(number):
    # 求他的平方
    result1 = number ** 2
    # 求他的立方
    result2 = number ** 3
    # 输出平方和立方
    return result1, result2

# # 获取用户的输入
# num = input("plz input a number: ")
# # 转换为数字
# num = int(num)
# # 调用函数并打印结果
# r1, r2 = get_answer(num)
# print(r1, r2)


# 定义判断奇偶的函数
def odd_or_even(num):
    # 如果 被2求模等于0
    if num % 2 == 0:
        # 输出 even
        return 'even'
    # 否则
    else:
        # 输出 odd
        return 'odd'


# 获取用户的输入
# 转换为整数
# number = int(input('plz input a number: '))
# 调用函数，打印结果
# print(odd_or_even(number))


# 定义函数
def is_divisible_3(number):
    # 如果被3求模等于0
    if number % 3 == 0:
        # 输出可以被3整除
        return 'divisible by 3'
    # 否则
    else:
        # 输出不可以的信息
        return 'sorry but no'


# 获得用户输入并转换为整数
# num = int(input('plz give a number: '))
# # 调用函数并打印结果s
# print(is_divisible_3(num))


# 定义一个函数()
def check_cert(word):
    # 如果输入是’yes’，输出 ‘you are wrong’
    if word == 'yes':
        return 'you are wrong'
    # 如果输入是’no’, 输出’no, not you'
    if word == 'no':
        return 'no, not you'
    # 如果输入是’chengfei’, 输出’yes you are’
    if word == 'chengfei':
        return 'yes you are'
    # 否则，输出’？？？’
    else:
        return '???'


# # 获取用户输入
# word = input('give your word: ')
# # 调用函数并打印结果
# print(check_cert(word))

import random
# 定义猜数字函数
def guess_number():
    # 生成答案1-10之间
    answer = random.randint(1, 10)
    # 记录次数
    n = 1
    # 获取用户的输入并转换为整数
    number = int(input('plz give your answer: '))
    # 比较输入与答案，如果不一致，持续执行下列代码
    while number != answer:
        # 如果输入大于答案
        if number > answer:
            # 提示猜大了，并继续输入
            number = int(input('too big, guess again: '))
        # 否则
        else:
            # 提示猜小了，并继续输入
            number = int(input('too small, guess again: '))
        # 次数+1
        n += 1

    # 猜对了情况
    # 如果n为1
    if n == 1:
        # 提示欧洲人这样特殊语句
        print('欧洲人')
    # 否则
    else:
        # 提示在第几次猜对的
        print("you got it at {} times".format(n))


guess_number()








