shopping = ['beer','vapes','curry','crisps','olives','peppers']
for i in range(len(shopping)):
    print('we need to buy ' + str(i))
for i in shopping:
    print('we need to buy ' + i)
num = range(len(shopping))
print(num)
shopping.index('curry')
shopping.append('cheese')
print(shopping)
shopping.insert(4,'wine')
print(shopping)
shopping.remove('peppers')
print(shopping)
for i in shopping:
    print('we need to buy ' + i)
shopping.sort()
print(shopping)
