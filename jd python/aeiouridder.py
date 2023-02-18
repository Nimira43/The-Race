def remove_aeiou(newStr,string):
    aeiou = ('a', 'e', 'i', 'o', 'u')
    for c in string.lower():
        if c in aeiou:
            newStr = newStr.replace(c,'')
    return newStr

print('Enter x to exit')
string = input('Enter a few words: ')
if string == 'x':
    exit()
else:
    newStr = string
    print('Now to remove letters a, e, i, o, u....')
    newStr = remove_aeiou(newStr,string)
    print('.....which gives use: ' + newStr)
