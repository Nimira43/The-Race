inputstring ='Lenny is a beautiful and clever super cat'

def revstr(string):
    print(string[::-1])

def evenodd(num):
    if (num % 2 == 0):
        print('The number is even')
    else:
        print('The number is odd')
    
revstr(inputstring)

inputstring = input('Enter some words:  ')
revstr(inputstring)

num = int(input('Enter a number: '))
evenodd(num)             
