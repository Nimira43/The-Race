#x = input("Enter number: ")
#y = input("Enter another: ")
#z = int(x) + int(y)
#print(z)

c = input("Enter a temperature in celsius: ")
f = (9/5) * int(c) + 32
print(f)

sec = input("Enter an amount of seconds ")
min = input("Enter an amount of minutes ")

secToMin = int(sec) / 60
totMin = secToMin + int(min)
hours = totMin / 60

print(hours)
