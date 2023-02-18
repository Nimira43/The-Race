# this is the first real python program I have written by myself

def areacircle():
    diameter = int(input('Enter diameter of the circle: '))
    area = 3.14159265 * (diameter / 2) ** 2
    print('Area of circle is: ' + str(area))
    circum = 3.14159265 * diameter 
    print('Circumference of circle is: ' + str(circum))

areacircle()
    
# tutor's version

print('Specify x to close program')

while True:
    rad = input('Enter radius: ')
    if rad == 'x':
        break
    else:
        radius = float(rad)
        area = 3.14159265 * radius * radius
        print('Area of circle: ' + str(area))
        

