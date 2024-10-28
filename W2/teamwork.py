import math

square_side_len = float(input('What is the length of a side of the square (in cm)? '))
square_area = square_side_len ** 2
print(f"The area of the square is: {square_area} cm^2")
print(f"The area of the square is: {square_area / 10000} m^2")

rectangle_len = float(input('What is the length of rectangle (in cm)? '))
rectangle_width = float(input('What is the width of the rectangle (in cm)? '))
rectangle_area = rectangle_len * rectangle_width
print(f'The area of the rectangle is: {rectangle_area} cm^2')
print(f"The area of the rectangle is: {rectangle_area / 10000} m^2")

circle_radius = float(input('What is the radius of the circle (in cm)? '))
circle_area = math.pi * circle_radius ** 2
print(f'The area of the circle is: {circle_area} cm^2')
print(f"The area of the circle is: {circle_area / 10000} m^2")


#2strech
value = float(input('What value do want to use? '))

square_area2 = value ** 2 
print(f"square area: {square_area2}")
rectangle_area2 = value * value
print(f"rectangle area: {rectangle_area2}")
circle_area2 = math.pi * value ** 2
print(f"circle area: {circle_area2}")
cube_volume = value ** 3
print(f"cube volume: {cube_volume}")
sphere_volume = (4/3) * math.pi * (value ** 3)
print(f"sphere volume: {sphere_volume}")


