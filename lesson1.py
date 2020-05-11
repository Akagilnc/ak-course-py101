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


# 猜数字游戏：计算机每次随机生成一个答案1-10，然后接受用户输入的数字
# 没猜对，计算机会提示你，是猜大了还是猜小了，并且让你继续输入，继续猜
# 猜对了，第一次猜对的，会有特别的祝贺语。不是第一次，提示他你在第几次猜对了
def guess_number():
    # 随机生成一个1-10答案
    import random
    answer = random.randint(1, 10)
    # 获取用户输入的数字
    number = int(input('please guess a number: '))
    # 定义一个次数
    n = 1
    # 没猜对，提示用户猜大了或者猜小了，并且继续猜
    while answer != number:
        # 如果猜大了
        if number > answer:
            # 提示猜大了，继续输入
            number = int(input('too big, please guess again: '))
        # 否则
        else:
            # 提示猜小了，继续输入
            number = int(input('too small, please guess again: '))
        # 次数也要+1
        n += 1

    # 非第一次猜对
    if n != 1:
        # 打印你是第几次猜对的
        print('你是在第{}次猜对的'.format(n))
    # 第一次猜对
    else:
        # 打印特别祝贺语
        print('欧吃矛')


print_round_area()
odd_or_even()
# guess_number()
