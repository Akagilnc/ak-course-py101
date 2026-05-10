def check_pass(word):
    # 如果是yes
    if word == 'yes':
        return 'you are wrong'
    # 如果是no
    if word == 'no':
        return 'no, not you'
    # 如果是chengfei
    if word == 'chengfei':
        return 'yes you are'
    # 否则
    return "???"


# # 获得用户输入
# password = input('input your password: ')
# # 调用函数
# print(check_pass(password))
#


import random
def guess_number():
    # 生成答案1-10随机数，次数
    n = 1
    answer = random.randint(1, 10)
    # 用户第一次猜
    guess = int(input('give me a number: '))
    # 如果猜错了，继续猜
    while guess != answer:
        # 如果猜大了，提示并继续猜
        if guess > answer:
            guess = int(input("too big, guess again: "))
        # 如果猜小李，提示并继续猜
        else:
            guess = int(input('too small, guess again: '))
        # 次数+1
        n += 1

    # 如果是第一次猜对
    if n == 1:
        print('Good Job!')
    # 不是第一次猜对
    else:
        print('you got it at {} times'.format(n))


# guess_number()


def riot_game():
    # 定义当前次数，总次数， 胜场，负场
    n, max_n, win, lose = 0, int(input('how many times? ')), 0, 0
    # 如果当前次数小于总次数，就一直玩
    while n < max_n:
        # 双方出拳
        com = random.randint(1, 3)
        hum = int(input('1 石头 2 剪刀 3 布'))
        # 如果平局
        if com == hum:
            # 不加次数
            print ('draw')
            continue
        # 如果赢
        if (hum == 1 and com == 2) or (hum == 2 and com == 3) or (hum == 3 and com == 1):
            # 胜场，次数+1
            print('you win')
            win += 1
            n += 1
        # 如果输
        else:
            # 负场，次数+1
            print("you lose")
            lose += 1
            n += 1
    # 打印胜负场
    print("you play {} times, win {} lose {}".format(n, win, lose))
riot_game()

