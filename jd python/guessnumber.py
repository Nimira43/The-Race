import random

secret_num = random.randint(1,20)
print('I am thinking of a number.')

for i in range(1,4):
    print('Try to guess the number!!!')
    guess = int(input('Enter number between 1 and 20: '))

    if guess < secret_num:
        print('That number is too low!!!')
    elif guess > secret_num:
        print('That number is too high!!!')
    else:
        break

if guess == secret_num:
    print('That is correct!!! Well done!!!')
else:
    print('Better luck next time. The correct number was ' + str(secret_num))
    
        
        
