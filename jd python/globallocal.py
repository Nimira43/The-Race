def funct1():
    num1 = 30
    print(num1)

funct1()
num1 =40
print(num1)

def funct2():
    global num2
    num2 = 35
    print('locally ' + str(num2))

funct2()
print('globally ' + str(num2))
num2 = 45
print(num2)
funct1()
print(num2)

def funct3(num3):
    num3 += 1
    return num3

num3 = 32
print(num3)

funct3(num3)
print(num3)

num3 = funct3(num3)
print(num3)
