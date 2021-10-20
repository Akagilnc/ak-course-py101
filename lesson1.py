import random


# 猜数字函数
def guess_number():
    # 自动生成随机答案1-10，定义次数
    n = 1
    answer = random.randint(1, 10)
    number = int(input('pls input your answer: '))
    while answer != number:
        # 如果猜大了
        if number > answer:
            print('猜大了,请重新输入：')
        else:
            print('猜小了,请重新输入：')
        # 重新获取玩家输入，并记录次数
        number = int(input())
        n += 1

    # 如果是第一次猜对
    if n == 1:
        # 输出特殊的句子
        print('欧吃矛')
    # 否则
    else:
        # 输出 你是在第几次猜对了
        print('恭喜，你在第{}次猜对了！'.format(n))


guess_number()
