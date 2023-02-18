import copy

animal = 'kangaroo'
animal[2]
for i in animal:
    print(i)
fruit = ('orange','apple','banana','pear','peach','lemon','grapes')
print(fruit)
# cannot change the contents of a tuple
anlist = ['bee','wasp','hornet','buzz'] # this is a list
print(anlist)
tuple_anlist = tuple(anlist) # now it is a tuple
print(tuple_anlist)
tuple_anlist = list(('bee','wasp','hornet','buzz')) # now is a list again
print(tuple_anlist)
# convert a string to a list
string = 'Hello Lenny, how are you today?'
print(string)
listfromstring = list(string)
print(listfromstring)
tuplestring = tuple(listfromstring)
print(tuplestring)
listfromstring[12] = 'Meow!!!'
listfromstring[7] = 'Purrr!!!'
print(listfromstring)
tuple2 = ('hook','ring','saw','hammer')
list2 = ['nails','spanner','wrench','file']
tuple3 = copy.copy(tuple2)
list3 = copy.copy(list2)
print(tuple3)
print(list3)
listfromstring[21] = list3
print(listfromstring)
listfromstring[28] = fruit
print(listfromstring)
