import random

def my_print(string):
    print(string)

string1 = 'McLaren'
my_print(string1)

def hi_lenny():
    print('Hi Lenny!!!')

hi_lenny()

def getNumber(number):
    if number == 1:
        return 'The number is 1'
    elif number == 2:
        return 'The number is 2'
    elif number == 3:
        return 'The number is 3'
    elif number == 4:
        return 'The number is 4'
    elif number == 5:
        return 'The number is 5'

ran_no = random.randint(1,5)
pick = getNumber(ran_no)
my_print(pick)
