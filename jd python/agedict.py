agedict = {'nelson':32,'nigel':30,'alain':28,'ayrton':25}
for val in agedict.values():
    print(val)
for key in agedict.keys():
    print(key)
for item in agedict.items():
    print(item)
for person, age in agedict.items():
    print('The age of ' + person + ' is ' + str(age) + ' years old')
name = input('Enter name: ')
print('The age of ' + name + ' is ' + str(agedict.get(name, -1)) + ' years old')

