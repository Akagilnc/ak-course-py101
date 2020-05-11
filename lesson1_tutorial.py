import random


# 猜数字游戏：计算机每次随机生成一个答案1-10，然后接受用户输入的数字
# 没猜对，计算机会提示你，是猜大了还是猜小了，并且让你继续输入，继续猜
# 猜对了，第一次猜对的，会有特别的祝贺语。不是第一次，提示他你在第几次猜对了
def guess_number():
    # 随机生成一个1-10答案

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


# 定义猜拳函数。1 代表石头， 2 代表剪刀 3 代表布
def finger_guessing_game():
    # 电脑生成1-3的随机数字代表 石头剪刀布
    com_hand = random.randint(1, 3)
    # 获取玩家的输入
    human_hand = int(input('1石头, 2剪刀, 3布, come on: '))

    # 如果玩家没有获胜，就一直玩下去
    while human_hand - com_hand != -1 and human_hand - com_hand != 2:
        # 如果是平手， 提示平手
        if human_hand == com_hand:
            print("平手，再来")
        # 否则就是电脑赢了
        else:
            print('电脑赢了，再来')
        # 无论是平手还是电脑赢了，都重新获得双方的输入
        human_hand = int(input('1石头, 2剪刀, 3布, come on: '))
        com_hand = random.randint(1, 3)
    # 恭喜玩家，结束
    print('恭喜你')
