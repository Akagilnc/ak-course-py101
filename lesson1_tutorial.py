import random


# 猜数字游戏：计算机每次随机生成一个答案1-x，然后接受用户输入的数字
# 没猜对，计算机会提示你，是猜大了还是猜小了，并且让你继续输入，继续猜
# 猜对了，第一次猜对的，会有特别的祝贺语。不是第一次，提示他你在第几次猜对了
def guess_number(input_max):
    # 生成一个1-max数字作为答案
    answer = random.randint(1, input_max)
    # 定义一个初始的次数1
    n = 1
    # 获取用户猜测的数字
    number = int(input('plz guess a number: '))

    # 没猜对，提示用户是猜大了还是小了，并且继续猜
    while answer != number:
        # 如果猜大了
        if number > answer:
            # 提示猜大了，继续输入数字
            number = int(input('too big, guess again: '))
        # 否则
        else:
            # 提示猜小了，继续输入
            number = int(input('too small, guess again: '))
        # 次数要 +1
        n += 1

    # 如果不是第一次猜对
    if n != 1:
        # 返回 你是在第X次猜对的
        return '你是在第{}次猜对的'.format(n)
    # 第一次猜对
    else:
        # 打印特别祝贺语
        return '欧吃矛'


# 调用函数，需要的输入是一个最大值，10
result = guess_number(10)
print(result)

# 石头剪刀布
# 1 石头 2 剪刀 3 布
# 如果是电脑赢或者平手，就继续玩
# 如果你赢了，就提示 恭喜 并且结束

