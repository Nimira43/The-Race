password = 'password'

inputed_password = input('Please enter password: ')
inputed_password = str(inputed_password)

if inputed_password == password:
    print('Password accepted')
else:
    print('Incorrect password')
