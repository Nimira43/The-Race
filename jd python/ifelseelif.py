input_num = input('Enter a number: ')
input_num = int(input_num)
print(input_num)

if input_num > 0:
    print('Number ' + str(input_num) + ' is bigger than 0')
elif input_num == 0:
    print('Number ' + str(input_num) + ' equal to 0')
else:
    print('Number ' + str(input_num) + ' is smaller than 0')
    
