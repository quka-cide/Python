print('Enter a list of numbers, type 0 when finished.')

numbers = []
number = None
largest = 1
smallest = 1000

while number != 0:
    number = int(input('Enter number: '))

    if number != 0:
        numbers.append(number)

total = 0

for i in numbers:
    total += i

length = len(numbers)
average = total / length

for i in numbers:
    if i > largest:
        largest = i
    if i > 0 and i < smallest:
        smallest = i


print(f'The sum is: {total}')
print(f'The average is: {average}')
print(f'The largest number is: {largest}')
print(f'The smallest positive number is: {smallest}')

sorted_list = sorted(numbers)

print(f'The sorted list is: ')
for i in sorted_list:
    print(i)