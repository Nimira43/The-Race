def chklarg(num1,num2,num3):
    global largest
    largest = num1
    if largest < num2:
        if num2 > num3:
            largest = num2
        else:
            largest = num3
    elif largest < num3:
        if num3 > num2:
            largest = num3
        else:
            largest = num2
    else:
        largest = num1

count = 1
print('Enter x to exit.')
print('Enter three numbers.')
num1 = input('1st number: ')
if num1 == 'x':
    exit()
else:
    num1 = int(num1)
    num2 = int(input('2nd number: '))
    num3 = int(input('3rd number: '))
    chklarg(num1,num2,num3)
    if (num1 == num2 and num1 == num3):
        count = 0
    if count == 0:
        print('All three number are the same.')
    else:
        print('Largest number is ' + str(largest))
        
        
