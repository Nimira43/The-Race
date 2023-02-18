# or        

def calrad(rad):
    radius = float(rad)
    area = 3.14159265 * radius * radius
    print('Area of circle: ' + str(area))

print('Specify x to close program')

while True:
    rad = input('Enter radius: ')
    if rad == 'x':
        break
    calrad(rad)
