import random


# define a function, get round area, get input_r as r
def get_round_area(input_r):
    pi = 3.14
    # area = PI * r ** 2
    area = pi * input_r ** 2
    return area


def odd_or_even(input_number):
    # 如果输入是奇数
    if input_number % 2 == 1:
        # 输出 "是奇数"
        return '是奇数'
    # 如果输入是偶数
    else:
        # 输出 "是偶数"
        return '是偶数'


def guess_game():
    # 定义 答案， 最小和最大，次数，获取用户猜的数字
    n = 1
    min_num, max_num = 0, 10
    guess_num = int(
        input(
            '请猜一个{}到{}的数字：'.format(min_num, max_num)
        ))
    answer = random.randint(min_num, max_num)
    # 如果答案不等于数字，执行以下
    while answer != guess_num:
        # 如果数字大于答案
        if guess_num > answer:
            # 输出 猜大了
            print('猜大了')
        # 否则
        else:
            # 输出 猜小了
            print('猜小了')
        # 继续获取用户猜的数字
        guess_num = int(input())
        n += 1
    # 如果次数等于1
    if n == 1:
        # 输出"欧吃矛"
        print("欧吃矛")
    # 否则
    else:
        # 输出"你在第N次猜对了"
        print("你在第{}次猜对了".format(n))
# r = input('please input r: ')
# result = get_round_area(int(r))
# print(result)
# number = input('please input a number: ')
# print(odd_or_even(int(number)))
guess_game()

