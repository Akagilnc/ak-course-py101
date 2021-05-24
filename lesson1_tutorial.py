import random


# 猜数字游戏：随机生成一个1-10的答案。接受用户输入的数字
# 没猜对，计算机就会提示你，猜大了或者猜小了，并且让你继续输入，继续猜
# 猜对了，第一次猜对的，特别的祝贺语。不是第一次的，提示在第几次猜对的
def guess_number():
    # 生成一个1-10的数字，作为答案
    answer = random.randint(1, 10)
    # 定义初始次数1
    count = 1
    # 获取用户猜的数字
    number = int(input("plz guess a number: "))

    # 如果没猜对，我要提示并且继续猜
    while answer != number:
        # 如果猜大了
        if number > answer:
            # 提示猜大了，并且让用户继续输入
            number = int(input('too big, guess again: '))
        # 否则
        else:
            # 提示猜小了，并且让用户继续输入
            number = int(input("too small, guess again: "))
        # 次数+1
        count += 1

    # 如果不是第一次猜对
    if count != 1:
        # 返回 你是在第X次猜对的
        return '你是在第{}次猜对的'.format(count)
    # 否则
    else:
        # 返回 特别祝贺语
        return "欧吃矛"


result = guess_number()
print(result)
