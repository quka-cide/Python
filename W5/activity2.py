print('Please enter the items of the shopping list (type: quit to finish):')

items = []

item = None

while item != 'quit':
    item = input('Item: ')
    if item != 'quit':
        items.append(item)

print('\nThe shoping list is:')

for i in items:
    print(i)

print()
print('The shopping list with indexes is:')

for i in range(len(items)):
    item = items[i]
    print(f'{i}. {item}')

print()

index = int(input('Which item would you like to change? '))
new_item = input('What is the new item? ')

items[index] = new_item

print()
print('The shopping list with indexes is:')

for i in range(len(items)):
    item = items[i]
    print(f'{i}. {item}')