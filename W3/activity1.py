num1 = int(input('What is the first number? '))
num2 = int(input('What is the second number? '))

if num1 > num2:
    print('The first number is greater')
else:
    print('The first number is not greater')

if num1 == num2:
    print('The numbers are equal')
else:
    print('The numbers are not equal')

if num2 > num2:
    print('The second number is greater')
else:
    print('The second number is not greater')

print()

user_animal = input('What is your favorite animal? ')

if user_animal.lower() == 'cat':
    print("That's my favorite animal too!")
else:
    print('That one is not my favorite.')