import math
def compute_area_square(num):
   return num * num

def compute_area_rectangle(length, width):
    return length * width

def compute_area_circle(radius):
    return math.pi * radius * radius

shape = ''

while shape != 'quit':
    shape = input('What shape do you have? ')

    if shape.lower() == 'square':
        side_len = float(input('Side length: '))
        area = compute_area_square(side_len)
        print(f'The area is {area}')

    if shape.lower() == 'rectangle':
        length = float(input('Length: '))
        width = float(input('Width: '))
        rect_area = compute_area_rectangle(length, width)
        print(f'The area is {rect_area}')
    
    elif shape.lower() == 'circle':
        circle_radius = float(input('Radius: '))
        circle_area = compute_area_circle(circle_radius)
        print(f'The area is {circle_area}')