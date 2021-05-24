import random


# define a function, get round area, get input_r as r
def get_round_area(input_r):
    # define PI
    pi = 3.14
    # get round area by area = PI * r ** 2
    area = pi * input_r ** 2
    # output area
    return area


# define a function. odd or even. input_number
def odd_or_even(input_number):
    # if input_number % 2 is 0
    if input_number % 2 == 0:
        # return 'even'
        return 'even'
    # else
    else:
        # return 'odd'
        return 'odd'

# r = input("input r please: ")
# r = float(r)
# result = get_round_area(r)
# print(result)


number = int(input('input a number: '))
result = odd_or_even(number)
print(result)




