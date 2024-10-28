# This program calculates the total cost of a meal including the prices for children's and adult's meals,
# as well as additional items like drinks and appetizers. It allows the user to input prices for drinks
# and appetizers, which are then added to the subtotal before calculating sales tax, and change.
child_price = float(input("The price of a child's meal? "))
adult_price = float(input("The price of an adult's meal? "))
child_num = int(input('The number of children? '))
adult_num = int(input('The number of adults? '))

child_total_price = child_num * child_price
adult_total_price = adult_num * adult_price
subtotal = child_total_price + adult_total_price

drink_price = float(input("The price of drinks? "))
appetizer_price = float(input("The price of appetizers? "))
subtotal += drink_price + appetizer_price

print(f'\nSubtotal: ${subtotal:.2f}')
print()

sales_tax_rate = float(input('What is the sales tax rate? '))
sales_tax = subtotal * (sales_tax_rate / 100)
total_price = subtotal + sales_tax
print(f'Sales Tax: ${sales_tax:.2f}')
print(f'Total: ${total_price:.2f}')
print()

payment = float(input('What is the payment amount? '))
change = payment - total_price
print(f'Change: ${change:.2f}')