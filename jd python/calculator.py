def addition(num1,num2):
    result = num1 + num2
    print('The result is ' + str(result))

def subtract(num1,num2):
    result = num1 - num2
    print('The result is ' + str(result))

def multiple(num1,num2):
    result = num1 * num2
    print('The result is ' + str(result))

def divide(num1,num2):
    result = num1 / num2
    print('The result is ' + str(result))

print('1. Addition')
print('2. Subtraction')
print('3. Multiplication')
print('4. Division')
print('5. Exit')

while True:
    choice = int(input('Enter choice: '))
    if (choice >= 1 and choice <= 4):
        print('Enter two numbers')
        num1 = int(input('1st number: '))
        num2 = int(input('2nd number: '))
        if choice == 1:
            addition(num1,num2)
        elif choice == 2:
            subtract(num1,num2)
        elif choice == 3:
            multiple(num1,num2)
        else:
            choice == 4
            divide(num1,num2)
    elif choice == 5:
        break
    else:
        print('Choose number between 1 to 5')
