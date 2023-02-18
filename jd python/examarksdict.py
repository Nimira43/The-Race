examarks ={'Lenny':'A','Jack':'B','Yogi':'D','Monkeypox':'F'}
print('EXAM RESULT DATABASE')
name = input('Enter student name: ')
if name == None:
    exit()
    
if name in examarks:
    print('Exam mark for ' + name + ' is ' + examarks[name])
else:
    print('No student called ' + name)
