# 定义函数
def odd_or_even(num):
    # 如果对二求模 等于0
    if num%2 == 0:
        # 输出偶数
        return 'even'
    # 否则
    else:
        # 输出奇数
        return 'odd'


# # 获得一个数字输入
# number = int(input('请输入要判断的数字: '))
# # 调用函数
# answer = odd_or_even(number)
# # 打印结果
# print(answer)


# 定义函数
def is_divisible_3(num):
    # 对3求余数，如果余数为0，输出
    if num % 3 == 0:
        return 'divisible by 3'
    # 否则 输出
    else:
        return 'sorry but no'


# # 获得数字输入，并调用函数打印结果
# number = int(input('请输入要判断的数字：'))
# print(is_divisible_3(number))


# 定义函数
def check_pass(word):
    # 判断输入是否为yes
    if word == 'yes':
        return 'you are wrong'
    # 判断输入是否为no
    if word == 'no':
        return 'no, not you'
    # 判断输入是否为chengfei
    if word == 'chengfei':
        return 'yes you are'
    # 否则，输出???
    else:
        return '???'


# 获得word，然后调用函数并打印结果
password = input('请输入口令: ')
print(check_pass(password))



