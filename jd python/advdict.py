dict1 = {'a':1,'b':2,'c':3,'d':4,'e':5,'f':6,'g':7,'h':8}
print(dict1)
doubdict = {k:v*2 for (k,v) in dict1.items()}
print(doubdict)
dictkeys = {k*2:v for (k,v) in dict1.items()}
print(dictkeys)
num = range(100)
print(num)
newdict = {}
for n in num:
    if n%2 == 0:
        newdict[n] = n**2
print(newdict)
newdict2 = {n:n**2 for n in num if n%2 == 0}
print(newdict2)
dict2 = {'t':1,'u':2,'v':3,'w':4,'x':5,'y':6,'z':7}
dict3 = {k:v for (k,v) in dict2.items() if v>2}
print(dict2)
print(dict3)
dict4 = {k:v for (k,v) in dict2.items() if v>2 if v%2 == 0}
print(dict4)

